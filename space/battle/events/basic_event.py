from space.engine.debug.logs.main_log import log_warning


class Event:
    def __init__(self, main):
        self.main = main
        self.subscribers = {}

        self.main.manager.events.events_for_init.append(self)

    def emit(self, data, current, obj=None):
        ''' Локальные слушатели '''
        if obj in self.subscribers.keys():
            for sub in self.subscribers[obj]:
                if current:
                    sub.callback(self.callback_information(data))
                else:
                    self.main.callbacks.append((sub, self.callback_information(data)))

        ''' Глобальные слушатели '''
        if obj:
            for sub in self.subscribers[None]:
                try:
                    if current:
                        sub.callback(self.callback_information(data))
                    else:
                        self.main.callbacks.append((sub, self.callback_information(data)))
                except Exception as e:
                    log_warning(f'Ошибка в emit ({self.key}): {e}')

    def subscribe(self, subscriber, obj):
        if obj not in self.subscribers.keys():
            self.subscribers[obj] = []
        self.subscribers[obj].append(subscriber)

    def unsubscribe(self, subscriber, obj):
        if obj in self.subscribers.keys():
            if subscriber in self.subscribers[obj]:
                self.subscribers[obj].remove(subscriber)

    def callback_information(self, data):
        return None
