from project.data.protocols.protocols import MainLike


def test_command(main: MainLike, data):
    print('command is ok!')
