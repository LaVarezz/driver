from itertools import chain

from space.engine.debug.logs.main_log import log_info
from space.scripts.utils.reselect_ship import reselect


class BattleQueue:
    def __init__(self, ships):
        self.first_side, self.second_side, self.third_side = [], [], []
        self.sides = [self.first_side, self.second_side, self.third_side]
        self.queue = [self.first_side, self.second_side, self.third_side]
        for ship in ships.values():
            self.queue[ship.side].append(ship)
        self.absolute_queue = []
        self.refill_queue()
        self.absolute_queue = list(chain(*self.queue))

    @property
    def current_mover(self):
        ''' Возвращает ходящего в данный момент '''
        if self.absolute_queue:
            return self.absolute_queue[0]
        return None

    @property
    def current_side(self):
        if self.absolute_queue:
            return self.absolute_queue[0].side
        else:
            return 0 # Пустая очередь означает, что идет фаза завершения хода, а следующий будет ходить игрок, гы

    def remove_ship(self, ship):
        if ship in self.absolute_queue:
            self.absolute_queue.remove(ship)
        if ship in self.queue[ship.side]:
           self.queue[ship.side].remove(ship)


    def next_step(self):
        ''' Удаляет последнего ходящего из очереди'''
        if self.absolute_queue:
            del self.absolute_queue[0]

    def refill_queue(self):
        ''' Обновляет очередь для нового хода '''
        for i in range(2):
            self.queue[i] = sorted(self.queue[i], key=lambda x: x.initiative, reverse=True)
            self.absolute_queue = list(chain(*self.queue))


        log_info(f'Очередь обновлена: игрок {len(self.queue[0])} корабля, противник: {len(self.queue[1])} корабля. Суммарно {len(self.queue[0] + self.queue[1] + self.queue[2])}')

    @property
    def is_queue_empty(self):
        if not self.absolute_queue:
            return True
        return False