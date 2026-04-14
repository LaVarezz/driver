from project.data.protocols.protocols import MainLike
from project.engine.modules.UI_modules.widget_module.widgets.basic_widget import BasicWidget


class Panel(BasicWidget):
    ''' All widgets are assembled in the panels '''

    def __init__(self, main: MainLike, cords, size, id, layer, panel=None, moveable=False, visible=True, enabled=True,
                 anchor=None, offset=(0, 0)):
        super().__init__(main, cords, size, id, layer, panel, anchor, offset, moveable, visible, enabled)
        self.layers = {
            0: {},
            1: {},
            2: {}
        }
        self.id_list = {}
        self.panel = panel

        self.surface.fill('green')

        self.type = 'panel'

    def add_widget(self, widget):
        self.layers[widget.layer][widget.id] = widget
        self.id_list[widget.id] = widget

    def process(self):
        pass

    def update(self):
        for layer in self.layers.values():
            for widget in layer.values():
                widget.update()

    def draw(self, window):
        self.surface.fill('green')
        for layer in self.layers.values():
            for widget in layer.values():
                widget.draw(self.surface)
        window.blit(self.surface, self.rect)

    def get_data_json_like(self):
        d = {
            "position": [self.x, self.y],
            "size": [self.width, self.height],
            "layer": self.layer,
            "panel": self.panel,
            "moveable": self.moveable,
            "visible": self.visible,
            "enabled": self.enabled,
            "anchor": self.anchor,
            "offset": self.offset
        }
        return d

    def check_collide(self, px, py):
        real_x, real_y = px - self.x, py - self.y

        for layer in self.layers:
            for wid in self.layers[layer].values():
                if wid.rect.collidepoint(real_x, real_y):
                    return wid
        if self.rect.collidepoint(px, py):
            return self

    def __repr__(self):
        return 'panel'
