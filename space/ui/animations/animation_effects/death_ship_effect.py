from space.scripts.calculators.get_scripts import get_pixel_position
from space.ui.animations.animation import Animation


class DeathShipEffect(Animation):
    def __init__(self, object):
        super().__init__(object, object.game.main)
        self.object = object
        self.game = self.object.game
        self.progress = 256

        self.position_x, self.position_y = get_pixel_position(self.object)

    def update(self):
        if self.progress > 0:
            self.progress -= 2
            self.object.direction -= 3
            self.exchange_sipites(self.object.direction, self.progress)

            if self.current_frame_int < self.frames_len - 1:
                self.current_frame_int += 1
                self.current_time = 0
            else:
                self.current_time = 0
                self.current_frame_int = 0
            self.current_frame = self.frames_pool[self.current_frame_int]

        else:
            self.game.main.manager.animation.remove_effect(self)

    def draw(self):
        s = self.object.surf_size
        rect = (self.position_x,
                self.position_y,
                s, s)

        self.game.main.window.blit(self.current_frame, rect)
