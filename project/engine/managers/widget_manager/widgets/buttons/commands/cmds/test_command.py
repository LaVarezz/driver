from project.data.protocols.protocols import MainLike


def test_command(main:MainLike, button_id):
    print('command is ok!')
    main.manager.widget_manager.get_widget(button_id).surface.fill('red')