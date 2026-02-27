from project.data.protocols.protocols import MainLike
from project.engine.managers.widget_manager.widgets.basic_widget import BasicWidget


class Button(BasicWidget):
    def __init__(self, main: MainLike, cords, size, id, text, command, layer, panel, moveable=False, visible=True, enabled=True, anchor=None,
                 offset=(0, 0)):
        super().__init__(main, cords, size, id, layer, panel, anchor, offset, moveable, visible, enabled)
        self.main = main
        self.command = command[0]
        self.data = command[1]
        self.command_raw = command[2]
        self.text = text
        self.type = 'button'
        self.main.manager.text_manager.create_text_object((0, 0), (self.width, self.height), self.surface, self.text, 1,
                                                          center=(1, 1))

    def __call__(self):
        if not self.main.manager.engine_manager.able_to_change:
            self.command(self.main, self.data)


    def update(self):
        pass

    def draw(self, window):
        if self.visible:
            window.blit(self.surface, self.rect)

    def process(self):
        self()

    def get_data_json_like(self):
        d = {
            "position": [self.x, self.y],
            "size": [self.width, self.height],
            "text": self.text,
            "command": {
                "action": self.command_raw,
                "data": self.data
            },
            "panel": self.panel,
            "layer": self.layer,
            "moveable": self.moveable,
            "visible": self.visible,
            "enabled": self.enabled,
            "anchor": self.anchor,
            "offset": self.offset
        }
        return d

    def __repr__(self):
        return f'Button with text: {self.text}'
