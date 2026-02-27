import pygame as pg

from space.resourses.cache.text_cache import TextObject, TextCache
from space.ui.widgets.UIelement import UIelement


class Button(UIelement):
    def __init__(self, cords, size, main, text=None, command=None, img=None, parent=None, center=(False, False), alpha=256, font=2):
        super().__init__(cords, size, main, parent=parent, center=center, alpha=alpha, font=font)

        self.triggered = False

        if text:
            self.font = text[1]
            self.text = str(text[0])
            self.rendered_text = self.font.render_text(self.text)
        else:
            self.text = ''
            self.font = pg.font.Font(None, 1)
            self.size = 1

        self.command = command
        self.img = img
        self.parent = parent

    def handle_event(self, game, pos):
        if self.enabled:
            self.triggered = True

    def process_command(self):
        if not self.activated:
            self.triggered = False
            if self.check_collide(self.main.mouse_pos):
                if self.command:
                    self.command(self.main)
                else:
                    print('No command!')

    def update(self):
        if self.triggered:
            self.process_command()

    def draw(self, window):
        if self.visible:
            if isinstance(self.rendered_text, TextObject) and isinstance(self.font, TextCache):
                px = self.width / 2 - self.font.get_size(self.text)[0] / 2
                py = self.height / 2 - self.font.get_size(self.text)[1] / 2
                self.rendered_text.draw(self.surface, (px, py))
            window.blit(self.surface, self.rect)

    def __repr__(self):
        return f'Button: {self.text}'
