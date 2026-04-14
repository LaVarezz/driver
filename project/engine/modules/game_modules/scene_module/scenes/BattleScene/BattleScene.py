from project.data.protocols.protocols import MainLike
from project.engine.modules.game_modules.scene_module.scenes.BattleScene.map.battle_map import BattleMap
from project.engine.modules.game_modules.scene_module.scenes.BattleScene.ship_controller.ship_controller import \
    ShipController
from project.engine.scripts.utils.no_use_utils.tile_size_counter import count_tile_size
from project.engine.utills.logging.log import log_info


class BattleScene():
    def __init__(self, main: MainLike):
        log_info('Battle map create: start')
        self.main = main
        self.name = 'battle_scene'

        settings = self.main.settings
        ''' "Стандарт" размера игрового объекта. На него должны ориентироваться клетки игрового поля, корабли, астероиды и прочие злые штуки.'''
        self.tile_size = count_tile_size((settings.open_settings['width'], settings.open_settings['height']), \
                                         settings.game_settings['battle_map_size'],
                                         settings.game_settings['battle_map_outpost'])

        self.battle_map = BattleMap(main=self.main, map_size=self.main.settings.game_settings['battle_map_size'],
                                    tile_size=self.tile_size,
                                    battle_map_outpost=settings.game_settings['battle_map_outpost'])

        log_info('Battle map create: finish')

    def setup(self):
        self.ship_controller = ShipController(self.main)

        # test
        self.ship_controller.create_new_ship((1, 1), 'basic_ship', 0)
        self.ship_controller.create_new_ship((5, 1), 'basic_ship', 1)

    def update(self):
        self.battle_map.update()
        self.ship_controller.update()

    def draw(self):
        self.battle_map.draw(self.main.modules.window_module.app)
        self.ship_controller.draw()

    def kill_scene(self):
        pass

    def __repr__(self):
        return 'BATTLE SCENE'
