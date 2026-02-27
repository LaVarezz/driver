from space.engine.debug.debug_state import DebugState
from space.engine.debug.logs.main_log import log_info
from space.settings.settings.main_settings.config import Settings, WindowSettings
from space.settings.settings.main_settings.env import Env


def setup(self):
    log_info('Настройка окна начата')
    ''' Надстройки '''
    self.test_mode = DebugState()
    self.test_mode.show_debug_ui = Env.test_mode

    width, height = Env.screen_size
    fps = Env.fps
    '''Фоны'''
    self.backgrounds = {}
    ''' Обьекты '''

    self.settings = Settings(
        WindowSettings(width, height, fps)
    )
    ''' Менеджеры '''
    self.reset_managers(new=True)

    log_info('Настройка окна завершена')
