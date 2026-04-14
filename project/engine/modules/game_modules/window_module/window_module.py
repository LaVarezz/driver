import pygame as pg

from project.engine.modules.basic_module import Module
from project.engine.utills.logging.log import log_info


class WindowModule(Module):
    ''' управление окном '''

    def __init__(self, main):
        super().__init__(main)
        log_info('Window modules is being creating')
        self.app = None
        self.clock = None
        self.dt = float(0)
        log_info('Window modules has created')

    def setup(self, data):
        log_info('Window modules is on setup')
        self.app = pg.display.set_mode((data.open_settings['width'], data.open_settings['height']))
        self.clock = pg.time.Clock()
        self.fps = data.open_settings['fps_limit']
        self.time = 0
        log_info('Window modules setup if finish')

    def update_window(self):
        self.time += 0.0083
        pg.display.update()
        self.clock.tick(self.main.settings.open_settings['fps_limit'])
        self.app.fill('black')

