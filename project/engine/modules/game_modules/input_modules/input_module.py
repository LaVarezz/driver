from project.engine.events.event_types import EventTypes
from project.engine.modules.basic_module import Module

import pygame as pg

class InputModule(Module):
    def __init__(self, main):
        super().__init__(main)

    def setup(self, data):
        pass

    def process_inputs(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                data = {
                    'run': False
                }
                self.main.events.emit(EventTypes.EXITGAMEEVENT, data)
