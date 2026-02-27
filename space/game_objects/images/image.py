import pygame as pg

from space.settings.protocols.protocols import MainLike


class Image:
    def __init__(self, cords, size, main: MainLike, layer, image=None, panel=None):
        self.main = main
        self.image = image
        self.size = size
        self.cords = cords

        self.surface = pg.surface.Surface(self.size)
        self.main.manager.images.add_image(self, layer)

    def update(self):
        pass

    def draw(self, surface):
        surface.blit(self.surface, self.cords)

    def __repr__(self):
        return 'image'