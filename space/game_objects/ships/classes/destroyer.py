from space.game_objects.ships.ship import ShipMethods


class Destroyer(ShipMethods):
    def __init__(self, cords, side, parameters):
        super().__init__(cords, side, parameters)
        self.width, self.height = 2, 1
