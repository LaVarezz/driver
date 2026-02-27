from space.scripts.calculators.get_scripts import get_pixel_position
from space.settings.constants.ship_constants import States
from space.settings.protocols.protocols import Rentable, HasGame, CellLike


class MovingEffect:
    def __init__(self, object: Rentable | HasGame, target_place: CellLike, time: int):

        self.speed = object.game.main.manager.animation.animation_speed

        self.object = object
        self.game = object.game
        self.time = time / self.speed
        self.target_place = target_place

        self.position_x, self.position_y = get_pixel_position(self.object)
        self.target_x, self.target_y = get_pixel_position(self.target_place)

        self.position_x += self.game.main.manager.camera.camera_x
        self.position_y += self.game.main.manager.camera.camera_y
        self.target_x += self.game.main.manager.camera.camera_x
        self.target_y += self.game.main.manager.camera.camera_y

        self.progress = 0

    def update(self):
        self.progress += 0.1*self.speed / self.time

        t = min(self.progress, 1)

        eased = 2*t**2 - 2*t**3

        outpost_x, outpost_y = self.target_x - self.position_x, self.target_y - self.position_y
        outpost_x = outpost_x * eased
        outpost_y = outpost_y * eased

        self.position_x += outpost_x
        self.position_y += outpost_y
        self.time -= 1
        if self.time == 2:
            self.object.state = States.IDLE
        if not self.time:
            self.game.main.manager.animation.remove_effect(self)

    def draw(self):
        rect = (self.position_x-self.game.main.manager.camera.camera_x, self.position_y-self.game.main.manager.camera.camera_y, self.object.surf_size, self.object.surf_size)
        self.game.main.window.blit(self.object.surface, rect)
