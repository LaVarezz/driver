from pygame import Surface, Rect, SRCALPHA

from project.engine.managers.text_manager.word_object import WordObject




class TextObject:
    def __init__(self, cords, length, text, window, font, size, outpost=10, delta=1, center=(0, 0)):
        self.text = text
        self.font = font
        self.size = size
        self.x, self.y = cords
        self.lx, self.ly = length
        self.cx, self.cy = self.x, self.y
        self.window = window

        self.lines = []

        self.surface = Surface((self.lx, self.ly), SRCALPHA)
        self.surface.set_colorkey('black')
        self.rect = Rect(self.x, self.y, self.lx, self.ly)

        self.delta = delta
        self.outpost = outpost
        self.center = center
        self.setup()

    def setup(self):
        ''' Вызывается единожды при создании объекта. Является первой ступенью обработки. Разбивает текст на слова и превращает их в слова-объекты. см. word_object '''
        words = []
        for element in self.text.split():
            words.append(WordObject(element, self.font, self.delta))

        self.wrap(words)
        self.layout()

    def wrap(self, unsorted):
        '''
        Разбивает слова на линии в соответствии с размерами этих слов.
        '''
        length = 0
        line = []
        ''' если прокатит в одну строчку'''
        if self.get_max_len(unsorted, self.lx):
            self.lines.append(unsorted)
            return
        else:
            for word in unsorted[:]:
                px = word.get_length()
                if length + px + self.outpost < self.lx:
                    ''' если слово еще влезает в строчку'''
                    line.append(word)
                    length += px + self.outpost
                    if unsorted:
                        unsorted.pop(0)
                else:
                    ''' если нет '''
                    self.lines.append(line)
                    if unsorted:
                        return self.wrap(unsorted)
                    else:
                        return

    def layout(self):
        ''' Вызывается единожды. Рассчитывает точные положения слов внутри строки. '''
        y = 0
        for line in self.lines:
            my = 0
            x = 0
            for word in line:
                word.end_setup((x, y))
                x += word.get_length()
                print(x, y)
                my = max(my, word.get_height())
                x += self.outpost
            y += my
            x = self.x

        self.to_center()

    def to_center(self):
        ''' Последний этап обработки. Центрирует объект при необходимости. завершает обработку внутри слова. '''
        center_x, center_y = self.center

        if center_x:
            for line in self.lines:
                dx = (self.lx - self.get_len(line)) // 2
                for word in line:
                    word.post_setup((dx, 0))
        else:
            for line in self.lines:
                for word in line:
                    word.post_setup((0, 0))

    def get_max_len(self, words, length):
        return sum([i.get_length() for i in words]) + self.outpost * (len(words) - 1) <= length

    def get_len(self, line):
        return sum([i.get_length() for i in line]) + self.outpost * (len(line) - 1)

    def update(self):
        pass

    def draw(self):
        for line in self.lines:
            for word in line:
                word.draw(self.surface)
        self.window.blit(self.surface, self.rect)


