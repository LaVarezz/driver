from fileinput import hook_encoded
from idlelib.macosx import hideTkConsole

from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes
from project.engine.managers.basic_manager import Manager


class WidgetManager(Manager):
    def __init__(self, main: MainLike):
        super().__init__()
        ''' Слои
         0 - фон карты
         1 - отображение игровых объектов
         2 - панели интерфейса
         3 - панели overlay
         4 - резервный overlay(на всякий)
         5 - дебаг панель
         6 - настройки + выход
         при этом каждая панель так же обладает слоями, и обрабатывает кнопки в соответствии со слоями
         '''
        self.main = main
        self.layers = {
            0: {},
            1: {},
            2: {},
            3: {},
            4: {},
            5: {},
            6: {},
        }
        self.layers_int = 6

        self.hovered_id = None
        self.captured_id = None

        self.main.events.subscribe(self, EventTypes.BUTTONCHANGE)

    def update(self):
        ''' если нужно будет оптимизировать, то я буду держать список с пуллом и после каждого изменения состава виджетов этот список пересобирать '''
        self.UI_run()
        if self.captured_id:
            widget = self.get_widget(self.captured_id)
            widget.surface.fill('blue')

        for layer in self.layers.values():
            for widget in layer.values():
                widget.update()

    def draw(self, window):
        for layer in self.layers.values():
            for widget in layer.values():
                widget.draw(window)

    def check_id(self, id):
        ks = []
        for keys_lists in self.layers.values():
            for kys in keys_lists.keys():
                ks.append(kys)
        return id in ks

    def get_widget(self, id, layer=-1):
        if layer >= 0:
            return self.layers[layer][id]
        for de_layer in self.layers.values():
            if id in de_layer.keys():
                return de_layer[id]

    def create_widget(self, widget, layer):
        if not self.check_id(widget.id):
            self.layers[layer][widget.id] = widget
        else:
            widget.create_id()
            self.create_widget(widget, layer)

    def remove_widget(self, widget_id):
        for layer in self.layers:
            for widget in self.layers[layer].values()[:]:
                if widget.id == widget_id:
                    del self.layers[layer][id]
                    # при ошибочном вызове создаст исключение

    def UI_run(self):
        CG = False  # click given
        px, py, rel = self.main.cursor.get_mouse_states()
        for layer in [self.layers[i] for i in range(self.layers_int, -1, -1)]:
            for widget in layer.values():
                if widget.check_collide(px, py):
                    CG = widget
                    self.hovered_id = widget.id
                    break
            if CG: break
        if not CG:
            self.hovered_id = None

    def trigger(self, msg, data):
        if msg == EventTypes.BUTTONCHANGE:
            but = data['buttons']
            if (0, 1) in but:
                self.captured_id = self.hovered_id
            if (0, 0) in but:
                if self.captured_id and self.captured_id == self.hovered_id:
                    self.get_widget(self.captured_id).process()
                self.captured_id = None

