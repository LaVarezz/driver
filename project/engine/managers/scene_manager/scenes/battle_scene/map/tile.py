from pygame import surface, rect


class BattleMapTile:
    ''' Объект игровой клетки
    content - Obj | None - игровой объект, находящийся на клетке
    '''

    def __init__(self, cords, tile_size, battle_map_outpost):
        self.content = None


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
