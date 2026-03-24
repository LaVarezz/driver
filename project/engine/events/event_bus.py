from project.engine.events.event_types import EventTypes
from project.engine.utills.logging.log import log_warning


class EventBus:
    def __init__(self):
        ''' Управление событиями. Ключем в подписке является тип события, а значением - подписчик. '''
        self._current_events = []
        self._next_events = []
        self._subscribes = {}

    def subscribe(self, listener, event_type, priority=1):
        ''' Защита от дурака '''
        if hasattr(listener, 'trigger'):
            if event_type not in self._subscribes.keys():
                self._subscribes[event_type] = {}
            if listener not in self._subscribes[event_type]:
                ''' priority's logic '''
                if priority not in self._subscribes[event_type]:
                    self._subscribes[event_type][priority] = []

                self._subscribes[event_type][priority].append(listener)

        else:
            log_warning('Слушатель не найден или у него отсутствует trigger')

    def unsubscribe(self, listener, event_type=None):
        if event_type and event_type in self._subscribes.keys():
            if listener in self._subscribes[event_type].values():

                for priority in self._subscribes[event_type].keys():
                    if self._subscribes[event_type][priority] == listener:
                        self._subscribes[event_type][priority].remove(listener)
        else:
            for event in self._subscribes:
                for priority in self._subscribes[event].keys():
                    if self._subscribes[event][priority] == listener:
                        self._subscribes[event][priority].remove(listener)

    def emit(self, msg, data):
        self._next_events.append((msg, data))

    def push_emit(self, msg, data):
        if msg in self._subscribes.keys():
            for priority in sorted(self._subscribes[msg].keys(), reverse=True):
                for listener in self._subscribes[msg][priority]:
                    if listener.trigger(msg, data):
                        break

    def begin_frame(self):
        self._current_events, self._next_events = self._next_events, []

    def process_frame(self):
        for event in self._current_events:
            if event[0] in self._subscribes.keys():
                for priority in sorted(self._subscribes[event[0]].keys(), reverse=True):
                    for listener in self._subscribes[event[0]][priority][:]:
                        if listener.trigger(event[0], event[1]):
                            break

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
