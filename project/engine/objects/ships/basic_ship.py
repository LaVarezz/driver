class BasicShip:
    def __init__(self, main, cords):
        self.main = main
        self.grid_x, self.grid_y = cords # position on the battle map(x, y - intengers).

        self.rect = None
        self.surface = None

        self.side: int # lol it is a side, nothing more :]


    def update(self):
        pass

    def draw(self, window):
        window.blit(self.surface, self.rect)