from project.data.protocols.protocols import MainLike


class Sublabel:
    def __init__(self, main: MainLike, path):
        self.main = main
        self.path = path
        self.value = str(self.main.get_parameter(self.path))


