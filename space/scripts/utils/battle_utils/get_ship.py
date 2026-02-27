from space.settings.protocols.protocols import MainLike


def get_object(main: MainLike, id):
        return main.manager.objects.get_object(id)