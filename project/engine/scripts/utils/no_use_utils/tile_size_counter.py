def count_tile_size(window_size: tuple|list, tiles:tuple|list, outpost: tuple|list) -> int:
    ''' Утилита возвращает минимальный допустимый размер клетки карты с учетом отступов. '''
    width, height = window_size
    x, y = tiles

    dx = (width-outpost[0]) // x
    dy = height-outpost[1] // y

    return min(dx, dy)