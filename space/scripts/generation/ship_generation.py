import dataclasses

from space.game_objects.ships.classes.destroyer import Destroyer
from space.game_objects.ships.classes.frigate import Frigate
from space.scripts.utils.battle_utils.place_ship_to_cords import place_ship_to_cords
from space.ui.animations.animation import Animation


def create_ship(side, self, load, parameters: dataclasses.dataclass, cords=None):
    if not cords:
        if self.side == 0:
            cords = [2, 2]
        elif self.side == 1:
            cords = [9, 8]

    if parameters.ship_tonnage == 'Фрегат':
        cls = Frigate
    elif parameters.ship_tonnage == 'Эсминец':
        cls = Destroyer
    ship = cls(cords, side, parameters)

    ''' Фаза присваивания внешних параметров '''
    ship.place = self.main.manager.objects.cells[ship.x][ship.y]
    ship.game = self
    ship.place.content = ship

    ship.sprites, ship.sprites_original = self.main.manager.downloader.download_ship('frigate', 'lm-1', self, load)

    eff = Animation(ship, self.main)
    self.main.manager.animation.add_effect(eff)
    ship.animation = eff

    self.main.manager.objects.add_object(ship)

    ''' Фаза размещения '''
    place_ship_to_cords(ship, cords, self, True)


    ''' Фаза добавления '''
