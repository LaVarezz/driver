from project.engine.events.event_types import EventTypes


class EventBus:
    def __init__(self):
        ''' Управление событиями. Ключем в подписке является тип события, а значением - подписчик. '''
        self._current_events = []
        self._next_events = []
        self._subscribes = {}

    def subscribe(self, listener, event_type):
        ''' Защита от дурака '''
        if hasattr(listener, 'trigger'):
            if event_type not in self._subscribes.keys():
                self._subscribes[event_type] = []
            if listener not in self._subscribes[event_type]:
                self._subscribes[event_type].append(listener)
        else:
            print('Слушатель не найден или у него отсутствует trigger')

    def unsubscribe(self, listener, event_type=None):
        if event_type and event_type in self._subscribes.keys():
            if listener in self._subscribes[event_type]:
                self._subscribes[event_type].remove(listener)
        else:
            for event in self._subscribes:
                if listener in self._subscribes[event]:
                    self._subscribes[event].remove(listener)

    def emit(self, msg, data):
        self._next_events.append((msg, data))

    def begin_frame(self):
        self._current_events, self._next_events = self._next_events, []

    def process_frame(self):
        for event in self._current_events:
            if event[0] in self._subscribes.keys():
                for listener in self._subscribes[event[0]][:]:
                    listener.trigger(event[0], event[1])
        self._current_events = []

    def current_events(self):
        return self._current_events

    def next_events(self):
        return self._next_events

    def try_to_get_event(self, event_type):
        return [event for event in self._next_events if event[0] == event_type]


    def current_len(self):
        return len(self._current_events)

    def next_len(self):
        return len(self._next_events)


auto_test = False
bus = EventBus()
if auto_test:
    bus = EventBus()


    class Dumpling:
        def __init__(self):
            self.age = 100

        def trigger(self, msg, data):
            if msg == EventTypes.EXITGAMEEVENT:
                self.age = data['age']


    dumpling = Dumpling()


    class TimeWaste:
        def __init__(self):
            self.waste = 0
            bus.subscribe(dumpling, EventTypes.EXITGAMEEVENT)

        def time_waste(self):
            self.waste += 70
            if self.waste >= 100:
                data = {
                    'age': self.waste
                }
                bus.emit(EventTypes.EXITGAMEEVENT, data)


    tw = TimeWaste()

    tw.time_waste()
    bus.begin_frame()
    bus.process_frame()
    tw.time_waste()
    bus.begin_frame()
    tw.time_waste()
    bus.begin_frame()
    tw.time_waste()
    bus.begin_frame()
    bus.process_frame()
    if dumpling.age > 100:
        print('Автотест пройден успешно')
