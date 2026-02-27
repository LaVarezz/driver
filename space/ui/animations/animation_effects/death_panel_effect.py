
class DeathPanelEffect:
    def __init__(self, object):
        self.object = object
        self.game = self.object.main.scene.game
        self.progress = self.object.alpha

        self.position_x, self.position_y = self.object.x, self.object.y


    def update(self):
        if self.progress > 0:
            self.progress -= 2
            self.object.surface.set_alpha(self.progress)
        else:
            self.object.destroy_panel()
            self.game.main.manager.animation.remove_effect(self)

    def draw(self):
        rect = (self.position_x,
                self.position_y,
                self.object.main_width, self.object.main_height)

        self.game.main.window.blit(self.object.surface, rect)
