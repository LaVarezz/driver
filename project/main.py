from pygame import init

from project.data.protocols.protocols import MainLike
from project.data.settings.settings_lib import SettingsLib
from project.engine.events.event_bus import EventBus
from project.engine.events.event_types import EventTypes
from project.engine.managers.input_manager.cursor import Cursor
from project.engine.managers.main_manager.main_manager import MainManager
from project.engine.utills.logging.log import setup_logging, log_info


class Game(MainLike):
    ''' Основной класс игры, подгружает подсистемы '''

    def __init__(self):
        init()
        setup_logging()
        log_info('game initialization: start')

        self.run = True

        self.manager = MainManager(self)
        self.events = EventBus()

        self.events.subscribe(self, EventTypes.EXITGAMEEVENT)
        self.events.subscribe(self, EventTypes.CHANGEFLAG)
        self.events.subscribe(self, EventTypes.ACTIVATEFUNCTION)
        self.settings = SettingsLib()
        self.cursor = Cursor(self)

        self.manager.create_submanagers()
        self.manager.setup_submanagers()
        log_info('game initialization: finish')

    def mainloop(self):
        while self.run:
            ''' Обновление таймеров '''
            self.manager.time_manager.update(0.0083)

            ''' Формирование очереди событий '''
            self.events.begin_frame()

            ''' Выполнение очереди событий '''
            self.events.process_frame()

            self.cursor.update_cursor_state()

            ''' сбор инпутов '''
            self.manager.input_manager.process_inputs()

            ''' Обновление менеджеров '''
            self.manager.scene_manager.current_scene.update()
            self.manager.widget_manager.update()
            self.manager.text_manager.update_text_objects()

            ''' Отрисовка менеджеров '''
            self.manager.scene_manager.current_scene.draw()
            self.manager.text_manager.draw_text_objects()
            self.manager.widget_manager.draw(self.manager.window_manager.app)



            ''' обновление экрана '''
            self.manager.window_manager.update_window()

    def trigger(self, msg, data):
        if msg == EventTypes.EXITGAMEEVENT:
            self.run = data['run']
            self.manager.engine_manager.save_config_to_json()
        elif msg == EventTypes.CHANGEFLAG:
            parameter = self
            for next_par in data[:-1]:
                parameter = getattr(parameter, next_par)
            val = getattr(parameter, data[-1])
            setattr(parameter, data[-1], False if val else True)
        elif msg == EventTypes.ACTIVATEFUNCTION:
            ''' может вызывать функции с нулем аргументов, или со строкутурой аргументов '''
            func = self
            for next_par in data['path']:
                func = getattr(func, next_par)
            if data['args']:
                func(data['args'])
            else:
                func()


    def get_parameter(self, path):
        parameter = self
        for next_par in path[1:]:
            parameter = getattr(parameter, next_par)
        return parameter

    def shutdown(self):
        log_info('game finish: start')
        self.events.unsubscribe(self, EventTypes.EXITGAMEEVENT)
        log_info('game finish: done')

    def dev_process(self):
        ''' сюды вводить код, который выполняется при старте в целях проверки и отладки '''
        pass

    def __repr__(self):
        return 'Main game object'


if __name__ == '__main__':
    game = Game()
    game.dev_process()
    game.mainloop()
    game.shutdown()
