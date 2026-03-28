import pygame as pg

from project.data.protocols.protocols import MainLike


class BasicWidget:
    def __init__(self, main: MainLike, cords, size, id, layer, panel, anchor, offset, moveable, visible=True,
                 enabled=True):
        self.main = main
        self.x, self.y = cords
        self.width, self.height = size
        self.id = id
        self.rect = None
        self.surface = pg.surface.Surface((self.width, self.height))
        self.panel = panel

        self.anchor = anchor
        self.layer = layer
        self.offset = offset

        self.visible = visible
        self.enabled = enabled
        self.moveable = moveable

        self.process_place()

    def process_place(self):
        if not self.panel:
            ''' в таком случае в роли поверхности выступает окно '''
            app_width = self.main.settings.open_settings['width']
            app_height = self.main.settings.open_settings['height']
        else:
            p = self.main.manager.widget_manager.get_widget(self.panel)
            app_width = p.width
            app_height = p.height
        if self.anchor:
            ox, oy = self.offset
            if 'CENTER' in self.anchor:
                self.x = app_width//2-self.width//2+ox
                self.y = app_height//2-self.height//2+oy
            if 'TOP' in self.anchor:
                self.y = min(app_height - self.height, max(oy, 0))
            if 'BOTTOM' in self.anchor:
                self.y = min(app_height - self.height, max(app_height - oy - self.height, 0))
            if 'LEFT' in self.anchor:
                self.x = min(app_width - self.width, max(ox, 0))
            if 'RIGHT' in self.anchor:
                self.x = min(app_width - self.width, max(app_width - ox - self.width, 0))

        self.rect = pg.rect.Rect(self.x, self.y, self.width, self.height)

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
