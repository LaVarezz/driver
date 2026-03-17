from project.engine.managers.scene_manager.scenes.battle_scene.map.tile import BattleMapTile
from project.engine.utills.logging.log import log_info


class BattleMap:
    def __init__(self, map_size: tuple[int, int], tile_size: int, battle_map_outpost: tuple[int, int]):
        '''
        Класс игровой карты. Хранит тайлы в двумерном списке.
        '''

        x, y = map_size
        self.tiles = [[[] for _ in range(y)] for _ in range(x)]

        for x1 in range(x):
            for y1 in range(y):
                self.tiles[x1][y1] = BattleMapTile(cords=(x1, y1), tile_size=tile_size,
                                                   battle_map_outpost=battle_map_outpost)

        log_info(f'Battle map {x} x {y} has created')

    def update(self):
        pass

    def draw(self, window):
        for line in self.tiles:
            for tile in line:
                tile.draw(window)

    def __repr__(self):
        return 'Battle map object'
