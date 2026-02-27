from space.engine.debug.logs.main_log import log_info
from space.ui.animations.animation_effects.death_panel_effect import DeathPanelEffect
from space.ui.widgets.buttons.button import Button
from space.ui.widgets.buttons.commands import select_moving_command, select_attack_command
from space.ui.widgets.frames.frame import Frame
from space.ui.widgets.panels.panel import Panel


class ControlPanel(Panel):
    def __init__(self, main, content):

        w = main.ws.WIDTH
        h = main.ws.HEIGHT
        super().__init__((w*4//5, 0), (w // 5, h), main)
        self.main_width = w // 5
        self.main_height = main.ws.HEIGHT

        self.reset_panel(content, True)

        ''' Кнопка перемещения '''
        self.UI.add_widget(Button((15, self.main_height - 100), (180, 60), main, ('Move to', \
                                                                                 self.main.ws.GLOBAL_TEXT_CACHE['big']),
                                  command=select_moving_command, parent=self, center=(False, False)), 5)
        ''' Кнопка атаки '''
        self.UI.add_widget(Button((205, self.main_height - 100), (180, 60), main, ('Blast', \
                                                                                 self.main.ws.GLOBAL_TEXT_CACHE['big']),
                                  command=select_attack_command, parent=self, center=(False, False)), 5)


        txt = (
            'Control panel',
            '\n',
            'Ship: ',
            (None, 'selected_ship_changed', lambda d: [f'{d.object}'], content),
            '\n',
            'Выбрано: ',
            (None, 'selected_move_changed', lambda d: [f'{d.value}'], self.main.manager.clicks, 'state'),
        )


        self.UI.add_widget(Frame((self.main_width//20, 30), (self.main_width-self.main_width//10, 160), main, txt, parent=self, center=(True, False)), 5)

    def update(self):
        pass

    def draw(self, window):
        self.surface.fill('orange')
        for widget in self.widgets:
            widget.draw(self.surface)
        window.blit(self.surface, self.rect)

    def kill_panel(self):
        self.main.manager.animation.add_effect(
            DeathPanelEffect(self))
        self.main.manager.overlay.delete_widget(self)
        self.main.scene.game.control_panel = None

    def destroy_panel(self):
        self.main.manager.overlay.delete_widget(self)
        for widget in self.widgets:
            self.main.manager.widgets.delete_widget(widget)
            self.widgets.remove(widget)
        log_info('Панель управления уничтожена')

    def reset_panel(self, content, new=False):
        self.content = content
        if not new:
            self.main.manager.events.emit('selected_ship_changed', None, True, object=self.content)
