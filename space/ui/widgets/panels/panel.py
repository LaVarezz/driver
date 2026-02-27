
from space.settings.protocols.protocols import MainLike
import pygame as pg

class Panel:
    def __init__(self, cords, size, main:MainLike, alpha=256, parent=None):
        self.x, self.y = cords
        self.width, self.height = size
        self.main = main
        self.alpha = alpha
        self.surface = pg.surface.Surface((self.width, self.height), pg.SRCALPHA) if self.alpha != 256 else pg.surface.Surface((self.width, self.height))
        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)
        self.surface.set_alpha(self.alpha) if self.alpha != 256 else None
        self.UI = self.main.manager.widgets

        self.parent = parent
        self.widgets = []
        self.dead_count = self.alpha

    def update(self):
        pass

    def draw(self, window):
        self.surface.fill("yellow")
        print(len(self.widgets))
        for widget in self.widgets:
            self.surface.blit(widget.surface, widget.rect)
        window.blit(self.surface, self.rect)



    def get_position(self):
        return self.x, self.y

    def get_size(self):
        return self.width, self.height

    def __repr__(self):
        return 'Panel'
