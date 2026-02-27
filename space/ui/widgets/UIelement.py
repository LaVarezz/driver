import pygame as pg

from space.settings.protocols.protocols import MainLike


class UIelement:
    def __init__(self, cords, size, main: MainLike, parent=None, center=(False, False), alpha=None, font=None):
        self.width, self.height = size
        self.main = main
        self.parent = parent
        self.alpha = alpha

        if not any(center):
            self.absolute_x, self.absolute_y = cords
            self.rect = pg.rect.Rect(self.absolute_x, self.absolute_y, self.width, self.height)

        else:
            into = [center[0], center[1]]
            if not center[0]:
                into[0] = cords[0]
            if not center[1]:
                into[1] = cords[1]

            self.centring(into)

        if self.parent:
            if self not in self.parent.widgets:
                self.parent.widgets.append(self)

        if self.alpha:
            self.surface = pg.surface.Surface((self.width, self.height))
            self.surface.set_alpha(self.alpha)
        else:
            self.surface = pg.surface.Surface((self.width, self.height), pg.SRCALPHA)

        self.visible = True
        self.enabled = True
        self.activated = False

    def update(self):
        pass

    def draw(self, window):
        if self.visible:
            window.blit(self.surface, self.rect)

    def check_collide(self, pos):
        if self.enabled:
            x = pos[0]
            y = pos[1]
            px, py = self.parent.get_position() if self.parent else (0, 0)
            if self.parent:
                px = self.parent.x
                py = self.parent.y
            if self.absolute_x + px < x < self.absolute_x + px + self.width:
                if self.absolute_y + py < y < self.absolute_y + py + self.height:
                    return True
        return False

    def centring(self, cords=(False, False)):
        ''' На вход подается кортеж из чисел и\или булевых выражений. В зависимости от входа, изменяются координаты точки входа '''
        lines = [0, 1]
        need_to_center = []
        if cords[0] and isinstance(cords[0], bool):
            need_to_center.append((0, 1)) if self.parent else need_to_center.append((0, 0))

        if cords[1] and isinstance(cords[1], bool):
            need_to_center.append((1, 1)) if self.parent else need_to_center.append((1, 0))

        for line in need_to_center:
            if line[0] in lines:
                lines.remove(line[0])

        for line in lines:
            if not line:
                self.absolute_x = cords[0]

            else:
                self.absolute_y = cords[1]

        for line in need_to_center:
            if not line[0]:
                if line[1]:
                    px = self.parent.get_size()[0]
                    self.absolute_x = px / 2 - self.width / 2
                else:
                    self.absolute_x = self.main.ws.WIDTH / 2 - self.width / 2
            else:
                if line[1]:
                    py = self.parent.get_size()[1]
                    self.absolute_y = py / 2 - self.height / 2
                else:
                    self.absolute_y = self.main.ws.HEIGHT / 2 - self.height / 2
        self.rect = pg.rect.Rect(self.absolute_x, self.absolute_y, self.width, self.height)

    def handle_event(self, game, pos):
        pass
