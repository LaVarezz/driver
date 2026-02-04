from pygame import init

from project.data.settings.settings_lib import SettingsLib
from project.engine.events.event_bus import EventBus
from project.engine.events.event_types import EventTypes
from project.engine.managers.main_manager.main_manager import MainManager
from project.engine.managers.widget_manager.widgets.buttons.commands.command_types import CommandTypes
from project.engine.managers.widget_manager.widgets.widget_types import WidgetTypes
from project.engine.utills.logging.log import setup_logging, log_info


class Game:
    ''' Основной класс игры, подгружает подсистемы '''

    def __init__(self):
        init()
        setup_logging()
        log_info('game initialization: start')

        self.run = True

        self.manager = MainManager(self)
        self.events = EventBus()

        self.events.subscribe(self, EventTypes.EXITGAMEEVENT)
        self.settings = SettingsLib()

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

            ''' сбор инпутов '''
            self.manager.input_manager.get_inputs()

            ''' Обновление менеджеров '''
            self.manager.scene_manager.current_scene.update()
            self.manager.widget_manager.update()

            ''' Отрисовка менеджеров '''
            self.manager.scene_manager.current_scene.draw()
            self.manager.widget_manager.draw(self.manager.window_manager.app)

            ''' обновление экрана '''
            self.manager.window_manager.update_window()

    def trigger(self, msg, data):
        if msg == EventTypes.EXITGAMEEVENT:
            self.run = data['run']

    def shutdown(self):
        log_info('game finish: start')
        self.events.unsubscribe(self, EventTypes.EXITGAMEEVENT)
        log_info('game finish: done')


    def __repr__(self):
        return 'Main game object'


if __name__ == '__main__':
    game = Game()
    game.dev_process()
    game.mainloop()
    game.shutdown()
    log_info('Bye!')
