import pygame as pg

from space.engine.debug.logs.main_log import log_info
from space.engine.managers.main_manager import Manager
from space.engine.managers.managers.core.object_manager import VisibleObject
from space.engine.managers.managers.data.contain_manager import Container
from space.engine.managers.managers.data.download_manager import DownloadManager
from space.engine.managers.managers.data.event_manager import EventBus
from space.engine.managers.managers.dev.statistic_manager import StatisticManager
from space.engine.managers.managers.ui.animation_manager import AnimationHandler
from space.engine.managers.managers.ui.camera_manager import CameraControl
from space.engine.managers.managers.ui.click_manager import ClickManager
from space.engine.managers.managers.ui.image_manager import ImageManager
from space.engine.managers.managers.ui.overlay_manager import OverlayManager
from space.engine.managers.managers.ui.widget_manager import UImanager
from space.engine.scenes.scenes.battle_scene import BattleScene
from space.engine.scenes.scenes.load_scene import LoadScene
from space.engine.scenes.scenes.main_scene import MainScene
from space.engine.scenes.scenes.settings_scene import MainSettingsScene
from space.game_objects.cursors.cursor import Cursor
from space.scripts.loaders.save_json import save_json
from space.scripts.utils.exit import hardcore_exit
from space.settings.constants.scenes_constants import Scenes
from space.settings.protocols.protocols import MainLike
from space.settings.settings.main_settings.env import Env
from space.settings.settings.main_settings.main_settings import setup


class Game(MainLike):
    def __init__(self):
        log_info('Инициализация игры начата')
        pg.init()
        self.scenes_pull = {
            Scenes.LOAD_SCENE: LoadScene,
            Scenes.BATTLE_SCENE: BattleScene,
            Scenes.MAIN_SCENE: MainScene,
            Scenes.MAIN_SETTINGS_SCENE: MainSettingsScene
        }
        setup(self)
        self.scene = None
        self.ws = self.settings.window_settings
        self.window = pg.display.set_mode((self.ws.WIDTH, self.ws.HEIGHT))
        pg.display.set_caption(Env.app_title)
        self.clock = pg.time.Clock()
        self.change_scene(self.scenes_pull[Scenes.MAIN_SCENE])  # Костыль. Удали потом

        log_info('Инициализация игры успешна. ')

    def change_scene(self, scene):
        if self.scene:
            self.scene.kill_scene()
            self.manager.widgets.destroy_UI()
        sc = scene(self)
        log_info(f'Игровая сцена сменилась на {sc}')
        self.scene = sc
        self.scene.setup()

    def mainloop(self):
        self.quit_game = False
        log_info('Вход в игровой цикл... ')
        while not self.quit_game:
            self.scene.scene_loop()
        log_info('Выход из игрового цикла успешен... ')
        stats = self.manager.statistic.return_statistic(all=True)
        save_json(stats, 'engine/debug/stats/', 'statistic.json')
        log_info('Статистика последней игровой сессии сохранена. ')

    def reset_managers(self, new=False):
        log_info('Менеджеры создаются')
        try:
            if new:
                self.manager = Manager()
                self.manager.container = Container(self)
                self.manager.statistic = StatisticManager(self)
                self.manager.downloader = DownloadManager(self)

            self.manager.widgets = UImanager(self)
            self.manager.animation = AnimationHandler(self)
            self.manager.camera = CameraControl(self)
            self.manager.events = EventBus(self)
            self.manager.overlay = OverlayManager(self)
            self.manager.clicks = ClickManager(self)
            self.manager.images = ImageManager(self)
            self.manager.cursor = Cursor(self)
            self.manager.objects = VisibleObject(self)

        except Exception as e:
            log_info(f'Ошибка при подключении менеджеров: {e}')
            hardcore_exit(self, e)
        else:
            log_info('Менеджеры подключены успешно.')

    def __repr__(self):
        return 'MAIN OBJECT'


if __name__ == '__main__':
    Game().mainloop()
