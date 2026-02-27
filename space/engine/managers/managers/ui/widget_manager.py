from space.engine.debug.logs.main_log import log_info
from space.settings.protocols.protocols import MainLike


class UImanager:
    def __init__(self, main: MainLike):
        self.main = main
        self.layers = [[]]
        log_info('Менеджер интерфейса создан.')

    def add_widget(self, widget, layer):
        if widget.parent:
            widget.parent.widgets.append(widget)

        if len(self.layers) < layer:
            while len(self.layers) <= layer:
                self.layers.append([])
        self.layers[layer].append(widget)

    def delete_widget(self, widget):
        if widget.parent: widget.parent.widgets.remove(widget)

        for layer in self.layers:
            if widget in layer:
                layer.remove(widget)
                if not layer:
                    del layer

    def get_widgets(self):
        return [j for i in self.layers for j in i]

    def activate_widget(self, pos):
        for layer in reversed(self.layers):
            for widget in layer:
                if widget.check_collide(pos):
                    widget.activated = True
                    widget.handle_event(self, pos)
                    ''' statistic '''
                    self.main.manager.statistic.update_statistic('Кликов по виджетам: ', 1)
                    return False
                else:
                    widget.activated = False

    def deactivate_widgets(self):
        for layer in reversed(self.layers):
            for widget in layer:
                widget.activated = False

    def update_UI(self):
        for layer in reversed(self.layers):
            for widget in layer:
                widget.update()

    def draw_UI(self, window):
        for layer in self.layers:
            for widget in layer:
                if not widget.parent:
                    widget.draw(window)

    def destroy_layer(self, layer):
        del self.layers[layer]
        log_info(f'Слой {layer} уничтожен')

    def destroy_UI(self):
        self.layers = []
        log_info('Интерфейс уничтожен.')

    def __repr__(self):
        return 'UI manager'
