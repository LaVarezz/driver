from pygame import Surface


class BasicShip:
    def __init__(self, main, cords):
        self.main = main
        self.grid_x, self.grid_y = cords

        self.rect = None
        self.surface = None

    def update(self):
        pass

    def draw(self, window):
        window.blit(self.surface, self.rect)