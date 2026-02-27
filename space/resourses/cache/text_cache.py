'''
TextCache - Кеширует все буквы в surface
TextObject - Рендерит получившуюся строку
Дает отличный выигрыш по кадрам в случае постоянного рендера
'''
import pygame as pg

un_test = False  # Флаг теста


class TextCache:
    def __init__(self, font_size=24, color='White'):
        pg.init()
        self.font_size = font_size
        self.color = color
        self.alphabet = set(
            "1234567890- =QWERTYUIOP+ё[]A!\nSDFGHJKL;:()<>_'ZXCVBNM,.\в/qwertyuiop[asdfghjkl;'zxcvbnm,./йцукенгшщзхъфывапролджэячсмитьбю.ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ")
        self.font = pg.font.Font('resourses/fonts/font_zero.ttf', self.font_size)  # пока такой шрифт.
        self.rendered_alphabet = {}
        for letter in self.alphabet:
            self.rendered_alphabet[letter] = (self.font.render(letter, 1, self.color), self.font.size(letter))

        self.line_height = False

    def get_size(self, text):
        x = 0
        y = 0
        for symbol in str(text):
            x += self.rendered_alphabet[symbol][0].get_width()
            y = self.rendered_alphabet[symbol][0].get_height()
        return x, y

    def render_text(self, text: str):
        current_len = 0
        text = text

        text_list = list()

        for letter in text:
            ''' Символ, координата'''
            text_list.append((self.rendered_alphabet[letter][0], current_len))
            current_len += self.rendered_alphabet[letter][1][0]
        return TextObject(text_list)


class TextObject():
    def __init__(self, text_list):
        self.text_list = text_list

    def draw(self, wnd, start_pos):
        for pack in self.text_list:
            letter = pack[0]
            pos = pack[1]
            wnd.blit(letter, (start_pos[0] + pos, start_pos[1]))


if un_test:
    t = TextCache(24, 'White')
    window = pg.display.set_mode((300, 300))
    rendered = False
    f = True
    while f:
        if not rendered:
            rendered = True
            text = t.render_text('Тут текст ляляа2123++1ё.м ')
        text.draw(window, (10, 10))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                f = False

        pg.display.update()
