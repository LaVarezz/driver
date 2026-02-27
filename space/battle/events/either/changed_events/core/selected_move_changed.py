from space.battle.events.basic_event import Event
from space.battle.events.event_data import EventData

class SelectedMoveChanged(Event):
    def __init__(self, main):
        super().__init__(main)
        self.key = 'selected_move_changed'
        self.configuration = 0
        self.positions = ['object', 'value']

    def callback_information(self, data):
        return EventData(data, self.key, configuration=self.configuration)

    def __repr__(self):
        return 'Selected move changed init'

