from project.data.protocols.protocols import ModuleLike
from project.engine.modules.game_modules.time_module.timer import Timer


class TimeModule(ModuleLike):
    def __init__(self, main):
        super().__init__(main)
        self.timers = []

    def update(self, dt):
        to_add = []
        for timer in self.timers[:]:
            timer.update_timer(dt)
            if not timer.active:
                self.main.events.emit(timer.event, timer.data)
                self.timers.remove(timer)
                if timer.repeat:
                    to_add.append(
                        Timer(self.main, self.main.modules.window_module.time, timer.duration, timer.event, timer.data,
                              timer.repeat))
        self.timers = self.timers + to_add

    def create_timer(self, start, duration, event, data, repeat=False):
        self.timers.append(Timer(self.main, start, duration, event, data, repeat))
