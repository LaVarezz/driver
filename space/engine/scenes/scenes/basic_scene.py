from space.settings.protocols.protocols import SceneLike


class BasicScene(SceneLike):
    def __init__(self, main):
        self.main = main

    def kill_scene(self):
        self.running = False
    

