from enum import Enum



class Phase(Enum):
    BEGIN_ROUND = 'begin_round'
    BATTLE_PHASE = 'battle_round'
    END_ROUND = 'end_round'

class TurnPhase(Enum):
    BEGIN_TURN = 'begin_phase'
    PLAYER_PHASE = 'player_phase'
    END_TURN = 'end_phase'

class Types(Enum):
    SHIP = 'ship'
    CELL = 'cell'
    IMAGE = 'image'

