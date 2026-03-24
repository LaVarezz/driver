from pygame import surface, rect, draw

from project.engine.managers.widget_manager.widgets.buttons.button import Button


class BattleMapTile:
    ''' Объект игровой клетки
    content - Obj | None - игровой объект, находящийся на клетке
    button - связующее звено между ячейкой карты и курсором.
    '''

    def __init__(self, main,  cords, tile_size, battle_map_outpost):
        self.content = None
        self.main = main


        self._x, self._y = cords
        self._tile_size = tile_size
        self._ox, self._oy = battle_map_outpost
        self._surface = surface.Surface((tile_size, tile_size))

        self._rect = rect.Rect(self._ox//2 + self._x * self._tile_size, self._oy//2 + self._y * self._tile_size, self._tile_size,
                               self._tile_size)
        self._surface.fill('red')


    def update(self):
        pass

    def draw(self, window):
        window.blit(self._surface, self._rect)
        draw.rect(window, 'blue', self._rect, width=3)

    def __repr__(self):
        return f"tile {self._x} x {self._y}"