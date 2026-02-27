
class PanelListener:
    def __init__(self, main, overlay, panel, configuration):
        self.main = main
        self.overlay = overlay
        self.configuration = configuration
        self.content = []
        self.parent = self.overlay

        self.panel = panel[0]
        self.panel_name = panel[1]

        self.event = None
        self.sub = None
        self.format = None


    def use_format(self):
        return self.content

    def callback(self, data):
        object = data.object
        game = self.main.scene.game
        if object and not getattr(game, self.panel_name):
            m = self.panel(self.main, object)
            setattr(game, self.panel_name, m)
            self.main.manager.overlay.add_widget(m, pause=False)
        else:
            if self.panel_name != 'settings_panel':
                getattr(game, self.panel_name).kill_panel()
                setattr(game, self.panel_name, None)
            else:
                ''' Сугубо для панели оверлей настроек '''
                if getattr(game, self.panel_name):
                    getattr(game, self.panel_name).kill_panel()
                    setattr(game, self.panel_name, None)
                else:
                    m = self.panel(self.main, object)
                    setattr(game, self.panel_name, m)
                    self.main.manager.overlay.add_widget(m, pause=True)

    def __repr__(self):
        return f'listener: {self.event}'