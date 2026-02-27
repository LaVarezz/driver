import pygame as pg


def get_screen_position(object: 'positionable obj'):
    x0, y0 = get_pixel_position(object)
    size = get_scaled_position(object.game)
    return x0, y0, size, size

def get_cell_rect(cell: 'cell obj', outpost=0):
    return pg.rect.Rect(cell.screen_x+outpost, cell.screen_y+outpost, cell.size-outpost*2, cell.size-outpost*2)

def get_cell_py_cords(cords, game):
    return game.main.manager.objects.cells[cords[0]][cords[1]]

def get_pixel_position(object: 'Positionable obj', center=False):
    x = (object.x * object.game.bs.field_size - object.game.main.manager.camera.camera_x) * object.game.main.manager.camera.zoom + object.game.bs.padx
    y = (object.y * object.game.bs.field_size - object.game.main.manager.camera.camera_y) * object.game.main.manager.camera.zoom + object.game.bs.pady
    if center:
        offset = object.game.bs.field_size * object.game.main.manager.camera.zoom / 2
        return x+offset, y+offset
    return x, y

def get_grid_position(object, return_cell=False):
    return (object.x, object.y) if not return_cell else get_cell_py_cords(object.get_cords(), object.game)

def get_scaled_position(game):
    return game.bs.field_size * game.main.manager.camera.zoom


