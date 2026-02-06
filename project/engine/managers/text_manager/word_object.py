from pygame import Surface, Rect


class WordObject:
    def __init__(self, word, font, delta=1):
        self._word = word
        self._font = font

        self._delta = delta

        self._size_x = 0
        self._size_y = 0

        self.letters = []

        pos_x = 0

        for symbol in word:
            surf = self._font[symbol]
            px, py = surf.get_size()
            self._size_x += px + self._delta
            self._size_y = max(self._size_y, py)

            self.letters.append([surf, Rect(pos_x, 0, px, py)])
            pos_x += px + self._delta


        self._surface = Surface((self._size_x, self._size_y))
        self._rect = None

        self._ready_to_render = False

    def end_setup(self, position):
        self._ready_to_render = True
        x, y = position
        self._rect = Rect(x, y, self._size_x, self._size_y)

    def update(self):
        pass

    def draw(self, window):
        if self._ready_to_render:
            for letter in self.letters:
                self._surface.blit(letter[0], letter[1])
            window.blit(self._surface, self._rect)


    def get_length(self):
        return self._size_x

    def get_height(self):
        return self._size_y

    def __repr__(self):
        return f'"{self._word}" txt.obj'
