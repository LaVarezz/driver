from space.engine.contollers.binds.normal.normalmenu_binds import binds
from space.engine.debug.logs.main_log import log_info
from space.engine.scenes.scene_loops.settings_scene_loop import MainSettingsMenu
from space.engine.scenes.scenes.basic_scene import BasicScene
from space.settings.configs.resourse_configurations.resourse_configurations import mainsettingsmenu_configuration


class MainSettingsScene(BasicScene):
    def __init__(self, main):
        super().__init__(main)
        self.title = 'Main settings scene'

    def setup(self):
        log_info('Инициализация меню настроек начата.')
        self.menu = MainSettingsMenu()
        self.menu.main = self.main
        self.menu.binds = binds

        mainsettingsmenu_configuration(self.menu)

        self.running = True
        log_info('Инициализация меню настроек успешна.')

    def scene_loop(self):
        log_info('Переход к игровому циклу... ')
        while self.running:
            self.menu.mainloop()
        log_info('Выход из сцены... ')

    def __repr__(self):
        return self.title