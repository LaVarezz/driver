
import pygame as pg

from space.battle.updates import update_all_mode
from space.engine.contollers.handler import event_handler
from space.settings.protocols.protocols import SceneLike


class MainMenu(SceneLike):
    def mainloop(self):
        self.update_interface()
        event_handler(self)

    def update_interface(self):
        update_all_mode(self.main)
