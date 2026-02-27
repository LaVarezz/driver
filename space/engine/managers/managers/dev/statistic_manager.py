from space.engine.debug.logs.main_log import log_info


class StatisticManager:
    def __init__(self, main):
        self.main = main
        self.stats = {}
        log_info('Модуль статистики подключен. ')

    def update_statistic(self, slot, value):
        if slot in self.stats.keys():
            self.stats[slot] += value
        else:
            self.stats[slot] = value

    def return_statistic(self, slot=False, all=False):
        if not all:
            return self.stats[slot]
        return self.stats
