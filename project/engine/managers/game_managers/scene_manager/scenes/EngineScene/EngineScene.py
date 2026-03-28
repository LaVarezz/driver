from project.data.protocols.protocols import MainLike


class EngineScene:
    def __init__(self, main: MainLike):
        self.main = main
        self.name = "engine_scene"

    def setup(self):
        pass

    def update(self):
        if self.main.manager.engine_manager.able_to_change:
            if self.main.manager.widget_manager.hovered_id and self.main.manager.widget_manager.hovered_id == self.main.manager.widget_manager.captured_id:
                widget = self.main.manager.widget_manager.get_widget(self.main.manager.widget_manager.hovered_id)
                dx, dy = self.main.cursor.get_mouse_states()[2]
                if self.can_replace_widget(widget, dx, dy):
                    widget.replace(dx, dy)


    def can_replace_widget(self, widget, dx, dy):
        if not widget.panel:
           wg = self.main.settings.open_settings['width']
           hg = self.main.settings.open_settings['height']
           ''' рассчеты для беспанельных виджетов '''
        else:
           pan = self.main.manager.widget_manager.get_widget(widget.panel)
           wg = pan.width
           hg = pan.height

        return (0 <= widget.x + dx <= wg - widget.width) and (0 <= widget.y + dy <= hg - widget.height)

    def draw(self):
        pass

    def kill_scene(self):
        pass

    def __repr__(self):
        return 'MAIN SCENE'
