''' Логика боевой очереди '''
from space.engine.debug.logs.main_log import log_info


def set_phase(game, phase):
    log_info(f'Переход в фазу раунда {str(phase)[6:]}')
    game.phase = phase

def set_turn_phase(game, phase):
    log_info(f'Переход в фазу хода {str(phase)[6:]}')
    game.turn_phase = phase