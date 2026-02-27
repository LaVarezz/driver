from space.settings.protocols.protocols import ManagerLike


class Manager(ManagerLike):
    def __int__(self, main):
        self.main = main