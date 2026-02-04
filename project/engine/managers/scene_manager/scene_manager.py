from project.engine.managers.scene_manager.scenes.scenes import SceneTypes
from project.engine.utills.logging.log import log_info


class SceneManager:
    def __init__(self, main):
        self.main = main
        self.current_scene = None

    def change_scene(self, scene):
        log_info(f'scenes changing: start')
        if self.current_scene:
            self.current_scene.kill_scene()

        self.current_scene = scene(self.main)
        self.current_scene.setup()
        log_info(f'scenes changing: finish')


    def setup(self, settings):
        self.change_scene(SceneTypes.main_scene.value)
