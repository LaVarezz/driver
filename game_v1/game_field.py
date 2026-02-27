
import pygame as pg
from pygame import Surface

from StatusEffect import StatusEffect
from effects_animation import create_effect

'''класс игрового поля'''
class Field:
    def __init__(self, x, y, size, game, color='Gray', ):
        self.x = x+1
        self.y = y+1
        self.color = color
        self.size = size
        self.rect = pg.rect.Rect(250+x*size+size, 50+y*size+size, size, size)
        self.status = None
        self.object = None
        self.img = game.grasses[0]
        self.img = pg.transform.scale(self.img, (self.size-2, self.size-2))

        self.board_color = (33, 70, 33)

    def draw(self, window, font, game_object):
        size = self.size
        x = self.x
        y = self.y

        rect = self.img.get_rect(center=(250+self.x*size+size//2, 50+self.y*size+size//2))
        pg.draw.rect(window, self.board_color, self.rect, 2)
        window.blit(self.img, rect)

        if self.status:
            if self.status.can_draw_avatar:
                var = 200
                rect_bar_full = Surface((size//5*4+4, size//4 + 4))
                rect_bar_full.fill('black')
                rect_bar_full.set_alpha(var)

                rect_health_bar = Surface((int((size//5*4)*self.status.health[0]//self.status.health[1]), size//8))
                rect_health_bar.fill('red')
                rect_health_bar.set_alpha(var)
                rect_bar_full.blit(rect_health_bar, (2, 2))
                rect_mana_bar = Surface((int((size//5*4)*self.status.mana[0]//self.status.mana[1]), size//8))
                rect_mana_bar.fill('blue')
                rect_mana_bar.set_alpha(var)
                rect_bar_full.blit(rect_mana_bar, (2, size//8+2))

                window.blit(rect_bar_full, (250 + x * size + size // 10, 50 + y * size + size // 20 * 17))

                if self.status.shield:
                    rect_shield_bar = pg.rect.Rect(250 + x * size + size // 10+2, 50 + y * size + size // 20 * 17+2,
                                                   int((size // 5 * 4) * self.status.shield // self.status.health[1]),
                                                   size // 8)
                    pg.draw.rect(window, 'Gray', rect_shield_bar)


        if game_object.test_mode:
            text = font.render(f'{self.x}{self.y}', 1, 'white')
            window.blit(text, self.rect)

    def __repr__(self):
        return f'field ({self.x} {self.y})'

class Object:
    def __init__(self, x, y, type, fields, game, time=-1):
        self.x = x
        self.y = y
        self.type = type
        self.game = game
        self.time = time
        fields[x][y].object = self
        if self.type == 'Rock':
            create_effect((self.x, self.y), (self.x, self.y), self, self.game, 2,
                          False, self.game.rocks, 'Rock', 0, 0.5)
            self.can_stay = False
        if self.type == 'Firewall':
            create_effect((self.x, self.y), (self.x, self.y), self, self.game, True,
                          False, self.game.fires, 'Firewall', 0.2, 0.5)
            self.can_stay = True
        if self.type == 'Tree':
            create_effect((self.x, self.y), (self.x, self.y), self, self.game, 2,
                          False, self.game.trees, 'Tree', 0, 0)
            self.can_stay = False

        game.objects.append(self)

    def draw(self):
        if self.type == 'Rock':
            pass
        if self.type == 'Fire':
            pass

    def update(self):
        game = self.game
        time = self.time
        if time > 0:
            self.time -= 1
        if not self.time:
            self.game.objects.remove(self)
            game.removed_effects.append((self.x, self.y))

    def check_contact(self):
        if self.type == 'Rock':
            for i in self.game.creatures:
                for creature in i:
                    if abs(creature.x - self.x) <= 1:
                        if abs(creature.y - self.y) <= 1:
                            StatusEffect(creature, 'Avoidance', 1, creature.avoidance, 20, 'rock_effect')

        if self.type == 'Firewall':
            if self.game.fields[self.x][self.y].status:
                StatusEffect(self.game.fields[self.x][self.y].status, 'Fire', 2, self.game.fields[self.x][self.y].status.health[0], 100, 'fireplace', True)



    def __repr__(self):
        return f'{self.type} {self.x} {self.y}'
