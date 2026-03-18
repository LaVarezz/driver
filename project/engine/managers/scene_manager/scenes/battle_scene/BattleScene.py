from project.data.protocols.protocols import MainLike
from project.engine.managers.scene_manager.scenes.battle_scene.map.battle_map import BattleMap
from project.engine.scripts.utils.no_use_utils.tile_size_counter import count_tile_size


class BattleScene():
    def __init__(self, main: MainLike):
        self.main = main
        self.name = 'battle_scene'

        settings = self.main.settings
        tile_size = count_tile_size((settings.open_settings['width'], settings.open_settings['height']), \
                                    settings.game_settings['battle_map_size'],
                                    settings.game_settings['battle_map_outpost'])
        self.battle_map = BattleMap(main=self.main, map_size=self.main.settings.game_settings['battle_map_size'], tile_size=tile_size,
                                    battle_map_outpost=settings.game_settings['battle_map_outpost'])

    def setup(self):
        pass

    def update(self):
        self.battle_map.update()

    def draw(self):
        self.battle_map.draw(self.main.manager.window_manager.app)

    def kill_scene(self):
        pass

    def __repr__(self):
        return 'BATTLE SCENE'
