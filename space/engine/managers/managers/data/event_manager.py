import weakref

from space.battle.events.either.listeners.text_listener import TextListener
from space.engine.debug.logs.main_log import log_info
from space.scripts.utils.exit import hardcore_exit
from space.settings.constants.event_types import EventTypes
from space.settings.protocols.protocols import ManagerLike

'''
!!! Содержит 3 уровня событий. Нулевой для общего события типа event, первый для общего события
(ship_damaged, т.е какой-то корабль получил урон) и конкретный ship_damaged, т.е конкретный корабль получил урон. 
При создании или погдписи на событие второго уровня, нужно указать так же и объект, к которому событие будет привязано, 
иначе будет ключ None и может вылезти ошибка.
'''

auto_test = False


class EventBus(ManagerLike):
    def __init__(self, main):
        try:
            '''
            events содержит уже инициализированный класс события
            keys по ключу возвращает еще не инициализированный класс события
            '''
            self.main = main
            self.events = {}
            self.keys = {}

            self.callbacks = []

            self.events_for_init = []

        except Exception as e:
            log_info(f'Ошибка при подключении обработчика событий: {e}')
            hardcore_exit(main, e)
            raise e
        else:
            log_info('Обработчик событий подключен')

    def add_event(self, event):
        ''' Добавляет событие в реестр, если оно еще не существует. '''
        candidate = event.value(self.main)
        if not self.does_event_exist(candidate):
            if candidate.key not in self.events.keys():
                self.events[candidate.key] = candidate
            if candidate.key not in self.keys.keys():
                self.keys[candidate.key] = event.value
            print('event created')

    def does_event_exist(self, event):
        if event.key in [i.key for i in self.events.values()]:
            return True
        return False

    def get_event(self, event, config_number=False):
        if event in self.events.keys():
            return self.events[event].configuration if config_number else self.events[event]

    def subscribe(self, event, subscriber, obj=None, reverse=False):
        ''' Принимает событие и объект(даже None, т.е глобальное событие, который на него подписывается. reverse=True для отписки от события. '''
        if event in self.keys.keys():
            candidate = self.events[event]
            action = candidate.subscribe if not reverse else candidate.unsubscribe
            sub = weakref.ref(subscriber)
            if sub():
                # log_info(f'object {sub().parent} {'subscribed' if not reverse else 'unsubscribed'} on {candidate}')
                action(sub(), obj)
                return True
            return False

    def emit(self, event, obj, current, **kwargs):
        ''' Стандартный триггер '''
        data = kwargs
        if event in self.keys.keys():
            self.events[event].emit(data, current, obj)
            return True
        return False

    def report(self):
        for event in self.events.values():
            print(f'{event} listeners: {event.subscribers}')

    def once(self, event, listener, current, **kwargs):
        ''' Одноразовый триггер '''
        data = kwargs
        if event in self.keys.keys():
            self.events[event].emit(listener, data, current)
            return True
        return False

    def update(self):
        if self.callbacks:
            container = self.callbacks[0]
            self.callbacks.remove(container)
            obj = container[0]
            data = container[1]
            obj.callback(data)

    def create_events(self):
        self.main.manager.events.add_event(EventTypes.ship_damaged)
        self.main.manager.events.add_event(EventTypes.selected_ship_changed)
        self.main.manager.events.add_event(EventTypes.selected_ship_changed_raw)
        self.main.manager.events.add_event(EventTypes.pointed_ship_changed)
        self.main.manager.events.add_event(EventTypes.pointed_ship_changed_raw)
        self.main.manager.events.add_event(EventTypes.settings_panel_changed)
        self.main.manager.events.add_event(EventTypes.selected_move_changed)


if auto_test:
    class Main():
        def __init__(self):
            pass


    main = Main()

    main.event_bus = EventBus(main)


    class Ship:

        def __init__(self, main):
            self.health = 10

        def __repr__(self):
            return 'Ship'


    main.l = TextListener(main, 1, 0)
    main.sh = Ship(main)
    main.event_bus.add_event(EventTypes.ship_damaged)

    main.event_bus.subscribe('ship_damaged', main.l)
    ''' вызывать при изменении '''
    main.event_bus.emit('ship_damaged', True, object=main.sh, value=123)
    main.event_bus.once('ship_damaged', main.l, False, object=main.sh, value=111)

    main.event_bus.update()
    main.event_bus.update()
    main.event_bus.update()
    main.event_bus.update()
    main.event_bus.update()
