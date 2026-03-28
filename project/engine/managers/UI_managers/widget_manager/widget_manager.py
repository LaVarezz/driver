from project.data.protocols.protocols import MainLike, WidgetLike
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

        self.main.events.subscribe(self, EventTypes.BUTTONCHANGE, 0)
        self.main.events.subscribe(self, EventTypes.SCENEOBJECTSCREATED)
        self.main.events.subscribe(self, EventTypes.SCENEHASCHANGED)

    def update(self):
        ''' если нужно будет оптимизировать, то я буду держать список с пуллом и после каждого изменения состава виджетов этот список пересобирать '''
        self.UI_run()
        # if self.captured_id:
        #    widget = self.get_widget(self.captured_id)
        for layer in self.layers.values():
            for panel in layer.values():
                panel.update()

    def draw(self, window):
        for layer in self.layers.values():
            for panel in layer.values():
                panel.draw(window)

    def get_widget(self, id, layer=-1):
        ''' Возвращает наведенный виджет (?) '''
        if layer >= 0:
            return self.layers[layer][id]
        for de_layer in self.layers.values():
            for panel in de_layer.values():
                if id == panel.id:
                    return panel
                if id in panel.id_list:
                    return panel.id_list[id]

    def get_all_panels(self):
        d = []
        for layer in self.layers.values():
            for panel in layer.values():
                d.append(panel)
        return d

    def create_widget(self, widget):
        if widget.type == 'panel':
            self.layers[widget.layer][widget.id] = widget
        else:
            self.get_widget(widget.panel).add_widget(widget)

    def remove_widget(self, widget_id):
        for layer in self.layers:
            for widget in self.layers[layer].values()[:]:
                if widget.id == widget_id:
                    del self.layers[layer][widget.id]
                    # при ошибочном вызове создаст исключение

    def UI_run(self):
        ''' Switch hovered button's id '''
        CG = False  # click given
        px, py = self.main.cursor.get_mouse_states()[:2]
        for layer in [self.layers[i] for i in range(self.layers_int, -1, -1)]:
            for widget in layer.values():
                hovered_widget = widget.check_collide(px, py)
                if hovered_widget:
                    CG = hovered_widget
                    self.hovered_id = hovered_widget.id
                    break
            if CG: break
        if not CG:
            self.hovered_id = None

    def trigger(self, msg, data) -> bool:
        if msg == EventTypes.BUTTONCHANGE:
            '''   изменяет выбранную и наведенную кнопку
             И ТРИГГЕРИТ ЕЕ!!!  '''
            but = data['buttons']
            if (0, 1) in but:
                self.captured_id = self.hovered_id
                if self.captured_id:
                    return True
            if (0, 0) in but:
                if self.captured_id and self.captured_id == self.hovered_id:
                    self.get_widget(self.captured_id).process()
                    return True
                self.captured_id = None

        if msg == EventTypes.SCENEOBJECTSCREATED:
            for wid in data["widgets"]:
                self.create_widget(wid)


        if msg == EventTypes.SCENEHASCHANGED:
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


    def __repr__(self):
        return 'widget_manager'
