''' Рассчет инициативы из модификаторов '''
from space.scripts.utils.reselect_ship import reselect


def begin_round(game):
    """Сброс модификаторов, подготовка к новому раунду"""
    ships = game.main.manager.objects.ships
    for ship in ships.values():
        for key, valur in ship.initiative_coeffs.items():
            if key != 'basic':
                ship.initiative_coeffs[key] = 0

        if ship.is_flagship_near:
            ship.initiative_coeffs['flagship'] += game.FLAGSHIP_INITIATIVE_BONUS

    game.queue.refill_queue()
    reselect(game.main)


def begin_turn(unit):
    """Обработка начала хода конкретного юнита"""


def end_turn(unit):
    """Обработка конца хода конкретного юнита"""


def end_round(game):
    """Завершение раунда: отчистка статусов, таймеров, возможно проверка победы"""


phase_handler = {
    'begin_round': begin_round,
    'begin_turn': begin_turn,
    'end_turn': end_turn,
    'end_round': end_round,
}
