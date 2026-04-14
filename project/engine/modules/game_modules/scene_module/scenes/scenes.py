from project.engine.modules.game_modules.scene_module.scenes.EngineScene.EngineScene import EngineScene
from project.engine.modules.game_modules.scene_module.scenes.MainScene.main_scene import MainScene
from project.engine.modules.game_modules.scene_module.scenes.BattleScene.BattleScene import BattleScene

scene_types = {
    "main_scene": MainScene,
    "engine_scene": EngineScene,
    "battle_scene": BattleScene
}
