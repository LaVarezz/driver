import pygame as pg

from space.engine.contollers.binds.battle.battlestate_binds import binds
from space.settings.protocols.protocols import SceneLike


def event_handler(self: SceneLike):
    self.main.mouse_state = pg.mouse.get_pressed()
    self.main.mouse_pos = pg.mouse.get_pos()

    ''' Мышь '''
    if any(self.main.mouse_state):

        handler = self.main.binds.get(pg.K_RSHIFT)
        if handler:
            handler(self)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            self.main.scene.running = False
            self.main.quit_game = True

        if event.type == pg.MOUSEBUTTONDOWN:
            handler = self.main.binds.get(pg.MOUSEBUTTONDOWN)
            if handler:
                handler(self)



        elif event.type == pg.MOUSEWHEEL:
            if not self.main.manager.overlay.check_pause():
                if self.main.binds == binds:
                    py = event.y
                    if py == -1 and self.main.manager.camera.zoom >= 0.4:
                        self.main.manager.camera.zoom -= 0.2
                    elif py == 1 and self.main.manager.camera.zoom <= 1.8:
                        self.main.manager.camera.zoom += 0.2

        ''' Клавиши '''
        if event.type == pg.KEYDOWN:
            handler = self.main.binds.get(event.key)
            if handler:
                handler(self)

        if event.type == pg.MOUSEBUTTONUP:
            handler = self.main.binds.get(pg.MOUSEBUTTONUP)
            if handler:
                handler(self)
    self.main.mouse_old_pos = self.main.mouse_pos
