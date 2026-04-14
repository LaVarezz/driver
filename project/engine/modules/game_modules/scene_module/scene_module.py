from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes
from project.engine.modules.game_modules.scene_module.scenes.scenes import scene_types
from project.engine.utills.logging.log import log_info


class SceneModule:
    def __init__(self, main: MainLike):
        self.main = main
        self.current_scene = None

    def change_scene(self, scene: str):
        log_info(f'scenes changing: start')
        if self.current_scene:
            self.current_scene.kill_scene()

        self.current_scene = scene_types[scene](self.main)
        self.current_scene.setup()
        data = {
            "scene": self.current_scene.name
        }
        self.main.events.emit(EventTypes.SCENEHASCHANGED, data)

        log_info(f'scenes changing: finish')


    def setup(self, settings):
        if not self.main.settings.open_settings['dev_mode']:
            self.change_scene('main_scene')
        else:
            self.change_scene('engine_scene')
