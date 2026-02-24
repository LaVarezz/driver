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
                if widget.x + dx >= 0:
                    if widget.x + dx + widget.width < self.main.manager.widget_manager.get_widget(widget.panel).width:

                widget.replace(dx, dy)


    def draw(self):
        pass

    def kill_scene(self):
        pass

    def __repr__(self):
        return 'MAIN SCENE'
