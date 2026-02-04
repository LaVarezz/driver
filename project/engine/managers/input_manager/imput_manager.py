from project.engine.events.event_types import EventTypes
from project.engine.managers.basic_manager import Manager

import pygame as pg

class InputManager(Manager):
    def __init__(self, main):
        super().__init__(main)

    def setup(self, data):
        pass

    def get_inputs(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                data = {
                    'run': False
                }
                self.main.events.emit(EventTypes.EXITGAMEEVENT, data)
