from project.engine.managers.game_managers.scene_manager.scenes.EngineScene.EngineScene import EngineScene
from project.engine.managers.game_managers.scene_manager.scenes.MainScene.main_scene import MainScene
from project.engine.managers.game_managers.scene_manager.scenes.battle_scene.BattleScene import BattleScene

scene_types = {
    "main_scene": MainScene,
    "engine_scene": EngineScene,
    "battle_scene": BattleScene
}
