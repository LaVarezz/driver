from project.data.protocols.protocols import MainLike
from project.engine.managers.widget_manager.widgets.basic_widget import BasicWidget
from project.engine.managers.widget_manager.widgets.labels.sublabel import Sublabel


class Label(BasicWidget):
    def __init__(self, main: MainLike, cords, size, id, layer, panel, anchor, offset, moveable, visible, enabled,
                 text_pattern):
        super().__init__(main, cords, size, id, layer, panel, anchor, offset, moveable, visible, enabled)
        self.main = main
        self.type = 'label'
        self.text_pattern = text_pattern
        self.text = []
        self.convert_pattern()

    def convert_pattern(self):
        lx = ly = 0
        dirty_converted = self.text_pattern.split('%')
        for component in dirty_converted:
            if "|" not in component:
                if component:
                    obj = self.main.manager.text_manager.create_text_object((lx, ly), (None, 25), self.surface, component, 1, 5)
                    self.text.append(obj)
                    lx += obj.lx

            else:
                path = component.removeprefix('%').removesuffix('%').split('|')
                sub = Sublabel(self.main, path)
                obj = self.main.manager.text_manager.create_text_object((lx, ly), (None, 25), self.surface, sub.value,
                                                                        1, 5)
                self.text.append([sub, obj, sub.value])
                lx += obj.lx
        print(self.text, 12341234123)

    def get_data_json_like(self) -> dict:
        d = {
            "position": [self.x, self.y],
            "size": [self.width, self.height],
            "text_pattern": self.text_pattern,
            "panel": self.panel,
            "layer": self.layer,
            "moveable": self.moveable,
            "visible": self.visible,
            "enabled": self.enabled,
            "anchor": self.anchor,
            "offset": self.offset
        }
        return d

    def update(self):
        ''' ВЫПОЛНЯЕТ ФУНКЦИИ DRAW!!! '''
        self.surface.fill('black')
        for case in self.text:
            if isinstance(case, list):
                """ Sublabel, object-listener, value """
                case[0].update()
                if case[0].value != case[-1]:
                    case[-1] = case[0].value
                    case[1].recalculate(case[0].value)

    def process(self):
        pass

    def __repr__(self):
        return f'Label with text'
