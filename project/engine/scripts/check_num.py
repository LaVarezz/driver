''' Колян сука, функция работает, не лезь в это дерьмо '''

def is_num(num: str) -> {0, 1, 2}:
    '''
    проверяет, возможно ли перевести строку в число
    Принимает: строку num
    Возвращает:
    [0] - строка не является числом
    [1] - стркоа является int
    [2] - строка является float
    '''

    dot_count = 0
    minus_count = 0
    result = 0
    alp = [i for i in num]
    for element in alp:
        if element == '.': dot_count += 1
        elif element == '-': minus_count += 1
        elif element in '0123456789':
            continue
        else:
            return result
    if num == '-': return result

    if minus_count == 1:
        if alp[0] != '-': return result
        if num != '-0':
            if alp[1] == '0': return result
    elif minus_count == 0:
        if num != '0':
            if alp[0] == '0': return result

    #постобработка
    if dot_count <= 1 and minus_count <= 1:
        if dot_count == 1:
            result += 1
        result += 1


        return result

    else:
        return result


test = True
if test:
    if not is_num('000'): print('Тест #1 пройден')
    if not is_num('-000'): print('Тест #2 пройден')
    if not is_num('0.00'): print('Тест #3 пройден')
    if not is_num('01.00'): print('Тест #4 пройден')
    if not is_num('--0100'): print('Тест #5 пройден')
    if is_num('0'): print('Тест #6 пройден')
    if is_num('105.3'): print('Тест #7 пройден')
    if is_num('-1105.3'): print('Тест #8 пройден')
    if not is_num('-110.5.3'): print('Тест #9 пройден')