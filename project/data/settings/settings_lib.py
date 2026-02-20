from project.data.settings.game_settings.game_settings import GameSettings
from project.data.settings.open_settings.open_settings import OpenSettings
from project.data.settings.state_settings.state_settings import StateSettings


class SettingsLib:
    def __init__(self):
        self.open_settings = OpenSettings()
        self.state_settings = StateSettings()
        self.game_settings = GameSettings()
