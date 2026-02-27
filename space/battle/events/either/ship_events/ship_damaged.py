from space.battle.events.basic_event import Event
from space.battle.events.event_data import EventData

class ShipDamaged(Event):
    def __init__(self, main):
        super().__init__(main)
        self.key = 'ship_damaged'
        self.configuration = 0
        self.positions = ['object', 'value']

    def callback_information(self, data):
        return EventData(data, self.key)

    def __repr__(self):
        return 'ship damaged event init'


