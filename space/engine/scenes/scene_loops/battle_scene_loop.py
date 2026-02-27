from space.engine.managers.managers.core.turn_manager import turn_controller
from space.scripts.utils.battle_utils.initiative_tools import begin_round, end_round
from space.scripts.utils.battle_utils.queue_scripts import set_phase, set_turn_phase
from space.settings.constants.battle_constants import Phase, TurnPhase
from space.engine.contollers.handler import event_handler
from space.battle.updates import update_visual_info
from space.settings.protocols.protocols import SceneLike


class Core(SceneLike):
    def __init__(self):
        set_phase(self, Phase.BEGIN_ROUND)
        set_turn_phase(self, TurnPhase.BEGIN_TURN)

    def mainloop(self):
        update_visual_info(self)
        event_handler(self)
        if self.phase == Phase.BEGIN_ROUND:
            begin_round(self)
            set_phase(self, Phase.BATTLE_PHASE)
        if self.phase == Phase.BATTLE_PHASE:
            ''' Основная фаза боя, если что-то ломается, то 90%, что тут'''
            turn_controller(self)
            if self.queue.is_queue_empty:
                set_phase(self, Phase.END_ROUND)
        if self.phase == Phase.END_ROUND:
            end_round(self)
            set_phase(self, Phase.BEGIN_ROUND)
        # print(self.camera.zoom)

    def __repr__(self):
        return 'Battle Core'
