from dataclasses import dataclass, field

from space.resourses.cache.text_cache import TextCache


@dataclass
class WindowSettings:
    ''' Настройки окна '''
    '''
    WIDTH, HEIGHT - длина и высота окна.
    FPS - кол-во кадров в секунду
    mouse_old_pos - старые координаты мыши, для удобства изначально 0, 0
    play - Флаг основного цикла игры
    mousewheel - флаг движения колесика мыши
    '''
    WIDTH: int
    HEIGHT: int
    FPS: int
    mouse_old_pos: tuple[int, int] = (0, 0)
    play: bool = True
    mousewheel: bool = False
    GLOBAL_TEXT_CACHE: dict = field(default_factory=lambda: {
        'default': TextCache(24, 'white'),
        'big': TextCache(32, 'white'),
        'extra': TextCache(64, 'white'),
        'little': TextCache(16, 'white')
    })

@dataclass
class Settings:
    ''' Общие настройки '''
    '''
    battlefield_settings - параметры поля боя
    camera_settings - параметры камеры
    '''
    window_settings: WindowSettings
