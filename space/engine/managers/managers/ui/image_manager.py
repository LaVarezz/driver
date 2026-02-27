from random import randrange

from space.game_objects.images.bgs.bg import Background


class ImageManager:
    def __init__(self, main):
        self.main = main
        self.images = {
            0: [],
            1: [],
            2: [],
            3: [],
            4: [],
        }

    def add_image(self, image, layer):
        self.images[layer].append(image)

    def kill_image(self, image, layer):
        self.images[layer].remove(image)

    def update(self):
        for line in self.images.values():
            for image in line:
                image.update()

    def draw(self):
        for line in self.images.values():
            for image in line:
                image.draw(self.main.window)



    def __repr__(self):
        return 'Images manager'

