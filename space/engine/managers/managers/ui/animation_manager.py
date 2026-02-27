''' Работает с обьектами класса animation. Дает команды на обновлениеЮ отрисовку. Сам добавляет, хранит и удаляет анимации. '''

from space.settings.settings.battle_settings.env import Env



class AnimationHandler:
    def __init__(self, game):
        self.game = game
        self.current_animation = []  # Отрисовка в реальном времени, что нужно прямо сейчас
        self.non_current_animation = []  # Отрисовка отложена
        self.animation_speed = Env.animation_speed

        self.update_time = 30 // Env.animation_speed
        self.current_time = 0

    def add_effect(self, effect, temp=False):
        if not temp:
            self.current_animation.append(effect)
            return
        self.non_current_animation.append(effect)

    def remove_effect(self, effect):
        self.game.manager.animation.current_animation.remove(effect)

    def update_frames(self):
        if not self.game.manager.overlay.check_pause():
            self.current_time += 1
            if self.current_time == self.update_time:
                for ship in self.game.manager.objects.ships.values():
                    ship.animation.update_sprite()
                self.current_time = 0

    def rescale_sprites(self):
        for ship in self.game.manager.objects.ships.values():
            ship.animation.reload_pull()

    def render(self):
        self.update_frames()
        if not self.game.manager.overlay.check_pause():
            for animation in self.current_animation:
                animation.update()
        for animation in self.current_animation:
            animation.draw()
