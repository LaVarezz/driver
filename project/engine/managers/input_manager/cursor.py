from pygame import mouse

from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes
from project.engine.managers.basic_manager import Manager


class Cursor(Manager):
    ''' Собирает изменения положений и состояний мыши и создает события при таковых.'''
    def __init__(self, main: MainLike):
        super().__init__()
        self.main = main
        self.px, self.py = mouse.get_pos()
        self.state = mouse.get_pressed()
        self.previous_state = self.state
        self.rel = (0, 0)

    def update_cursor_state(self):
        ''' Обновляет положение '''
        self.px, self.py = mouse.get_pos()
        self.state = mouse.get_pressed()
        self.rel = mouse.get_rel()
        self.check_matches()
        self.previous_state = self.state

    def check_matches(self):
        ''' сравнивает положения мыши в разных кадрах '''
        if self.state != self.previous_state:
            d = []
            if self.state[0] and not self.previous_state[0]:
                d.append((0, 1))
            elif not self.state[0] and self.previous_state[0]:
                d.append((0, 0))

            if self.state[1] and not self.previous_state[1]:
                d.append((1, 1))
            elif not self.state[1] and self.previous_state[1]:
                d.append((1, 0))

            if self.state[2] and not self.previous_state[2]:
                d.append((2, 1))
            elif not self.state[2] and self.previous_state[2]:
                d.append((2, 0))

            data = {
                'buttons': d,
                'position': (self.px, self.py),
                'rel': self.rel
            }
            self.main.events.emit(EventTypes.BUTTONCHANGE, data)

    def get_mouse_states(self) -> tuple:
        ''' получить положение мыши '''
        return (self.px, self.py, self.rel)
