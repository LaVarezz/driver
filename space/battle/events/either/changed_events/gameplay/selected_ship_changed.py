from space.battle.events.basic_event import Event
from space.battle.events.event_data import EventData

class SelectedShipChanged(Event):
    def __init__(self, main):
        super().__init__(main)
        self.key = 'selected_ship_changed'
        self.configuration = 1
        self.positions = ['object']


    def callback_information(self, data):
        return EventData(data, self.key, configuration=1)

    def __repr__(self):
        return 'Selected ship changed init'

