import pygame as pg
from random import randrange

class BasicWidget:
    def __init__(self, main, cords, size, visible=True, enabled=True):
        self.main = main
        self.x, self.y = cords
        self.width, self.height = size
        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)
        self.surface = pg.surface.Surface((self.width, self.height))
        self.surface.fill('red')
        self.visible = visible
        self.enabled = enabled
        self.create_id()

    def update(self):
        pass

    def draw(self, window):
        if self.visible:
            window.blit(self.surface, self.rect)

    def create_id(self):
        self.id = ''
        for i in range(10):
            self.id += str(randrange(0, 10))

    def check_collide(self, px, py):
        if self.rect.collidepoint(px, py):
            return True
        return False
