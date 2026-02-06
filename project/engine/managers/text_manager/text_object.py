from pygame.draw import lines
from pygame.examples.midi import output_main

from project.engine.managers.text_manager.word_object import WordObject


class TextObject:
    def __init__(self, cords, length, text, font, size, outpost=10, delta=1, center=(0, 0)):
        self.text = text
        self.font = font
        self.size = size
        self.x, self.y = cords
        self.lx, self.ly = length
        self.cx, self.cy = self.x, self.y

        self.lines = []

        self.delta = delta
        self.outpost = outpost
        self.center = center
        self.setup()

    def setup(self):
        words = []
        for element in self.text.split():
            words.append(WordObject(element, self.font, self.delta))

        self.wrap(words)
        self.layout()


    def wrap(self, unsorted):
        length = 0
        line = []
        ''' если прокатит в одну строчку'''
        if self.count_max_len(unsorted, self.lx):
            self.lines.append(unsorted)
            return self.lines
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
                        return self.lines

    def layout(self):
        x, y = self.x, self.y
        my = 0
        for line in self.lines:
            for word in line:
                word.end_setup((x, y))
                x += word.get_length()
                my = max(my, word.get_height())
                x += self.outpost
            y += my
            x = self.x


    @staticmethod
    def count_max_len(words, length):
        return sum([i.get_length() for i in words]) <= length

    def update(self):
        pass

    def draw(self, window):
        for line in self.lines:
            for word in line:
                word.draw(window)
