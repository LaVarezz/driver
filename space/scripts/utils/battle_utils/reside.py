''' Логика фаз '''
from space.UI.debug_tools.logs.main_log import log_info


def reside(ship):
    ship.side = [0, 1].remove(ship.side)
    if ship.side:
        ship.side = 0
    else:
        ship.side = 1
    log_info(f'Ship {ship} resided to {ship.side}')
