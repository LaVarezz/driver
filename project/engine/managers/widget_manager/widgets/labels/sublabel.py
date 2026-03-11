from project.data.protocols.protocols import MainLike
from project.engine.scripts.check_num import is_num


class Sublabel:
    def __init__(self, main: MainLike, path):
        self.main = main
        self.path = path
        self.update()

    def update(self):
        ''' В зависимости от того, можно ли превратить исходную строку в число или нет, делает этого. (см is_num) '''
        val = str(self.main.get_parameter(self.path))
        var = is_num(val)
        if var != 0:
            if var == 2:
                self.value = str(round(float(val), 2))
            else:
                self.value = str(round(int(val), 2))
        else:
            self.value = val



    def __repr__(self):
        return f'sublabel with value: {self.value}'
