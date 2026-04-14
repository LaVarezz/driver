from random import randrange

from pygame import Surface, Rect

from project.data.protocols.protocols import MainLike
from project.engine.modules.game_modules.scene_module.scenes.BattleScene.ship_controller.ship_types import \
    ship_types


class ShipController:
    ''' Контроллер управляет кораблями и боевой очередью. '''

    def __init__(self, main: MainLike):
        self.main = main

        self.queue = []
        self.out_of_queue = []
        self.ships_list = {}
        self.battle_scene = self.main.modules.scene_module.current_scene

    def create_new_ship(self, cords, type, side):
        def generate_id():
            id = ''
            for i in range(8):
                id += str(randrange(0, 10))
            return id

        ship = ship_types[type](self.main, cords)
        data = self.main.camera.get_battle_map_configuration()
        tile_size = self.battle_scene.tile_size
        x, y = cords
        top = y * tile_size + data['map_outpost'][1]//2
        left = x * tile_size + data['map_outpost'][0]//2

        ''' Присвоение параметров '''
        ship.surface = Surface((tile_size, tile_size))
        ship.rect = Rect(left, top, tile_size, tile_size)
        ship.id = generate_id()

        ship.side = side

        self.queue.append(ship.id)

        ship.surface.fill('blue')

        self.ships_list[ship.id] = ship

    def update(self):
        for id in self.ships_list.keys():
            self.get_ship(id).update()

    def draw(self):
        for id in self.ships_list.keys():
            self.get_ship(id).draw(self.main.modules.window_module.app)

    def get_ship(self, id):
        return self.ships_list[id]

    def remove_ship(self):
        pass

    def __repr__(self):
        return 'Ship controller'
