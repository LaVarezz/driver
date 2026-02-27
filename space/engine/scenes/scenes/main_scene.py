from space.engine.contollers.binds.normal import normalmenu_binds
from space.engine.debug.logs.main_log import log_info
from space.engine.scenes.scene_loops.main_scene_loop import MainMenu
from space.engine.scenes.scenes.basic_scene import BasicScene
from space.engine.scenes.scenes.load_scene import LoadScene
from space.settings.configs.resourse_configurations.resourse_configurations import mainmenu_configuration


class MainScene(BasicScene):
    def __init__(self, main):
        super().__init__(main)
        self.title = 'Main Scene'

    def setup(self):
        log_info('Инициализация главного меню начата.')
        self.menu = MainMenu()
        self.menu.main = self.main
        self.menu.binds = normalmenu_binds.binds

        self.running = True
        load = LoadScene(self.main, self.menu, mainmenu_configuration)
        load.setup()
        load.scene_loop()

        log_info('Инициализация главного меню успешна.')

    def scene_loop(self):
        log_info('Переход к игровому циклу... ')
        while self.running:
            self.menu.mainloop()
        log_info('Выход из сцены... ')

    def __repr__(self):
        return self.title
