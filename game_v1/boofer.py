
from random import randrange, gauss
from tools import tan_counter
import pygame as pg
def create_effect(start_coordinates, finish_coordinates,  parent, game, static_picture, moveable_picture, images, effect_type, speed=0.1, scale=1, double=False):
    x_pos_start = game.fields[start_coordinates[0]][start_coordinates[1]].rect.center[0]
    y_pos_start = game.fields[start_coordinates[0]][start_coordinates[1]].rect.center[1]

    x_pos_finish = game.fields[finish_coordinates[0]][finish_coordinates[1]].rect.center[0]
    y_pos_finish = game.fields[finish_coordinates[0]][finish_coordinates[1]].rect.center[1]

    start_coordinates = (x_pos_start, y_pos_start)
    finish_coordinates = (x_pos_finish, y_pos_finish)
    if effect_type == 'Avatar':
        AvatarGoTO(game, game.mover_person.avatar, start_coordinates, finish_coordinates)
        AvatarGoTO(game, game.mover_person.avatar, start_coordinates, finish_coordinates, True)
    else:
        Animation(start_coordinates, finish_coordinates,  parent, game, static_picture, moveable_picture, images, effect_type, speed, scale, double)

class Animation:
    def __init__(self, start_coordinates, finish_coordinates,  parent, game, static_picture, moveable_picture, images, effect_type, speed, scale, double):
        self.parent = parent
        self.game = game
        self.effect_type = effect_type

        self.frame = 0
        self.speed = speed
        self.start_x, self.start_y = start_coordinates[0], start_coordinates[1]
        self.finish_x, self.finish_y = finish_coordinates[0], finish_coordinates[1]
        if self.effect_type == 'Blink':
            self.start_y-=10
        if self.effect_type == 'Tree':
            self.start_y-=25
        if self.effect_type == 'Firewall':
            self.start_y-=20

        self.x, self.y = self.start_x, self.start_y


        self.scale = scale
        self.static = static_picture
        self.moveable = moveable_picture

        self.double = double
        self.double_created = double

        self.images = images
        self.game.effects.append(self)

        if self.moveable:
            if self.effect_type in ('Slash'):
                self.rotation = tan_counter(self.finish_x - self.x, self.y - self.finish_y)
            else:
                self.rotation = 180 + tan_counter(self.finish_x - self.x, self.y - self.finish_y)

        if self.static:
            self.field = game.fields[((self.x - 250) // game.size)][((self.y - 50) // game.size)]

            if self.effect_type == 'Firewall':
                self.time = 3
            if self.effect_type in ['Rock', 'Tree']:
                self.time = -1
            if self.static == 2:
                self.images = [self.images[randrange(0, len(self.images))]]

    def update(self):
        self.frame += self.speed
        if not self.static:
             if self.frame >= len(self.images):
                 self.game.effects.remove(self)
                 self.frame-=self.speed
             if self.moveable:
                 self.x += (self.finish_x - self.x) * 0.2
                 self.y += (self.finish_y - self.y) * 0.2

             if self.double:
                 if self.double_created:
                     if round(self.frame) == 6:
                         self.double_created = False
                         self.parent.movement(self.game, self.parent.x, self.game.pressed_field.x, self.parent.y, self.game.pressed_field.y,
                                          paranormal_movement=True)
                         self.parent.can_draw_avatar = False
                         self.game.end_of_turn(person=self.parent)
                         create_effect((self.parent.x, self.parent.y), (self.parent.x, self.parent.y), self.parent, self.game,
                                       False, False, self.game.blinks, 'Blink', 0.2, 2.5)
                 if round(self.frame >= 15):
                     self.parent.can_draw_avatar = True
        else:
            if self.frame >= len(self.images):
                self.frame = 0

            if self.game.removed_effects:
                for effect in self.game.removed_effects:
                    if effect[0] == self.field.x and effect[1] == self.field.y:
                        if self in self.game.effects:
                            self.game.effects.remove(self)
                        if effect in self.game.removed_effects:
                            self.game.removed_effects.remove(effect)
                        self.game.fields[self.parent.x][self.parent.y].object = None

    def draw(self):
        image = self.images[int(self.frame)]
        if self.effect_type in ['Rock', 'Tree']:
            if self.effect_type == 'Rock':
                image = pg.transform.scale(image, (self.game.size-5, self.game.size-5))
            elif self.effect_type == 'Tree':
                image = pg.transform.scale(image, (self.game.size+10, self.game.size+40))

        else: image = pg.transform.scale_by(image, self.scale)

        if self.moveable:
            image = pg.transform.rotate(image, self.rotation)

        rect = image.get_rect(center=(self.x, self.y))
        self.game.window.blit(image, rect)

    def __repr__(self):
        return f'{self.effect_type}, {self.x, self.y}'


class AvatarGoTO:
    def __init__(self, game, avatar, start, finish, bar=False):
        self.game = game
        self.parent = game.mover_person
        self.image = avatar
        self.x = start[0]
        self.y = start[1]
        self.start_x = game.mover_person.x
        self.start_y = game.mover_person.y
        self.stx = game.mover_person.x
        self.sty = game.mover_person.y
        self.e_x = finish[0]
        self.e_y = finish[1]-13

        self.effect_type = 'Avatar'
        self.time = 0
        self.bar = bar
        self.game.effects.append(self)
        self.parent.can_draw_avatar = False

    def update(self):
        self.time += 0.2
        self.x += (self.e_x-self.x)*0.1
        self.y += (self.e_y-self.y)*0.1
        if round(self.x) == self.e_x and round(self.y) == self.e_y and self.time != 0:
            self.parent.can_draw_avatar = True
    def draw(self):
        x = round(self.x) - 90
        y = round(self.y)
        size = self.game.size
        if not self.bar:
            if self.parent.cls == 'Warrior':
                image = pg.transform.scale(self.image[0], (self.game.size+35, self.game.size+35))
            elif self.parent.cls == 'Necromancer':
                image = pg.transform.scale(self.image[0], (self.game.size-30, self.game.size-30))
            elif self.parent.cls == 'Necropet':
                image = pg.transform.scale(self.image[0], (self.game.size-50, self.game.size-50))
            elif self.parent.cls == 'Mage':
                image = pg.transform.scale(self.image[0], (self.game.size-10, self.game.size-10))
            elif self.parent.cls == 'Rogue':
                image = pg.transform.scale(self.image[0], (self.game.size-10, self.game.size-10))
            else:
                image = pg.transform.scale(self.image[0], (self.game.size-10, self.game.size-10))
            if not self.parent.can_be_attacked:
                image.set_alpha(60)
            else:
                image.set_alpha(self.parent.image.get_alpha())

            rect = image.get_rect(center=(self.x, self.y))
            tan_counter((self.e_x - self.x), self.y - self.e_y)
            self.game.window.blit(image, rect)
        else:
            if self.parent.health[0] <= 0:
                self.parent.health[0] = 1
            var = 200
            rect_bar_full = pg.Surface((size // 5 * 4 + 4, size // 4 + 4))
            rect_bar_full.fill('black')
            rect_bar_full.set_alpha(var)

            rect_health_bar = pg.Surface((int((size // 5 * 4) * self.parent.health[0] // self.parent.health[1]), size // 8))
            rect_health_bar.fill('red')
            rect_health_bar.set_alpha(var)
            rect_bar_full.blit(rect_health_bar, (2, 2))

            rect_mana_bar = pg.Surface((int((size // 5 * 4) * self.parent.mana[0] // self.parent.mana[1]), size // 8))
            rect_mana_bar.fill('blue')
            rect_mana_bar.set_alpha(var)
            rect_bar_full.blit(rect_mana_bar, (2, size // 8+2))

            rect = rect_bar_full.get_rect(center=(x+size, y+size//20*11+5))

            self.game.window.blit(rect_bar_full, rect)
