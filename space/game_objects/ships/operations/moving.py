from space.scripts.utils.battle_utils.place_ship_to_cords import place_ship_to_cords
from space.settings.constants.ship_constants import States
from space.ui.animations.animation_effects.moving_effect import MovingEffect


def move_to(self):
    target_field = self.game.main.manager.cursor.targeted_cell
    self.get_direction(target_field)
    self.animation.exchange_sipites(self.direction)

    if not target_field.content:
        self.game.main.manager.animation.add_effect(
            MovingEffect(self, target_field, 500))
        place_ship_to_cords(self, (target_field.x, target_field.y), self.game)
        self.state = States.MOVE

    self.game.queue.next_step()
    self.game.main.manager.objects.update_visible_objects()