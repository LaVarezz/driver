import pygame as pg

from space.settings.constants.ship_constants import States
from space.settings.settings.battle_settings.env import Env

class DownloadManager:
    def __init__(self, main):
        self.main = main

    def download_ship(self, type, name, game, load):
        path = f'{Env.ships_sprite_path}/{type}/{name}/'

        i = []
        for n in range(1, 9):
            i.append(pg.image.load(f'{path}idle/fregat_idle_{n}.png').convert_alpha())
            pg.display.update()
            load.draw_update_interface()

        a = []
        for n in range(1, 9):
            a.append(pg.image.load(f'{path}attack/fregat_atk_{n}.png').convert_alpha())
            pg.display.update()
            load.draw_update_interface()

        m = []
        for n in range(1, 9):
            m.append(pg.image.load(f'{path}walk/fregat_walk_{n}.png').convert_alpha())
            pg.display.update()
            load.draw_update_interface()

        idle = {}
        attack = {}
        move = {}
        for j in range(0, 21, 2):
            value = j / 10
            size = game.bs.field_size * value

            idle[value] = []
            for img in i:
                idle[value].append(pg.transform.smoothscale(img, (size, size)))
                load.draw_update_interface(lite=True)

            attack[value] = []
            for img in a:
                attack[value].append(pg.transform.smoothscale(img, (size, size)))
                load.draw_update_interface(lite=True)

            move[value] = []
            for img in m:
                move[value].append(pg.transform.smoothscale(img, (size, size)))
                load.draw_update_interface(lite=True)


        dict_for_return = {
            States.IDLE: idle,
            States.ATTACK: attack,
            States.MOVE: move
        }
        original_dict_for_return = {
            States.IDLE: i,
            States.ATTACK: a,
            States.MOVE: m
        }
        return dict_for_return, original_dict_for_return

    def download_background(self, bg):
        path = f'{Env.bg_sprite_path}'

        i = []
        for n in range(1, 9):
            img = pg.image.load(f'{path}bg1.png').convert()
            i.append(pg.transform.scale(img, bg.size))
            pg.display.update()


        dict_for_return = {
            States.IDLE: i,
        }
        original_dict_for_return = {
            States.IDLE: i,
        }
        return dict_for_return, original_dict_for_return
