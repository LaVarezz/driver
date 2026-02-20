import pygame as pg

class BasicWidget:
    def __init__(self, main, cords, size, id, moveable, visible=True, enabled=True):
        self.main = main
        self.x, self.y = cords
        self.width, self.height = size
        self.id = id
        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)
        self.surface = pg.surface.Surface((self.width, self.height))
        self.surface.fill('red')
        self.visible = visible
        self.enabled = enabled
        self.moveable = moveable

    def replace(self, px, py):
        if self.moveable:
            self.x += px
            self.y += py
            self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        pass

    def draw(self, window):
        if self.visible:
            window.blit(self.surface, self.rect)


    def check_collide(self, px, py):
        if self.rect.collidepoint(px, py):
            return True
        return False
