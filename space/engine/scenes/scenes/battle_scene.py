from space.engine.contollers.binds.battle.battlestate_binds import binds
from space.engine.debug.logs.main_log import log_info
from space.engine.managers.managers.core.object_manager import VisibleObject
from space.engine.scenes.scenes.basic_scene import BasicScene
from space.engine.scenes.scene_loops import battle_scene_loop
from space.engine.scenes.scenes.load_scene import LoadScene
from space.settings.configs.resourse_configurations.resourse_configurations import battleload_configuration
from space.settings.settings.battle_settings.battle_settings import setup


class BattleScene(BasicScene):
    def __init__(self, main):
        super().__init__(main)
        self.title = 'Battle Scene'

    def setup(self):
        log_info('Инициализация ядра боевой системы начата')
        self.game = battle_scene_loop.Core()
        self.game.main = self.main
        setup(self.game)
        self.game.main.manager.objects = VisibleObject(self.game.main)
        self.game.bs = self.game.settings.battlefield_settings
        self.game.cs = self.game.settings.camera_settings
        self.game.binds = binds

        self.running = True

        load = LoadScene(self.game.main, self.game, battleload_configuration)
        load.setup()
        load.scene_loop()

        log_info('Инициализация ядра боевой системы успешна.')

    def scene_loop(self):
        log_info('Переход к игровому циклу... ')
        while self.running:
            self.game.mainloop()
        # тут будет смена сцен
        log_info('Выход из сцены... ')

    def kill_scene(self):
        self.running = False
        self.main.manager.objects.destroy_objects()
        if self.main.scene.game.settings_panel:
            self.main.scene.game.settings_panel.kill_panel()
        self.main.reset_managers()



    def __repr__(self):
        return self.title
