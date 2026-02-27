from space.game_objects.images.image import Image
from space.settings.constants.battle_constants import Types
from space.settings.constants.ship_constants import States
from space.settings.protocols.protocols import MainLike

class Background(Image):
    def __init__(self, main: MainLike):
        ws = main.ws
        super().__init__((0, 0), (ws.WIDTH, ws.HEIGHT), main, 0)

        self.sprites = {}

        self.animation = None
        self.direction = None
        self.is_visible = True

        self.type = Types.IMAGE
        self.state = States.IDLE


    def __repr__(self):
        return 'Background object'