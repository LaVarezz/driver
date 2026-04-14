from project.data.protocols.protocols import MainLike
from project.engine.modules.UI_modules.widget_module.widgets.basic_widget import BasicWidget
from project.engine.modules.UI_modules.widget_module.widgets.labels.sublabel import Sublabel
from project.engine.utills.logging.log import log_info


class Label(BasicWidget):
    def __init__(self, main: MainLike, cords, size, id, layer, panel, anchor, offset, moveable, visible, enabled,
                 text_pattern, text_anchor, text_size):
        super().__init__(main, cords, size, id, layer, panel, anchor, offset, moveable, visible, enabled)
        self.main = main
        self.type = 'label'
        self.text_pattern = text_pattern
        self.text_anchor = text_anchor
        self.text_case = []
        self.text_size = text_size

        def convert_pattern(self):
            ''' Оперирует с текстовым шаблоном text_pattern, переводит шаблон в текстовые объекты вида
            list[[sublabel, object, value] или object[] в зависимости от того, является ли объект статичным или динамичным
            принцип работы:
            [1] - заменяет все %% на ^ - символ не должен использоваться в тексте
            [2] - разбивает строку на части по ^
            [3] - проходится по каждой разбитой части и превращает ее либо в текст, либо в слушателя
            [3.1] - если кейсом является текст: в text_case добавляется |text_object|
            [3.2] - если кейсом явлется слушатель: в text_case добавляется list[sublabel, object, value]
            [4] - проводится центрирование текста внутри label. См. to_anchor()
            обработанные данные хранятся в self.text_case
            вход: фиксированный text_pattern
            итог: заполняетя text_case, вызывается to_anchor
            примечания: sublabelом объект считается, если имеет хотя бы одну зависимость, т.е обращение "main" воспринимается как текст
            пример входных данных: "Welcome to the Hell! %%main|modules|window_module|time%%"
            '''
            lx = ly = 0
            dirty_converted = self.text_pattern.replace("%%", "^") # 1
            dirty_converted = dirty_converted.split("^") # 2
            for case in dirty_converted: #3
                if not case:
                    continue
                if "|" not in case: #3.1
                    obj = self.main.modules.text_module.create_text_object((lx, ly), (None, None), self.surface,
                                                                            case, self.text_size, 5)
                    self.text_case.append(obj)
                    lx += obj.lx
                else:
                    if case:
                        path = case.split('|') #3.2
                        sub = Sublabel(self.main, path)
                        obj = self.main.modules.text_module.create_text_object((lx, ly), (None, None), self.surface, sub.value,
                                                                                self.text_size, 5)
                        self.text_case.append([sub, obj, sub.value])
                        lx += obj.lx

            log_info(f"Текстовое поле с текстовыми объектами: {self.text_case} успешно создана.")

            self.to_anchor(lx) #4

        convert_pattern(self)

    def to_anchor(self, lx):
        dx = 0
        if "CENTER" in self.text_anchor:
            dx = (self.width - lx) // 2
        if dx:
            for case in self.text_case:
                if isinstance(case, list):
                    case[1].replace(dx)
                else:
                    case.replace(dx)

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
            "text_anchor": self.text_anchor,
            "text_size": self.text_size,
            "offset": self.offset
        }
        return d

    def update(self):
        ''' ВЫПОЛНЯЕТ ФУНКЦИИ DRAW!!! '''
        self.surface.fill('black')
        for case in self.text_case:
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
