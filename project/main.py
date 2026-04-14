from pygame import init

from project.data.protocols.protocols import MainLike
from project.data.settings.settings_lib import SettingsLib
from project.engine.events.event_bus import EventBus
from project.engine.events.event_types import EventTypes
from project.engine.modules.UI_modules.camera_module.camera_module import Camera
from project.engine.modules.game_modules.input_modules.cursor import Cursor
from project.engine.modules.main_module import MainModule
from project.engine.utills.logging.log import setup_logging, log_info


class Game(MainLike):
    ''' Основной класс игры, подгружает подсистемы '''

    def __init__(self):
        init()
        setup_logging()
        log_info('game initialization: start')

        self.run = True

        self.modules = MainModule(self)
        self.events = EventBus()

        self.events.subscribe(self, EventTypes.EXITGAMEEVENT, 0)
        self.events.subscribe(self, EventTypes.CHANGEFLAG)
        self.events.subscribe(self, EventTypes.ACTIVATEFUNCTION)
        self.settings = SettingsLib()
        self.cursor = Cursor(self)
        self.camera = Camera(self)

        self.modules.create_submodules()
        self.modules.setup_submodules()
        log_info('game initialization: finish')

    def mainloop(self):
        while self.run:
            ''' Обновление таймеров '''
            self.modules.time_module.update(0.0083)

            ''' Формирование очереди событий '''
            self.events.begin_frame()

            ''' Выполнение очереди событий '''
            self.events.process_frame()

            ''' Обновление состояния курсора '''
            self.cursor.update_cursor_state()

            ''' сбор инпутов '''
            self.modules.input_module.process_inputs()
            self.modules.console_module.update()

            ''' Обновление менеджеров '''
            self.modules.scene_module.current_scene.update()
            self.modules.widget_module.update()
            self.modules.text_module.update_text_objects()

            ''' Отрисовка менеджеров '''
            self.modules.scene_module.current_scene.draw()
            self.modules.text_module.draw_text_objects()
            self.modules.widget_module.draw(self.modules.window_module.app)

            ''' обновление экрана '''
            self.modules.window_module.update_window()

    def trigger(self, msg, data):
        if msg == EventTypes.EXITGAMEEVENT:
            self.run = data['run']
            self.modules.engine_module.save_config_to_json()
            return True

        elif msg == EventTypes.CHANGEFLAG:
            parameter = self
            for next_par in data[:-1]:
                parameter = getattr(parameter, next_par)
            val = getattr(parameter, data[-1])
            setattr(parameter, data[-1], False if val else True)
            return True

        elif msg == EventTypes.ACTIVATEFUNCTION:
            ''' может вызывать функции с нулем аргументов, или со строкутурой аргументов '''
            func = self
            for next_par in data['path']:
                func = getattr(func, next_par)
            if data['args']:
                func(data['args'])
            else:
                func()
        return False


    def get_parameter(self, path, direct=False) -> object|int|float|str:
        if not direct:
            parameter = self if path[0] == 'main' else getattr(self, path[0])
            for next_par in path[1:]:
                parameter = getattr(parameter, next_par)
            return parameter
        else:
            parameter = self if path[0] == 'main' else getattr(self, path[0])
            for next_par in path[1:]:
                parameter = getattr(parameter, next_par)
            if not isinstance(parameter, str) and not isinstance(parameter, int) and not isinstance(parameter, float) and not isinstance(parameter, list) and not isinstance(parameter, tuple):
                d = dir(parameter)
                fields = [field for field in d if not callable(getattr(parameter, field))]
                return fields
            else:
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
