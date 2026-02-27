''' Определяет, находится ли объект в поле зрения игрока. Возвращает True/False '''
from space.settings.protocols.protocols import Rentable, HasMain

enabled = False
def check_if_object_on_screen(object: Rentable, game) -> bool:
    if enabled:
        size = game.bs.field_size * game.main.manager.camera.zoom
        px = round(game.bs.padx - game.main.manager.camera.camera_x * game.main.manager.camera.zoom)
        py = round(game.bs.pady - game.main.manager.camera.camera_y * game.main.manager.camera.zoom)
        if px + 10 * size < game.main.ws.WIDTH:
            ox = game.main.ws.WIDTH - px - 10 * size
        else:
            ox = 0
        if py + 10 * size < game.main.ws.HEIGHT:
            oy = game.main.ws.WIDTH - py - 10 * size - 200
        else:
            oy = 0
        if px < 0:
            px = 0
        if py < 0:
            py = 0

        total_cells_x = game.main.ws.WIDTH - px - ox
        total_cells_x //= size
        total_cells_x += 1
        if total_cells_x > 10:
            total_cells_x = 10

        total_cells_y = game.main.ws.HEIGHT - py - oy
        total_cells_y //= size
        total_cells_y += 1

        if total_cells_y > 10:
            total_cells_y = 10

        if (total_cells_y - 1) * size + oy < object.y * size or oy + (10 - object.y - 1) * size > game.main.ws.HEIGHT:
            return False
        if (total_cells_x - 1) * size + ox < object.x * size or ox + (10 - object.x - 1) * size > game.main.ws.WIDTH:
            return False
        return True
    else:
        return True