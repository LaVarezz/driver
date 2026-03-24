from xml.sax import parse

from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes
from project.engine.managers.scene_manager.scenes.battle_scene.map.tile import BattleMapTile
from project.engine.managers.text_manager.text_manager import event
from project.engine.managers.widget_manager.widgets.panel.panel import Panel
from project.engine.utills.logging.log import log_info


class BattleMap:
    def __init__(self, main: MainLike, map_size: tuple[int, int], tile_size: int, battle_map_outpost: tuple[int, int]):
        '''
        Класс игровой карты. Хранит тайлы в двумерном списке.
        hovered - наведенная клетка
        captured - захваченная клетка
        '''

        self.main = main
        x, y = map_size
        self.tiles = [[[] for _ in range(y)] for _ in range(x)]
        self.tile_size = tile_size

        self.hovered = None
        self.captured = None

        self.main.events.subscribe(self, EventTypes.BUTTONCHANGE)



        for x1 in range(x):
            for y1 in range(y):
                self.tiles[x1][y1] = BattleMapTile(main=self.main, cords=(x1, y1), tile_size=tile_size,
                                                   battle_map_outpost=battle_map_outpost)
        log_info(f'Battle map {x} x {y} has created')

    def collide_tiles(self) -> object:
        camera_x, camera_y = 0, 0  # Work piece
        tile_size = self.tile_size  # Work piece for the moment when tile size can be changed
        ox, oy = self.main.settings.game_settings["battle_map_outpost"]
        ox //= 2
        oy //= 2
        x, y = self.main.cursor.get_mouse_states()[:2]

        map_size_x, map_size_y = self.main.settings.game_settings["battle_map_size"]

        if ox < x < map_size_x * tile_size + ox:
            if oy < y < map_size_y * tile_size + oy:
                # here we are shore that the cursor is on the map
                x -= ox
                y -= oy

                dx = x // tile_size
                dy = y // tile_size
                return self.tiles[dx][dy]
        return None

    def click_process(self, pos):
        x, y = pos


    def update(self):
        self.hovered = self.collide_tiles()


    def draw(self, window):
        for line in self.tiles:
            for tile in line:
                tile.draw(window)

    def __repr__(self):
        return 'Battle map object'
