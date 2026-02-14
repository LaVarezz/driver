import pygame as pg

from project.engine.events.event_types import EventTypes
from project.engine.managers.basic_manager import Manager
from project.engine.utills.logging.log import log_info


class WindowManager(Manager):
    ''' управление окном '''

    def __init__(self, main):
        super().__init__(main)
        log_info('Window manager is being creating')
        self.app = None
        self.clock = None
        self.dt = float(0)
        self.run = None
        log_info('Window manager has created')

    def setup(self, data):
        log_info('Window manager is on setup')
        self.app = pg.display.set_mode((data.open_settings['width'], data.open_settings['height']))
        self.clock = pg.time.Clock()
        self.fps = data.open_settings['fps_limit']
        self.time = 0

        d = {}
        self.main.manager.time_manager.create_timer(self.time, 5, EventTypes.TIMERSHUTDOWN, d, True)
        self.main.events.subscribe(self, EventTypes.TIMERSHUTDOWN)
        log_info('Window manager setup if finish')

    def update_window(self):
        self.time += 0.0083
        pg.display.update()
        self.clock.tick(self.main.settings.open_settings['fps_limit'])

    def trigger(self, event_type, data):
        if event_type == EventTypes.TIMERSHUTDOWN:
            print('process...')
