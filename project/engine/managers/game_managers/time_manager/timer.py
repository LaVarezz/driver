class Timer:
    def __init__(self, main, start, duration, event, data, repeat):
        self.main = main
        self.start = start
        self.finish = self.start + duration
        self.current = self.start
        self.event = event
        self.data = data
        self.repeat = repeat
        self.duration = duration

        self.active = True

    def update_timer(self, dt):
        self.current += dt
        if self.current >= self.finish:
            self.active = False

