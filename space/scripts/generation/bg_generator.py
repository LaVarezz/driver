from space.engine.debug.logs.main_log import log_info, log_warning
from space.game_objects.images.bgs.bg import Background
from space.ui.animations.animation import Animation
from space.settings.settings.main_settings.env import Env


def create_bg(self):
    if not Env.optimize_mode:
        ct = self.manager.container
        if not ct.hasbox('backgrounds'):
            bg = Background(self)
            bg.sprites, bg.sprites_original = self.manager.downloader.download_background(bg)
            eff = Animation(bg, self, False)
            self.manager.animation.add_effect(eff)
            bg.animation = eff

            self.manager.images.bg = bg

            ''' кеширование '''
            ct.add_box('backgrounds', [bg.sprites, bg.sprites_original])
            ct.add_box('backgrounds_animation', eff)

            log_info('Фон загружен')
        else:
            bg = Background(self)
            bg.sprites, bg.sprites_original = ct.get_box('backgrounds')
            eff = ct.get_box('backgrounds_animation')[0]
            eff.set_object(bg)
            self.manager.animation.add_effect(eff)
            bg.animation = eff

            self.manager.images.bg = bg

            log_info('Фон загружен из кеша')
    else:
        log_warning('Фон не загружен!')
