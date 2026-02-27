from random import randrange

import pygame as pg
from space.engine.debug.logs.main_log import log_error
from space.settings.settings.battle_settings.env import Env


class Animation:
    def __init__(self, object, main, scalable=True):
        self.time = 30 // Env.animation_speed
        self.current_time = randrange(0, int(self.time))
        self.object = object
        self.main = main
        self.scalable = scalable
        self.reload_pull()
        self.frames_len = len(self.frames_pool)
        self.current_frame_int = randrange(0, self.frames_len)
        self.current_frame = self.frames_pool[self.current_frame_int]

        self.err = False

    def set_object(self, object):
        self.object = object

    def update(self):
        pass

    def exchange_sipites(self, direction, alpha=256):
        self.reload_pull(direction, alpha)

    def update_sprite(self):
        if self.current_frame_int < self.frames_len - 1:
            self.current_frame_int += 1
            self.current_time = 0
        else:
            self.current_time = 0
            self.current_frame_int = 0

        self.current_frame = self.frames_pool[self.current_frame_int]

    def reload_pull(self, direction=False, alpha=256):
        ''' Обновляет пулл обьектов в записимости от того, скейлитеся ли обьект или нет. '''
        if self.scalable:
            if not isinstance(direction, int):
                self.frames_pool = [i for i in
                                    self.object.sprites[self.object.state][
                                        round(self.main.manager.camera.zoom, 2)]]
            else:
                self.frames_pool = [pg.transform.rotate(i, self.object.direction)
                                    for i in self.object.sprites[self.object.state]
                                    [round(self.main.manager.camera.zoom, 2)]]

            if self.frames_pool == []:
                log_error(f'Пулл спрайтов не загрузился. Состояние: {self.object.sprites}')
                raise Exception
        else:
            if isinstance(direction, bool):
                for i in self.object.sprites.values():
                    self.frames_pool = [j for j in i]
            else:
                self.frames_pool = []
                for i in self.object.sprites.values():
                    for j in i:
                        self.frames_pool.append(pg.transform.rotate(j, self.object.direction))

            if self.frames_pool == []:
                log_error(f'Пулл спрайтов не загрузился. Состояние: {self.object.sprites}')
                raise Exception
        if alpha != 256: [i.set_alpha(alpha) for i in self.frames_pool]

    def draw(self):
        if not hasattr(self.object, 'cords'):
            self.object.surface.blit(self.current_frame, (0, 0))
        else:
            self.object.surface.blit(self.current_frame, self.object.cords)
            ''' Для текущего ходящего корабля '''
        if hasattr(self.main.scene, 'game'):
            if self.object == self.main.scene.game.queue.current_mover:
                pg.draw.rect(self.object.surface, 'Green' if self.object.side == 0 else 'red', (15, 15, 8, 8))
