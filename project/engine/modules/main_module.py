from project.engine.modules.support_modules.console_module.console_module import ConsoleModule
from project.engine.modules.support_modules.engine_module.engine_module import EngineModule
from project.engine.modules.game_modules.input_modules.input_module import InputModule
from project.engine.modules.game_modules.scene_module.scene_module import SceneModule
from project.engine.modules.UI_modules.text_module.text_module import TextModule
from project.engine.modules.game_modules.time_module.time_module import TimeModule
from project.engine.modules.UI_modules.widget_module.widget_module import WidgetModule
from project.engine.modules.game_modules.window_module.window_module import WindowModule
from project.engine.utills.logging.log import log_info

class MainModule():
    def __init__(self, main):
        self.main = main

    def create_submodules(self):
        log_info('submodules init: start')
        self.window_module = WindowModule(self.main)
        self.input_module = InputModule(self.main)
        self.scene_module = SceneModule(self.main)
        self.time_module = TimeModule(self.main)
        self.widget_module = WidgetModule(self.main)
        self.text_module = TextModule()
        self.engine_module = EngineModule(self.main)
        self.console_module = ConsoleModule(self.main)
        log_info('submodules init: complete')


    def setup_submodules(self):
        log_info('submodules setup: start')
        self.window_module.setup(self.main.settings)
        self.input_module.setup(self.main.settings)
        self.scene_module.setup(self.main.settings)
        self.text_module.setup(self.main.settings)
        self.engine_module.setup(self.main.settings)
        log_info('submodules setup: complete')

    def __repr__(self):
        return 'main module'