from project.engine.managers.widget_manager.widgets.basic_widget import BasicWidget


class Button(BasicWidget):
    def __init__(self, cords, size, text, command, visible=True, enabled=True):
        super().__init__(cords, size, visible, enabled)
        self.command = command
        self.text = text

    def __call__(self, data):
        self.command(data)

    def update(self):
        pass

    def draw(self, window):
        if self.visible:
            window.blit(self.surface, self.rect)