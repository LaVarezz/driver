''' Обьект контейнера - для хранения параметров или файлов '''


class Container:
    def __init__(self, game):
        self.game = game
        self.boxes = {}

    def add_box(self, index, value, delete=False):
        if index not in self.boxes.keys():
            if isinstance(value, list):
                self.boxes[index] = value
            else:
                self.boxes[index] = [value]
        else:
            if not delete:
                self.boxes[index].append(value)
            else:
                del self.boxes[index][value]

    def hasbox(self, index):
        return index in self.boxes.keys()

    def get_box(self, index):
        if index in self.boxes.keys():
            return self.boxes[index]

    def delete_box(self, index):
        if index in self.boxes.keys():
            del self.boxes[index]

    def __repr__(self):
        return 'Container'
