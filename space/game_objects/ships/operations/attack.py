from space.scripts.utils.battle_utils.damage import damage
from space.scripts.utils.battle_utils.get_ship import get_object


def attack(self):
    target_field = self.game.main.manager.cursor.targeted_cell
    self.get_direction(target_field)
    self.animation.exchange_sipites(self.direction)

    if target_field.content:
        undamaged = get_object(self.game.main, target_field.content)
        damage(undamaged, self.damage)

    self.game.queue.next_step()
    self.game.main.manager.objects.update_visible_objects()