from space.scripts.utils.battle_utils.get_ship import get_object
from space.ui.animations.animation_effects.death_panel_effect import DeathPanelEffect
from space.ui.widgets.frames.frame import Frame
from space.ui.widgets.panels.panel import Panel


class QuickInfoPanel(Panel):
    def __init__(self, main, content):
        px = 400
        py = 300
        super().__init__((main.ws.WIDTH - px - 300, main.ws.HEIGHT-py) if main.scene.game.control_panel else (main.ws.WIDTH - px, main.ws.HEIGHT-py),
                         (px, py), main)
        self.main_width = main.ws.WIDTH
        self.main_height = main.ws.HEIGHT

        self.reset_panel(content, True)

        self.previous_ship = None

        s = get_object(self.main, self.main.manager.cursor.pointed_ship)
        txt = (
            'INFO',
            '\n'
            'Ship: ',
            (None, 'pointed_ship_changed', lambda d: [f'{d.object}'], s, ''),
            '\n',
            'Health: ',
            (None, 'pointed_ship_changed', lambda d: [f'{d.object.health}'], s, ''),
        )


        self.UI.add_widget(Frame((3, 3), (px, py), main, txt, parent=self, center=(False, False), font=2), 5)

    def update(self):
        s =  self.main.manager.cursor.pointed_ship
        if s:
            if s != self.content:
                self.reset_panel(s)

    def draw(self, window):
        self.surface.fill('blue')
        for widget in self.widgets:
            widget.draw(self.surface)
        window.blit(self.surface, self.rect)

    def kill_panel(self):
        self.main.manager.animation.add_effect(
            DeathPanelEffect(self))
        self.main.manager.overlay.delete_widget(self)
        self.main.scene.game.quick_info_panel = None


    def destroy_panel(self):
        for widget in self.widgets:
            self.main.manager.widgets.delete_widget(widget)
            self.widgets.remove(widget)

    def reset_panel(self, content, new=False):
        self.content = content
        if not new:
            self.main.manager.events.emit('pointed_ship_changed', None, True, object=get_object(self.main, self.content))