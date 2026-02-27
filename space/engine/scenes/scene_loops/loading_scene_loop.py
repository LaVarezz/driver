import pygame as pg

from space.engine.debug.logs.main_log import log_info, log_warning
from space.resourses.cache.text_cache import TextCache
from space.scripts.utils.exit import exit_game
from space.settings.protocols.protocols import SceneLike
from space.settings.settings.main_settings.env import Env


class Loading(SceneLike):
    def __init__(self, main, scene, config):
        self.main = main
        self.scene = scene
        self.frame_count = 0

        self.max_frame_count = 0

        self.sx, self.sy = 300, 30
        self.surf = pg.surface.Surface((self.sx, self.sy))
        self.text_cache = TextCache()
        self.config = config

    @property
    def process(self):
        ratio = min(self.frame_count / self.max_frame_count, 1)
        return ratio * self.sx

    def mainloop(self):
        log_info('Инициирована загрузка ресурсов.')
        try:
            self.config(self)
        except Exception as s:
            log_warning(f'Ошибка пути! {s}')
            raise s
        log_info('Загрузка ресурсов успешна.')

    def draw_update_interface(self, lite=False, done=False):
        self.surf.fill('black')
        if not lite:
            self.frame_count += 1
        else:
            self.frame_count += 0.1
        self.text_cache.render_text(f'Загрузка ресурсов{'.' * (round(self.frame_count) % 160 // 40)}').draw(
            self.main.window, (Env.screen_size[0] // 2 - 70, Env.screen_size[1] - 130))
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit_game(self.main)

        rect = (5, 5, self.process, self.sy - 10)
        pg.draw.rect(self.surf, 'white', rect)
        self.main.window.blit(self.surf, (Env.screen_size[0] // 2 - self.sx // 2, Env.screen_size[1] - 100))
        if done:
            self.frame_count = self.max_frame_count

        pg.event.pump()
        pg.display.update()
