class TextListener:
    def __init__(self, main, frame, configuration):
        self.main = main
        self.frame = frame
        self.configuration = configuration
        self.content = []
        self.parent = self.frame

        self.event = None
        self.sub = None
        self.format = None

    def use_format(self):
        return self.content

    def callback(self, data):
        self.content = self.configuration(data)
        self.parent.text_data.update_text()


    def __repr__(self):
        return f'listener: {self.event}'