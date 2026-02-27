import pygame as pg

from space.engine.managers.managers.core.object_manager import Object
from space.scripts.control.trigger import cell_trigger

from space.settings.constants.battle_constants import Types

from space.settings.protocols.protocols import CellLike
from space.ui.debug.debug_render import debug_cell_update, debug_cell_draw


class Cell(CellLike, Object):
    __slots__ = ('x', 'y', 'game', 'content', 'window', 'cell_size', 'kx', 'ky', 'font')

    def __init__(self, cords, game):
        Object.__init__(self, cords, Types.CELL)
        pg.init()
        self.game = game

        self.content = None
        self.window = self.game.main.window
        self.cell_size = self.game.bs.field_size

        self.kx, self.ky = 0, 0

        self.font = self.game.main.ws.GLOBAL_TEXT_CACHE['little']

        self.game.has_camera_changed = True
        self.update_cell_visual()

    @property
    def absolute_x(self):
        return self.game.bs.padx + self.x * self.game.bs.field_size * self.game.main.manager.camera.zoom

    @property
    def absolute_y(self):
        return self.game.bs.pady + self.y * self.game.bs.field_size * self.game.main.manager.camera.zoom

    @property
    def screen_x(self):
        if self.game.has_camera_changed:
            self._screen_x = (
                                     self.x * self.cell_size - self.game.main.manager.camera.camera_x) * self.game.main.manager.camera.zoom + self.game.bs.padx
        return self._screen_x

    @property
    def screen_y(self):
        if self.game.has_camera_changed:
            self._screen_y = (self.y * self.cell_size - self.game.main.manager.camera.camera_y) * self.game.main.manager.camera.zoom + self.game.bs.pady
        return self._screen_y

    @property
    def size(self):
        if self.game.has_camera_changed:
            self._size = self.cell_size * self.game.main.manager.camera.zoom
        return self._size

    def update_cell_visual(self):
        self.rect = pg.rect.Rect(self.screen_x, self.screen_y, self.size, self.size)
        self.surface = pg.Surface((self.size, self.size))
        self.surface.set_alpha(128)

    def update(self):
        if self.game.has_camera_changed:
            self.update_cell_visual()
        if self.game.main.test_mode:
            debug_cell_update(self)

    def draw(self):

        self.surface.fill('gray')
        self.window.blit(self.surface, self.rect)
        pg.draw.rect(self.window, 'red', self.rect, 1)
        if self.game.main.test_mode.show_debug_ui:
            debug_cell_draw(self)

    def get_cords(self):
        return self.x, self.y

    def get_collide(self, pos):
        size = self.game.bs.field_size * self.game.main.manager.camera.zoom
        px = round(
            self.game.bs.padx - self.game.main.manager.camera.camera_x * self.game.main.manager.camera.zoom) - self.game.bs.padx
        py = round(
            self.game.bs.pady - self.game.main.manager.camera.camera_y * self.game.main.manager.camera.zoom) - self.game.bs.pady
        return self.absolute_x < pos[0] - px < self.absolute_x + size and self.absolute_y < pos[
            1] - py < self.absolute_y + size

    def trigger(self, type):
        cell_trigger(self, type)

    def __repr__(self):
        return f'Cell {self.x, self.y}'
