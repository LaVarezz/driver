import pygame

from space.engine.debug.logs.main_log import log_warning, log_info, log_error
from space.scripts.loaders.save_json import save_json


def exit_game(main):
    main.scene.running = False
    main.exit_game = True
    log_warning('Загрузка грубо прервана...')
    log_info('Выход из игры... ')
    pygame.quit()
    exit()


def hardcore_exit(main, error):
    main.exit_game = True
    log_error(error)
    try:
        stats = main.manager.statistic.return_statistic(all=True)
        save_json(stats, 'engine/debug/stats/', 'statistic.json')
    except Exception as e:
        log_warning(f'Ошибка при сохранении информации: {e}')
    else:
        log_info('Статистика сохранена')
    log_warning('Выход из игры...')

    pygame.quit()
    exit()
