
from space.settings.protocols.protocols import ShipLike


def damage(ship: ShipLike, damage: int):
    ship.health -= 1000
