import pygame as pg

import project.data.protocols.protocols as protocols
from project.engine.managers.basic_manager import Manager
from project.engine.managers.text_manager.text_object import TextObject


class TextManager(Manager, protocols.ManagerLike):
    '''
    Создает, управляет и удаляет блоки текста.
    из функций:
    - кеширование текста
    - центрирование текстового блока
    '''

    def __init__(self, main: protocols.MainLike):
        super().__init__()
        self._fonts = {}
        self._objects = []
        self._sizes = []


    def setup(self, data: protocols.SettingsLike) -> None:
        ''' кеширует алфавит в словари '''
        alp = '1234567890-=*qwertyuiopasdfghjklzxcvbn:mйцукенгшщзхъфывапролджэячсмитьбю.,_ QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ'
        for size in data.game_settings['text_sizes']:
            d = {}
            font = pg.font.SysFont('Arial', size)
            for unrendered_symbol in alp:
                rendered_symbol = font.render(unrendered_symbol, True, (255, 255, 255))
                d[unrendered_symbol] = rendered_symbol
            self._fonts[size] = d
            self._sizes.append(size)

    def create_text_object(self, cords: tuple, length: tuple, window, text: str, size_index: int, outpost=10, delta=1,
                           center=(0, 0), static=True):
        ''' создает блок текста. дальнейшая логика внутри text_object '''
        real_size = self._sizes[size_index]
        obj = TextObject(cords, length, text, window, self._fonts[real_size], real_size, outpost, delta, center)
        self._objects.append(
            obj)
        return obj

    def remove_text_object(self, obj):
        if obj in self._objects:
            self._objects.remove(obj)


    def update_text_objects(self):
        for obj in self._objects:
            obj.update()

    def draw_text_objects(self):
        for obj in self._objects:
            obj.draw()


test = False
if test:
    ''' небольшей тест на работоспособность '''

    pg.init()

    window = pg.display.set_mode((500, 300))


    class set:
        def __init__(self):
            self.game_settings = {
                "text_sizes": [12, 18, 24, 30, 60]
            }


    class main(protocols.MainLike):
        def __init__(self):
            self.settings = set()


    main = main()
    tm = TextManager(main)
    tm.setup(main.settings)
    tm.create_text_object((30, 50), (300, 150), window, '111 222 333 444 555 666 777 888 999', 3, 10, center=(0, 0))

    run = True
    while run:
        window.fill('blue')

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
        tm.update_text_objects()
        tm.draw_text_objects()

        pg.display.update()
