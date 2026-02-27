from space.engine.debug.logs.main_log import log_info
from space.ui.widgets.buttons.button import Button
from space.ui.widgets.buttons.commands import set_main_scene, set_main_settings_scene
from space.ui.widgets.panels.panel import Panel


class OverlayPanel(Panel):
    def __init__(self, main, *args, **kwargs):
        super().__init__((0, 0), (300, main.ws.HEIGHT), main, 128)

        self.UI.add_widget(Button((30, 30), (200, 80), self.main, ('Game', self.main.ws.GLOBAL_TEXT_CACHE['big']),
                             command=set_main_scene,
                             parent=self, center=(True, False), alpha=180), 3)
        self.UI.add_widget(Button((30, 180), (200, 80), self.main, ('Settings', self.main.ws.GLOBAL_TEXT_CACHE['big']),
                             command=set_main_settings_scene,
                             parent=self, center=(True, False), alpha=180), 3)
        self.main_width = 200
        self.main_height = self.main.ws.HEIGHT

    def update(self):
        pass

    def draw(self, window):
        self.surface.fill('red')
        for widget in self.widgets:
            widget.draw(window=self.surface)
        window.blit(self.surface, (self.x, self.y))

    def kill_panel(self):
        self.destroy_panel()


    def destroy_panel(self):
        self.main.manager.overlay.delete_widget(self)
        for widget in self.main.manager.widgets.get_widgets():
            if widget.parent and widget.parent == self:
                self.main.manager.widgets.delete_widget(widget)
        log_info('Панель параметров уничтожена')
