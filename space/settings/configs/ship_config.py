from dataclasses import dataclass
from enum import Enum

@dataclass
class ShipStates:
    ''' Шаблон для параметров корабля, вызывать в момент создания '''
    '''
    health - очки прочности
    damage - очки урона(пока общий)
    length - дальность выстрела
    move_points - дальность перемещения за ход
    ship_weight - вес корабля, влияет на инициативу.
    ship_tonnage - тип корабля (Дрон, линкор, ремонтная баржа и тд
    '''
    health: int
    damage: int #потом придется делить на орудия
    length: int
    move_points: int
    ship_weight: int
    ship_tonnage: str # пока

class ShipBasicStates(Enum):
    FRIGATE = ('Фрегат', 150, 300, 2, 2, 400)
    DESTROYER = ('Эсминец', 250, 300, 3, 1, 600)

    def __init__(self, title, damage, health, length, move_points, mass):
        self.title = title
        self.damage = damage
        self.health = health
        self.length = length
        self.move_points = move_points
        self.mass = mass