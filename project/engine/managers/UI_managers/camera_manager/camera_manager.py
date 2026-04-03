from project.data.protocols.protocols import MainLike, CameraManagerLike
from project.engine.events.event_types import EventTypes
from project.engine.utills.logging.log import log_info


class Camera(CameraManagerLike):
    def __init__(self, main: MainLike):
        super().__init__()
        log_info('Camera init: start')
        self.zoom = 1
        self.outpost_x, self.outpost_y = 0, 0
        self.main = main

        self.container = {}

        self.main.events.subscribe(self, EventTypes.GETBATTLEMAPCONFIGURATION, 0)

        log_info('Camera init: finish')

    def get_battle_map_configuration(self):
        ''' Создает событие, которое пробегается по battle_map и собирает данные в data, сохраняет в self.container '''
        self.main.events.push_emit(EventTypes.GETBATTLEMAPCONFIGURATION, {})
        return self.container

    def update(self):
        pass

    def draw(self):
        pass

    def trigger(self, msg, data):
        if msg == EventTypes.GETBATTLEMAPCONFIGURATION:
            self.container = data
            self.container["camera_outpost"] = (self.outpost_x, self.outpost_y)
            self.container["zoom"] = self.zoom
            return True

    def __repr__(self):
        return 'Camera object'
