'''
Принимает на вход текстовое поле вида text~SUBSCRIBER~text
'''
import pygame as pg

from space.battle.events.either.listeners.text_listener import TextListener


class TextObject:
    def __init__(self, main, text: tuple | list, font):
        self.main = main
        self.text_markers = text
        self.text_data = text
        self.font = font

        self.update_text()

    def update_text(self):
        ''' Рендерит surface, уже готовый для отрисовки. '''
        ready = []

        for element in self.text_markers:
            if isinstance(element, TextListener):
                e = element.use_format()
                for line in e:
                    ready.append(line)
            else:
                ready.append(element)
        self.text_data = ready

        text_lines = self.get_text_list()
        outpost = self.font.get_size('A')[1]
        px, py = 0, outpost,
        px_max = 0

        lines = []

        for line in text_lines:
            if line == '\n':
                px = 0
                py += outpost
                size = (0, 0)
            else:
                size = self.font.get_size(line)
                px += size[0]
                if px_max < px: px_max = px
                py += size[1]
            lines.append((line, size))

        self.surface = pg.surface.Surface((2+px_max, 2+py))
        ox = oy = 5

        for line in lines:
            if '\n' not in line[0]:
                self.font.render_text(line[0]).draw(self.surface, (ox, oy))
                ox += line[1][0]
            else:
                ox = 5
                oy += outpost

    def get_text_list(self):
        text = self.text_data
        lines = []

        for element in text:
            line = ''
            line += str(element)
            line += ' '
            lines.append(line)
        return lines



    def __repr__(self):
        return f'TextObject: {self.text_data}'
