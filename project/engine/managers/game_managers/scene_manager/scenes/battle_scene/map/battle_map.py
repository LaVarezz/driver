from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes
from project.engine.managers.game_managers.scene_manager.scenes.battle_scene.map.tile import BattleMapTile
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

        self.ox, self.oy = self.main.settings.game_settings["battle_map_outpost"]
        self.tiles = [[[] for _ in range(y)] for _ in range(x)]
        self.tile_size = tile_size

        self.hovered = None
        self.captured = None

        self.main.events.subscribe(self, EventTypes.BUTTONCHANGE)
        self.main.events.subscribe(self, EventTypes.GETBATTLEMAPCONFIGURATION, 1)

        for x1 in range(x):
            for y1 in range(y):
                self.tiles[x1][y1] = BattleMapTile(main=self.main, cords=(x1, y1), tile_size=tile_size,
                                                   battle_map_outpost=battle_map_outpost)
        log_info(f'Battle map {x} x {y} has created')

    def collide_tiles(self, cords=None) -> object:
        camera_x, camera_y = 0, 0  # Work piece
        tile_size = self.tile_size  # Work piece for the moment when tile size can be changed
        self.ox //= 2
        self.oy //= 2
        if not cords:
            cords = self.main.cursor.get_mouse_states()[:2]
        x, y = cords

        map_size_x, map_size_y = self.main.settings.game_settings["battle_map_size"]

        if self.ox < x < map_size_x * tile_size + self.ox:
            if self.oy < y < map_size_y * tile_size + self.oy:
                # here we are shore that the cursor is on the map
                x -= self.ox
                y -= self.oy

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

    def trigger(self, msg, data):
        if msg == EventTypes.BUTTONCHANGE:
            ''' Триггерит наведенный тайл '''
            but = data['buttons']
            if (0, 1) in but:
                self.captured = self.hovered
                if self.captured:
                    return True
            if (0, 0) in but:
                if self.captured and self.captured == self.hovered:
                    self.captured.process()
                    self.captured = None

                    return True
                self.captured = None

        if msg == EventTypes.GETBATTLEMAPCONFIGURATION:
            ''' Возвращает свою часть данных, касающуюся игровой карты. Далее событие ловит camera '''
            data["tile_size"] = self.tile_size
            data["map_outpost"] = (self.ox, self.oy)
            return

    def __repr__(self):
        return 'Battle map object'
