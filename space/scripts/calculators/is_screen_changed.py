from space.scripts.utils.battle_utils.recount_ships_surfases import recount_ships_surfaces


def is_screen_changed(game):
    flag = False

    if game.main.manager.camera.camera_x != game.main.manager.camera.old_camera_x or game.main.manager.camera.camera_y != game.main.manager.camera.old_camera_y or game.main.manager.camera.zoom != game.main.manager.camera.old_zoom:
        flag = True

    game.main.manager.camera.old_camera_x = game.main.manager.camera.camera_x
    game.main.manager.camera.old_camera_y = game.main.manager.camera.camera_y
    game.main.manager.camera.old_zoom = game.main.manager.camera.zoom
    recount_ships_surfaces(game.main.manager.objects.ships.values())

    return flag
