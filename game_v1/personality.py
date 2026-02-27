import random

import pygame as pg
from StatusEffect import StatusEffect
from game_field import Object

from tools import check_longth, possible_damage, possible_heal, status_effect_update
from effects_animation import create_effect
import Classes

class Person:
    def __init__(self, x, y, side, persons, fields, game_object, cls, health=None, summoner=None):
        self.side = side
        self.x = x
        self.y = y
        self.cls = cls

        self.first_skill_cd = 0
        self.second_skill_cd = 0
        self.third_skill_cd = 0
        self.avoidance = 0
        self.move_type = 0
        self.game_object = game_object
        self.shield = 0
        self.status_effects = []
        self.dots = []
        self.basic_dmg_cof = 1
        self.shield = 0
        self.reflect = 0
        self.stun = 0
        self.speed = 1
        self.can_draw_avatar = True
        self.can_be_attacked = True

        self.pet = []


        if cls == 'Warrior':
            self.health = [800, 800, 50]
            if game_object.test_mode: self.health = [700, 1000, 0]
            self.mana = [200, 200, 20]
            self.damage = 100
            self.defence = 30
            self.color = ['Purple', 'Orange'][self.side]
            self.range = 1
            self.avatar = [pg.image.load('sprites/warrior_avatar.png')]
            self.image = self.avatar
            self.reflect = 0.2
            self.image = pg.transform.scale(self.avatar[0], (game_object.size-15, game_object.size-15))
            self.image = pg.transform.flip(self.image, True, False)
            self.image.set_alpha(0)

        elif cls == 'Necromancer':
            self.health = [800, 800, 40]
            if game_object.test_mode: self.health = [600, 800, 0]
            self.mana = [200, 200, 20]
            self.damage = 80
            self.defence = 10
            self.color = ['Purple', 'Orange'][self.side]
            self.range = 4
            self.avatar = [pg.image.load('sprites/necro_avatar.png')]
            self.image = self.avatar
            self.image = pg.transform.scale(self.avatar[0], (game_object.size+40, game_object.size+40))
            self.image = pg.transform.flip(self.image, True, False)
            self.image.set_alpha(0)


        elif cls == 'Necropet':
            self.health = [150, 150, 0]
            if game_object.test_mode: self.health = [100, 200, 0]
            self.mana = [100, 200, 20]
            self.damage = 80
            self.defence = 30
            self.color = ['Purple', 'Orange'][self.side]
            self.range = 2
            self.avatar = [pg.image.load('sprites/Skeleton enemy.png')]
            self.activated = []
            self.image = pg.transform.scale(self.avatar[0], (game_object.size - 10, game_object.size - 10))
            self.image = pg.transform.flip(self.image, True, False)
            self.image.set_alpha(0)

        elif cls == 'Mage':
            self.health = [600, 600, 20]
            if game_object.test_mode: self.health = [800, 800, 0]
            self.mana = [100, 200, 20]
            self.damage = 100
            self.defence = 30
            self.color = ['Purple', 'Orange'][self.side]
            self.range = 4
            self.avatar = [pg.image.load('sprites/mage_avatar.png')]
            self.image = pg.transform.scale(self.avatar[0], (game_object.size - 10, game_object.size - 10))
            self.image.set_alpha(0)

        elif cls == 'Rogue':
            self.health = [800, 800, 50]
            if game_object.test_mode: self.health = [1000, 1000, 0]
            self.mana = [100, 200, 20]
            self.damage = 100
            self.defence = 30
            self.color = ['Purple', 'Orange'][self.side]
            self.range = 1
            self.avatar = [pg.image.load('sprites/rogue.png')]
            self.image = self.avatar
            self.reflect = 0
            self.image = pg.transform.scale(self.avatar[0], (game_object.size - 10, game_object.size - 10))
            self.image.set_alpha(0)

        elif self.cls == 'Hunterspet':
            self.health = [800, 800, 40]
            if game_object.test_mode: self.health = [600, 800, 0]
            self.mana = [200, 200, 20]
            self.damage = 80
            self.defence = 10
            self.color = ['Purple', 'Orange'][self.side]
            self.range = 4
            self.avatar = [pg.image.load('sprites/golem1.png')]
            self.image = self.avatar
            self.image = pg.transform.scale(self.avatar[0], (game_object.size+5, game_object.size+15))
            self.image = pg.transform.flip(self.image, True, False)
            self.image.set_alpha(0)
            self.game_object.summons.append(self)
            game_object.fields[self.x][self.y].status = self

        elif self.cls == 'Hunter':
            self.health = [800, 800, 40]
            if game_object.test_mode: self.health = [600, 800, 0]
            self.mana = [200, 200, 20]
            self.damage = 80
            self.defence = 10
            self.color = ['Purple', 'Orange'][self.side]
            self.range = 4
            self.avatar = [pg.image.load('sprites/Hunter1.png')]
            self.image = self.avatar
            self.image = pg.transform.scale(self.avatar[0], (game_object.size+5, game_object.size+15))
            self.image = pg.transform.flip(self.image, True, False)
            self.image.set_alpha(0)
            self.pet = [Classes.HuntersPet(self.x-1, self.y, 1, game_object.persons, game_object.fields, game_object, 'Hunterspet', summoner=True)]

        if not summoner:
            persons.append(self)
        self.game_object.didnt_move.append(self)
        fields[x][y].status = self
        self.is_creature = 0
        if summoner:
            self.is_creature = 2


    def draw(self, game):
        if self.can_draw_avatar:

            rect = self.image.get_rect(center=(self.x, self.y-10))
            game.window.blit(self.image, rect)

    def update(self, game):
        if self.can_draw_avatar:
            if not self.can_be_attacked:

                if self.image.get_alpha() > 60:
                    self.image.set_alpha(self.image.get_alpha()-5)
            else:
                if self.image.get_alpha() < 260:
                    self.image.set_alpha(self.image.get_alpha()+5)

            rect = self.image.get_rect(center=(self.x*game.size+250+game.size*0.5, self.y*game.size+55+game.size*0.3))
            game.window.blit(self.image, rect)

            for eff in game.effects:
                if eff.effect_type == 'Avatar' and eff.parent == self:
                    game.effects.remove(eff)


    def movement(self, game_object, x1=None, x2=None, y1=None, y2=None, paranormal_movement=None, person=None):
        if not paranormal_movement:
            if not game_object.pressed_field.status:
                possibility = True
                if game_object.pressed_field.object:
                    if not game_object.pressed_field.object.can_stay:
                        possibility = False
                if possibility:
                    past_field = game_object.fields[game_object.mover_person.x][game_object.mover_person.y]

                    create_effect((self.x, self.y), (game_object.pressed_field.x, game_object.pressed_field.y),
                                  self, game_object, False, True, self.avatar, 'Avatar', 0.1, 1)
                    self.x = game_object.pressed_field.x
                    self.y = game_object.pressed_field.y
                    past_field.status = None
                    game_object.pressed_field.status = self
                    game_object.end_of_turn(self)
                    print(f'{self} has moved to X:{self.x} Y:{self.y}')

        else:
            if not game_object.fields[x2][y2].status:
                possibility = True
                if game_object.fields[x2][y2].object:
                    if not game_object.fields[x2][y2].object.can_stay:
                        possibility = False
                if possibility:
                    past_field = game_object.fields[x1][y1]
                    self.x = x2
                    self.y = y2
                    past_field.status = None
                    game_object.fields[x2][y2].status = self

                else:
                    if self.cls == 'Warrior':
                        game_object.charge_stop = True
            else:
                if self.cls == 'Warrior':
                    game_object.charge_stop = True

    def basic_attack(self, game):
        if game.pressed_field.status:
            if game.pressed_field.status.side != game.mover_person.side:
                if check_longth(game.pressed_field, self, self.range, game):
                    game.undamaged = game.pressed_field.status
                    if game.undamaged.can_be_attacked:
                        dmg = possible_damage(game.undamaged, game.mover_person.damage,
                                                                                game.undamaged.defence,
                                                                                game.mover_person.basic_dmg_cof,
                                                                                game.undamaged.shield, game.undamaged.avoidance)
                        game.undamaged.health[0] -= dmg
                        game.mover_person.health[0] -= round(dmg * game.undamaged.reflect)
                        if self.cls == 'Mage':
                            create_effect((self.x, self.y), (game.undamaged.x, game.undamaged.y)
                                          , self, self.game_object, False, True,
                                          self.game_object.flameshots, 'Flameshot', 0.2, 2)
                        elif self.range == 4:

                            create_effect((self.x, self.y), (game.undamaged.x, game.undamaged.y)
                                          , self, self.game_object, False, True,
                                          self.game_object.punches, 'Punch', 0.4, 0.4)
                        elif self.range in (1, 2):
                            create_effect((self.x, self.y), (game.undamaged.x, game.undamaged.y)
                                          , self, self.game_object, False, True,
                                          self.game_object.slashes, 'Slash', 0.2, 0.5)

                        print(f'{game.mover_person} has attacked {game.undamaged}! - {dmg} damage')

                        if self.cls == 'Mage':
                            if not random.randrange(0, 4):
                                Object(game.undamaged.x, game.undamaged.y, 'Firewall', game.fields, game, 2)
                        elif self.cls == 'Necropet':
                            for i in game.persons:
                                if i.side == self.side:
                                    i.health[0] += possible_heal(i, dmg//6)
                        elif self.cls == 'Rogue':
                            StatusEffect(game.undamaged, 'Blood', 3, 1, 20, 'Rogue_blood', True, True)
                        dead = []
                        if game.undamaged.health[0] <= 0:
                            dead.append([game, game.undamaged])

                        game.end_of_turn(self, dead)

    def __repr__(self):
        return f'{self.cls} {self.side}'

