from space.battle.battlequeue import BattleQueue
from space.engine.debug.logs.main_log import log_info


def script_create_queue(self):
    log_info('Очередь создается... ')
    q = []
    for ship in self.main.manager.objects.player_ships:
        q.append(ship)
    for ship in self.main.manager.objects.enemy_ships:
        q.append(ship)
    for ship in self.main.manager.objects.void_ships:
        q.append(ship)
    self.queue = BattleQueue(self.main.manager.objects.ships)
    self.queue.game = self
    log_info("Очередь успешно создана!")
