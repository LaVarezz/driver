
import pygame as pg

from space.engine.contollers.handler import event_handler
from space.settings.protocols.protocols import SceneLike


class MainSettingsMenu(SceneLike):
    def mainloop(self):
        self.update_interface()
        event_handler(self)

    def update_interface(self):
        self.main.window.fill('black')
        self.main.manager.widgets.update_UI()
        self.main.manager.widgets.draw_UI(self.main.window)
        pg.display.update()
