import space.engine.contollers.binds.battle.battlestate_binds as bb
import space.engine.contollers.binds.normal.normalmenu_binds as nb
from space.engine.debug.logs.main_log import log_info
from space.scripts.generation.bg_generator import create_bg
from space.scripts.generation.queue_generator import script_create_queue
from space.scripts.generation.map_generator import script_create_map
from space.scripts.generation.ship_generation import create_ship
from space.settings.configs.ship_config import ShipBasicStates, ShipStates
from space.ui.widgets.buttons.button import Button
from space.ui.widgets.buttons.commands import set_battle_scene, set_main_settings_scene, test_command, set_main_scene

from space.settings.settings.battle_settings.env import Env
crash_test = Env.stress_test


def battleload_configuration(load):
    kr = 10 if crash_test else 1
    load.main.binds = bb.binds


    log_info('Виджеты создаются')

    load.max_frame_count += 110 * 2 * kr
    load.max_frame_count += 1 * Env.field_size[0] * Env.field_size[1]
    log_info('Виджеты созданы')

    script_create_map(load.scene, load)

    sb = ShipBasicStates

    if Env.spawn_test_ships:
        log_info('Тестовые корабли создаются... ')
        for x in range(0, 4):
            for y in range(0, 1 * kr):
                if x % 2 == 0:
                    create_ship(x % 2, load.scene, load,
                                ShipStates(sb.FRIGATE.health, sb.FRIGATE.damage, sb.FRIGATE.length,
                                           sb.FRIGATE.move_points, sb.FRIGATE.mass, sb.FRIGATE.title),
                                (x, y))
                else:
                    create_ship(x % 2, load.scene, load,
                                ShipStates(sb.DESTROYER.health, sb.DESTROYER.damage, sb.DESTROYER.length,
                                           sb.DESTROYER.move_points, sb.DESTROYER.mass, sb.DESTROYER.title),
                                (x, y))
        log_info('Тестовые корабли созданы!')
    script_create_queue(load.scene)
    create_bg(load.scene.main)

    load.draw_update_interface(done=True)


def mainmenu_configuration(load):
    load.main.binds = nb.binds
    ui = load.main.manager.widgets
    ui.add_widget(Button((30, 150), (400, 100), load.main, ('Game', load.main.ws.GLOBAL_TEXT_CACHE['extra']),
                         command=set_battle_scene, center=(True, False), alpha=False), 3)
    ui.add_widget(Button((30, 400), (400, 100), load.main, ('Settings', load.main.ws.GLOBAL_TEXT_CACHE['extra']),
                         command=set_main_settings_scene, center=(True, False), alpha=False), 3)

    load.max_frame_count += 5

    ''' Создание фона '''
    create_bg(load.main)

    # тут кнопки
    load.draw_update_interface(done=True)

def mainsettingsmenu_configuration(load):
    load.main.binds = nb.binds
    ui = load.main.manager.widgets
    ui.add_widget(Button((100, 150), (400, 100), load.main, ('Test', load.main.ws.GLOBAL_TEXT_CACHE['big']),
                         command=test_command, center=(True, False)), 3)
    ui.add_widget(Button((30, 30), (400, 100), load.main, ('Main menu', load.main.ws.GLOBAL_TEXT_CACHE['big']),
                         command=set_main_scene, center=(True, False)), 3)

