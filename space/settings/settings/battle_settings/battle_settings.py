from space.engine.debug.logs.main_log import log_info, log_error
from space.scripts.utils.exit import hardcore_exit
from space.settings.constants.event_types import EventTypes
from space.settings.settings.battle_settings.calculator import calculator_field_size, calculator_max_size, \
    calculator_battlefield_from_left
from space.settings.settings.battle_settings.config import Settings, BattlefieldSettings, CameraSettings
from space.settings.settings.battle_settings.env import Env

def setup(self):
    ''' Параметры игры '''
    log_info('Настройки ядра начаты... ')
    log_info('Калькулирование настроек начато...')


    self.FLAGSHIP_INITIATIVE_BONUS = 0.3

    ''' Минимальный размер поля боя в пикселях, 
    размер такового в клетках,
    отступ поля боя от края экрана сверху '''
    min_size = 10
    battle_size_x, battle_size_y = Env.field_size
    pady = 40

    ''' Размер каждой клетки поля боя - в пикселЯх '''
    field_size_for_settings = calculator_field_size(self.main.ws.HEIGHT, battle_size_y)

    ''' Размер каждой клетки поля боя - в пикселЯх, пока что ничего не меняет, гы)'''
    max_size_for_settings = calculator_max_size(field_size_for_settings)
    padx_for_settings = calculator_battlefield_from_left(self.main.ws.WIDTH,
                                                         field_size_for_settings,
                                                         battle_size_x)
    ''' Параметры в бою '''
    self.settings_panel = None
    self.control_panel = None
    self.quick_info_panel = None
    self.out_scenes = []

    log_info('Калькулирование настроек завершено!')
    ''' Ивенты '''

    try:
        self.main.manager.events.create_events()
    except Exception as e:
        log_error('Ошибка при создании событий!')
        hardcore_exit(self.main, e)
    else:
        log_info('Создание событий успешно.')

    ''' Готовый класс параметров '''
    self.settings = Settings(
        BattlefieldSettings(max_size_for_settings, min_size, battle_size_x,
                            battle_size_y, field_size_for_settings, padx_for_settings, pady),
        CameraSettings()
    )

    log_info('Настройка ядра завершена!')
