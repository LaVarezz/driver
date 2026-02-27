from space.battle.events.either.listeners.panel_listener import PanelListener
from space.engine.scenes.scenes.battle_scene import BattleScene

from space.settings.protocols.protocols import MainLike
from space.ui.widgets.panels.constant_panels.contoll_panel import ControlPanel
from space.ui.widgets.panels.constant_panels.overlay_panel import OverlayPanel
from space.ui.widgets.panels.constant_panels.quick_info_panel import QuickInfoPanel


class OverlayManager:
    def __init__(self, main: MainLike):
        self.main = main
        self.non_pausing_panels = []
        self.pausing_panels = []

        self.first_setup = False

    def add_widget(self, widget, pause=True):
        if pause:
            self.pausing_panels.append(widget)
        else:
            self.non_pausing_panels.append(widget)

    def delete_widget(self, widget):
        if widget in self.pausing_panels:
            self.pausing_panels.remove(widget)
        elif widget in self.non_pausing_panels:
            self.non_pausing_panels.remove(widget)

    def is_widget_exist(self, widget):
        return widget in self.non_pausing_panels or widget in self.pausing_panels

    def setup(self):
        self.main.manager.events.subscribe('pointed_ship_changed_raw', PanelListener(self.main, self, (QuickInfoPanel, 'quick_info_panel'), 1))
        self.main.manager.events.subscribe('selected_ship_changed_raw', PanelListener(self.main, self, (ControlPanel, 'control_panel'), 1))
        self.main.manager.events.subscribe('settings_panel_changed', PanelListener(self.main, self, (OverlayPanel, 'settings_panel'), 1))

    def update_overlay_UI(self):
        if not self.first_setup:
            if isinstance(self.main.scene, BattleScene):
                self.first_setup = True
                self.setup()

        for widget in self.pausing_panels:
            widget.update()
        for widget in self.non_pausing_panels:
            widget.update()

    def draw_overlay_UI(self):
        for widget in self.pausing_panels:
            widget.draw(self.main.window)

        for widget in self.non_pausing_panels:
            widget.draw(self.main.window)

    def check_pause(self):
        if self.pausing_panels:
            return True
        return False

    def __repr__(self):
        return 'Overlay manager'
