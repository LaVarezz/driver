from space.scripts.utils.battle_utils.initiative_tools import begin_turn, end_turn
from space.settings.constants.battle_constants import TurnPhase, Phase
from space.engine.contollers.handler import event_handler

def turn_controller(game):

    if game.turn_phase == TurnPhase.BEGIN_TURN:
        begin_turn(game.queue.current_mover)
        game.turn_phase = TurnPhase.PLAYER_PHASE
        game.fl = False

    elif game.turn_phase == TurnPhase.PLAYER_PHASE:
        event_handler(game)


    elif game.turn_phase == TurnPhase.END_TURN:
        game.turn_phase = TurnPhase.BEGIN_TURN
        end_turn(game.queue.current_mover)
        if game.queue.is_queue_empty or game.main.test_mode:
            game.queue.refill_queue()
            game.phase = Phase.END_ROUND
