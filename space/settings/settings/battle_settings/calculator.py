def calculator_field_size(HEIGHT: int, BATTLEFIELD_SIZE_Y: int):
    ''' Размер каждой клетки поля боя - в пикселЯх '''
    return (HEIGHT - 200) // BATTLEFIELD_SIZE_Y

def calculator_max_size(field_size: int):
    ''' Размер каждой клетки поля боя - в пикселЯх, пока что ничего не меняет, гы)'''
    return field_size

def calculator_battlefield_from_left(WIDTH: int, field_size: int, BATTLEFIELD_SIZE_X: int):
    ''' Отступ поля боя от края экрана '''
    return (WIDTH - field_size * BATTLEFIELD_SIZE_X) // 2
