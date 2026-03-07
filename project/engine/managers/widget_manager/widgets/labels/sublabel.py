from project.data.protocols.protocols import MainLike


class Sublabel:
    def __init__(self, main: MainLike, path):
        self.main = main
        self.path = path
        self.value = str(round(self.main.get_parameter(self.path), 2))

    def update(self):
        self.value = str(round(self.main.get_parameter(self.path), 2))



    def __repr__(self):
        return f'sublabel with value: {self.value}'
