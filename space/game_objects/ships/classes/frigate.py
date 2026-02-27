from space.game_objects.ships.ship import ShipMethods


class Frigate(ShipMethods):
    def __init__(self, cords, side, parameters):
        super().__init__(cords, side, parameters)
        self.width, self.height = 1, 1


