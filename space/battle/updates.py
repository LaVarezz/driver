import pygame as pg

from space.scripts.calculators.is_screen_changed import is_screen_changed
from space.ui.debug.debug_render import debug_show_fps


def update_visual_info(self):
    self.has_camera_changed = is_screen_changed(self)
    update_all_mode(self.main)


def update_all_mode(main):
    main.window.fill('black')
    main.manager.images.update()
    main.manager.images.draw()

    main.manager.objects.update()
    main.manager.objects.draw()

    if main.test_mode.show_debug_ui:
        if main.test_mode.show_fps:
            debug_show_fps(main)

    main.manager.animation.render()
    main.manager.widgets.update_UI()
    main.manager.widgets.draw_UI(main.window)
    main.manager.overlay.update_overlay_UI()
    main.manager.overlay.draw_overlay_UI()

    main.manager.cursor.update()
    main.manager.cursor.draw()

    pg.display.update()

    main.clock.tick(main.ws.FPS)
