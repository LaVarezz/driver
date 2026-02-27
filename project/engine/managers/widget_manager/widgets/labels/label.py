from re import *

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
        self.convert_pattern()

    def convert_pattern(self):
        for i in finditer("%(.)+%", self.text_pattern):
            path = i.group().removeprefix('%').removesuffix('%').split('|')
            Sublabel(self.main, path).value


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


    def process(self):
        pass


    def __repr__(self):
        return f'Label with text'
