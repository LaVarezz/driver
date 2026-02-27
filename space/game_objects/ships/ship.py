import math
from abc import ABC
from functools import cached_property

import pygame as pg

from space.engine.debug.logs.main_log import log_info
from space.engine.managers.managers.core.object_manager import Object
from space.scripts.calculators.get_scripts import get_pixel_position
from space.settings.configs.ship_config import ShipStates
from space.settings.constants.battle_constants import Types
from space.settings.constants.ship_constants import States
from space.settings.protocols.protocols import ShipLike
from space.ui.animations.animation_effects.death_ship_effect import DeathShipEffect
from space.ui.debug.debug_render import debug_ship_update, debug_ship_draw


class Ship(ABC, Object):
    '''
    x, y - Логические координаты
    side - сторона

    health, ... move_points - параметры корабля как боевой единицы
    ship_weight - Вес корабля
    ship_tonnage - Класс корабля
    '''

    __slots__ = (
        'x', 'y', 'side', '_health', '_damage', '_length', '_move_points', '_ship_weight', '_ship_tonnage', 'game',
        'initiative_coeffs', 'direction', 'is_moving', '_state', 'sprites', 'sprites_original', "animation")

    def __init__(self, cords: tuple[int, int], side: int, parameters: ShipStates):
        Object.__init__(self, cords, Types.SHIP)
        self.side = side
        self._health = parameters.health
        self._damage = parameters.damage
        self._length = parameters.length
        self._move_points = parameters.move_points
        self._ship_weight = parameters.ship_weight
        self._ship_tonnage = parameters.ship_tonnage

        self.direction = 180 * side

        self._state = States.IDLE

        self.game: 'Game_obj' = None

        self.sprites = {}
        self.sprites_original = {}
        self.animation = None

        self.initiative_coeffs = {
            'basic': 1,
            'flagship': 0,
            'stasis': 0,
            'location': 0,
            'another_factors': 0
        }


    @property
    def is_flagship_near(self):
        ''' True, если флагман рядом '''
        return True  # Заглушка

    @property
    def base_initiative(self):
        ''' Базовая инициатива корабля '''
        k = 1  # заглушка
        return (100 * k) / math.log2(self.ship_weight + 1)  # тоннаж пока не представлен как класс, потому его игнорим

    @property
    def initiative(self):
        ''' Фактиеская инициатива '''
        cof = self.initiative_coeffs['basic'] + self.initiative_coeffs['flagship'] \
              + self.initiative_coeffs['stasis'] + self.initiative_coeffs['location'] \
              + self.initiative_coeffs['another_factors']
        return self.base_initiative * cof

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, value):
        self._health = max(value, 0)
        if self._health == 0:
            self.death()

    @property
    def damage(self):
        return self._damage

    @property
    def length(self):
        return self._length

    @property
    def move_points(self):
        return self._move_points

    @move_points.setter
    def move_points(self, value):
        ''' Тут логгирование будет '''
        self._move_points = value
        log_info(f'Установлено {value} очков хода для {self}')

    @cached_property
    def ship_weight(self):
        return self._ship_weight

    @cached_property
    def id(self):
        return self.game.main.manager.objects.create_id(self)

    @property
    def name(self):
        return f'{self._ship_tonnage}: {self.id}'

    @property
    def size(self):
        return self.width, self.height

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        if self._state != value:
            self._state = value
            self.animation.reload_pull()

    def __repr__(self):
        return self.name


class ShipMethods(Ship, ShipLike):
    __slots__ = ('preset', 'is_moving')

    def __init__(self, cords, size, parameters):
        super().__init__(cords, size, parameters)
        self.preset = False

    def update(self):
        if not self.preset:
            self.preset = True
            self.font = self.game.main.ws.GLOBAL_TEXT_CACHE['little']

        if self.game.main.test_mode.show_debug_ui:
            debug_ship_update(self)

    def draw(self):
        if self.state != States.MOVE:
            self.animation.draw()
            self.game.main.window.blit(self.surface, self.rect)
            if self.game.main.test_mode.show_debug_ui:
                debug_ship_draw(self)

    @property
    def surf_size(self):
        return ((self.game.bs.field_size * self.game.main.manager.camera.zoom) ** 2 * 2) ** 0.5

    @property
    def outpost(self):
        return (self.surf_size - self.game.bs.field_size) / 2

    def update_ship_visual(self):
        x0, y0 = get_pixel_position(self)

        self.rect = pg.rect.Rect(x0 - self.outpost, y0 - self.outpost, self.surf_size, self.surf_size)
        self.surface = pg.surface.Surface((self.surf_size, self.surf_size), pg.SRCALPHA)

    def death(self):
        log_info(f'{self} уничтожен')
        mg = self.game.main.manager
        self.game.queue.remove_ship(self)
        mg.objects.remove_object(self)
        self.place.content = None
        mg.cursor.remove_ship_from_select(mg.objects.normalize_object(self))
        mg.animation.remove_effect(self.animation)
        mg.animation.add_effect(DeathShipEffect(self))

    def skip_turn(self):
        log_info(f'{self} Пропустил ход')
        ''' Пропуск хода - потом + к инициативе на следующем ходу '''
        pass

    def can_place(self):
        return True

    def get_direction(self, target_field):
        point_x = get_pixel_position(target_field)[0] - get_pixel_position(self)[0]
        point_y = get_pixel_position(target_field)[1] - get_pixel_position(self)[1]

        self.direction = math.degrees(math.atan2(-point_y, point_x))

    ''' Методы корабля как игрового объекта '''

    def operation(self, operation):
        operation(self)

    ''' Прочее '''

    def get_title(self):
        return self.name

    def get_cords(self):
        return self.x, self.y
