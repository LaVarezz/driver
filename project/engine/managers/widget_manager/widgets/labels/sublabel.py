from project.data.protocols.protocols import MainLike


class Sublabel:
    def __init__(self, main: MainLike, path):
        self.main = main
        self.path = path
        self.value = str(self.main.get_parameter(self.path))

    def update(self):
        self.value = str(self.main.get_parameter(self.path))


    def __repr__(self):
        return f'sublabel with value: {self.value}'
