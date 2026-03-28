from pygame import Surface, Rect


class BasicShip:
    def __init__(self, main, cords, tile_size):
        self.main = main

        self.grid_x, self.grid_y = cords

        self.tile_size = tile_size

        self.surface = Surface((tile_size, tile_size))
        self.rect = Rect()


    def update(self):
        pass

    def draw(self, window):
        pass
