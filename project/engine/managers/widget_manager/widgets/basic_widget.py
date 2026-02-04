import pygame as pg

class BasicWidget:
    def __init__(self, cords, size, visible=True, enabled=True):
        self.x, self.y = cords
        self.width, self.height = size
        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)
        self.surface = pg.surface.Surface((self.width, self.height))
        self.surface.fill('red')
        self.visible = visible
        self.enabled = enabled

    def update(self):
        pass

    def draw(self, window):
        if self.visible:
            window.blit(self.surface, self.rect)