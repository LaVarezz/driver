from enum import Enum


class Directions(Enum):
    NORTH_WEST = (0, 0)
    NORTH_EAST = (0, 1)
    WEST = (1, 0)
    EAST = (1, 1)
    SOUTH_WEST = (2, 1)
    SOUTH_EAST = (2, 0)

    def __init__(self, angle, reverse):
        self.angle = angle
        self.reverse = reverse


class States(Enum):
    IDLE = 'idle'
    ATTACK = 'attack'
    MOVE = 'move'
