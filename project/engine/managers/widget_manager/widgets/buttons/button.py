from project.engine.managers.widget_manager.widgets.basic_widget import BasicWidget


class Button(BasicWidget):
    def __init__(self, main, cords, size, text, command, visible=True, enabled=True):
        super().__init__(main, cords, size, visible, enabled)
        self.command = command
        self.text = text

    def __call__(self):
        self.command(self.main, self.id)

    def update(self):
        pass

    def draw(self, window):
        if self.visible:
            window.blit(self.surface, self.rect)

    def process(self):
        self()

    def __repr__(self):
        return f'Button with text: {self.text}'