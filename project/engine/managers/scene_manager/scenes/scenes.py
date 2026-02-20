from enum import Enum

from project.engine.managers.scene_manager.scenes.EngineScene.EngineScene import EngineScene
from project.engine.managers.scene_manager.scenes.MainScene.main_scene import MainScene


class SceneTypes(Enum):
    main_scene = MainScene
    engine_scene = EngineScene
