from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Settings:
    ''' Общие настройки '''
    '''
    battlefield_settings - параметры поля боя
    camera_settings - параметры камеры
    '''
    battlefield_settings: BattlefieldSettings
    camera_settings: CameraSettings




@dataclass
class BattlefieldSettings:
    ''' Настройки поля боя '''
    '''
    max_size - максимальный размер поля боя в пикселях
    min_size - минимальный размер поля боя в пикселях
    BATTLEFIELD_SIZE_X, BATTLEFIELD_SIZE_Y - размер игрового поля(в клетках)
    mover - текущий ходящий корабль
    padx, pady - Отступы по x/y поля боя от края экрана в пикселях
    field_size - размер каждой клетки в пикселЯх
    '''
    max_size: int
    min_size: int
    BATTLEFIELD_SIZE_X: int
    BATTLEFIELD_SIZE_Y: int
    field_size: int
    padx: int
    pady: int
    mover: 'SpaseShip' = None

@dataclass
class ShipStates:
    ''' Шаблон для параметров корабля, вызывать в момент создания '''
    '''
    health - очки прочности
    damage - очки урона(пока общий)
    length - дальность выстрела
    move_points - дальность перемещения за ход
    ship_tonnage - тип корабля (Дрон, линкор, ремонтная баржа и тд
    '''
    health: int
    damage: int #потом придется делить на орудия
    length: int
    move_points: int
    ship_tonnage: str # пока




@dataclass
class CameraSettings:
    '''
    camera_x, camera_y - смещение камеры по х и у(в пикселях) от центра отсчета.
    old_camera_x, old_camera_y - смещение за предыдущий кадр
    zoom - размер клетки в пикселях(Изменяется при скроллинге мыши)
    '''
    camera_x: int = 0
    camera_y: int = 0
    old_camera_x: int = 0
    old_camera_y: int = 0
    zoom: int = 1.0