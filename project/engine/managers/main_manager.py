from project.engine.managers.support_managers.engine_manager.engine_manager import EngineManager
from project.engine.managers.game_managers.input_manager.input_manager import InputManager
from project.engine.managers.game_managers.scene_manager.scene_manager import SceneManager
from project.engine.managers.UI_managers.text_manager.text_manager import TextManager
from project.engine.managers.game_managers.time_manager.time_manager import TimeManager
from project.engine.managers.UI_managers.widget_manager.widget_manager import WidgetManager
from project.engine.managers.game_managers.window_manager.window_manager import WindowManager
from project.engine.utills.logging.log import log_info

class MainManager():
    def __init__(self, main):
        self.main = main

    def create_submanagers(self):
        log_info('sub managers init: start')
        self.window_manager = WindowManager(self.main)
        self.input_manager = InputManager(self.main)
        self.scene_manager = SceneManager(self.main)
        self.time_manager = TimeManager(self.main)
        self.widget_manager = WidgetManager(self.main)
        self.text_manager = TextManager()
        self.engine_manager = EngineManager(self.main)
        log_info('sub managers init: complete')


    def setup_submanagers(self):
        log_info('sub managers setup: start')
        self.window_manager.setup(self.main.settings)
        self.input_manager.setup(self.main.settings)
        self.scene_manager.setup(self.main.settings)
        self.text_manager.setup(self.main.settings)
        self.engine_manager.setup(self.main.settings)
        log_info('sub managers setup: complete')

    def __repr__(self):
        return 'main_manager'