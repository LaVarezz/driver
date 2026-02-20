from enum import Enum

class EventTypes(Enum):
    EXITGAMEEVENT = 'exit_game_event'
    TIMERSHUTDOWN = 'timer_shut_down'
    BUTTONCHANGE = 'button_change'
    SCENEHASCHAMGED = 'scene_has_changed'
    SCENEOBJECTSCREATED = "scene_objects_created"
    CHANGEFLAG = 'change_flag'
    ACTIVATEFUNCTION = 'activate_function'