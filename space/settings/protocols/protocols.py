from typing import Protocol, Any

import pygame.surface
from pygame import display, time

from space.engine.managers.managers.ui.camera_manager import CameraControl


class Rentable(Protocol):
    x: int
    y: int

    def update(self):
        pass

    def draw(self):
        pass


class HasFont(Protocol):
    font: Any


class HasGame(Protocol):
    game: Any

class HasMain(Protocol):
    main: Any

class HasRect(Protocol):
    rect: Any


class ShipLike(Rentable, HasFont, HasGame):
    side: int
    health: int
    damage: int
    length: int
    move_points: int
    ship_weight: int
    ship_tonnage: str

    text_hp: Any
    text_id: Any

    id: int

    surface: pygame.surface.Surface
    rect: pygame.rect.Rect

    def death(self):
        pass


class CellLike(Rentable, HasFont, HasRect):
    absolute_x: int | float
    absolute_y: int | float
    cell_size: int

    text_cords: Any

    kx: int
    ky: int

    game: 'game object'

    content: int


class MainLike():
    scenes_pull: dict
    binds: dict

    scene: Any
    ws: Any
    window: display.set_mode
    clock: time.Clock
    manager: Any

    settings: Any

    cursor: Any
    mouse_pos: tuple


    def change_scene(self, scene):
        pass

    def mainloop(self):
        pass

    def reset_managers(self):
        pass


class BattleLike():
    camera: CameraControl


class SceneLike(BattleLike):
    main: MainLike
    title: str

    def scene_loop(self):
        pass

    def kill_scene(self):
        pass

    def setup(self):
        pass


class ManagerLike():
    animation: Any
    overlay: Any
    objects: Any
    container: Any
    downloader: Any
    widgets: Any
    camera: Any
    statistic: Any
    events: Any
