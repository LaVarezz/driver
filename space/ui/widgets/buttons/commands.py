
from space.settings.constants.click_constants import ClickStates
from space.settings.constants.scenes_constants import Scenes
from space.settings.protocols.protocols import MainLike


def test_command(main: MainLike):
    print(main.scene)

def set_battle_scene(main: MainLike):
    main.change_scene(main.scenes_pull[Scenes.BATTLE_SCENE])

def set_main_scene(main: MainLike):
    main.change_scene(main.scenes_pull[Scenes.MAIN_SCENE])

def set_main_settings_scene(main: MainLike):
    main.change_scene(main.scenes_pull[Scenes.MAIN_SETTINGS_SCENE])


def select_moving_command(main: MainLike):
    if main.scene.game.control_panel:
        main.manager.cursor.selecting_state = ClickStates.SelectMoveCellState
        main.manager.events.emit('selected_move_changed', None, True, object=main.manager.clicks, value=ClickStates.SelectMoveCellState.value)

def select_attack_command(main: MainLike):
    if main.scene.game.control_panel:
        main.manager.cursor.selecting_state = ClickStates.SelectAttackCellState
        main.manager.events.emit('selected_move_changed', None, True, object=main.manager.clicks, value=ClickStates.SelectAttackCellState.value)
