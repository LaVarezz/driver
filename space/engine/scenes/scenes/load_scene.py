from space.engine.debug.logs.main_log import log_info
from space.engine.scenes.scene_loops.loading_scene_loop import Loading
from space.engine.scenes.scenes.basic_scene import BasicScene


class LoadScene(BasicScene):
    def __init__(self, main, scene, config):
        super().__init__(main)
        self.title = 'Load Scene'
        self.scene = scene
        self.config = config

    def setup(self):
        log_info('Инициализация загрузочного экрана начата... ')
        self.load = Loading(self.main, self.scene, self.config)
        log_info('Инициализация загрузочного экрана завершена!')

    def scene_loop(self):
        self.running = True
        self.load.mainloop()

    def __repr__(self):
        return self.title
