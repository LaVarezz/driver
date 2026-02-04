from project.engine.managers.basic_manager import Manager


class WidgetManager(Manager):
    def __init__(self, main):
        super().__init__(main)
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
        self.layers = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
            5: [],
            6: [],
        }

    def update(self):
        ''' если нужно будет оптимизировать, то я буду держать список с пуллом и после каждого изменения состава виджетов этот список пересобирать '''
        for layer in self.layers.values():
            for widget in layer:
                widget.update()

    def draw(self, window):
        for layer in self.layers.values():
            for widget in layer:
                widget.draw(window)

    def create_widget(self, widget, layer):
        self.layers[layer].append(widget)

    def remove_widget(self, widget_id):
        for layer in self.layers:
            for widget in self.layers[layer][:]:
                if widget.id == widget_id:
                    self.layers[layer].remove(widget)
