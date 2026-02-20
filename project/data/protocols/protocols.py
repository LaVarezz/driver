from __future__ import annotations

from typing import Protocol, Any


class HasTrigger(Protocol):
    def trigger(self, msg: EnumLike, data: dict) -> None: ...


class HasSetup(Protocol):
    def setup(self, data: SettingsLike) -> None: ...


class SceneLike(Protocol):

    def setup(self): ...

    def update(self): ...

    def draw(self): ...

    def kill_scene(self): ...


class EnumLike(Protocol): ...


class ManagerLike(HasSetup, Protocol): ...


class WidgetLike(Protocol):
    x: int
    y: int
    width: int
    height: int
    rect: Any
    surface: Any
    visible: bool
    enabled: bool
    id = int

    def update(self): ...

    def draw(self, window): ...


class EventBusLike(Protocol):
    def subscribe(self, listener: HasTrigger, event_type: EnumLike) -> None: ...

    def unsubscribe(self, listener: HasTrigger, event_type: EnumLike | None = None) -> None: ...

    def emit(self, msg: EnumLike, data: dict) -> None: ...

    def current_len(self) -> int: ...

    def next_len(self) -> int: ...

    def begin_frame(self): ...

    def process_frame(self): ...

    def current_events(self) -> list: ...

    def next_events(self) -> list: ...

    def try_to_get_event(self, event_type) -> list: ...

class CursorLike(Protocol):
    def update_cursor_state(self): ...

    def check_matches(self): ...

    def get_mouse_states(self) -> tuple: ...

class WindowManagerLike(ManagerLike, HasSetup, HasTrigger, Protocol):
    app: Any  # из pygame
    clock: Any  # из pygame
    dt: float
    run: bool


    def update_window(self) -> None: ...


class InputManagerLike(ManagerLike, HasSetup, Protocol):
    def get_inputs(self) -> None: ...


class SceneManagerLike(ManagerLike, Protocol):
    current_scene: SceneLike

    def change_scene(self, scene: SceneLike) -> None: ...


class TimeManagerLike(ManagerLike, Protocol):
    def create_timer(self, start: int | float, duration: int | float, event: EnumLike, data: dict,
                     repeat: bool = False) -> None: ...


class WidgetManagerLike(ManagerLike, Protocol):
    captured_id: int
    hovered_id: int

    def create_widget(self, widget: WidgetLike, layer: int) -> None: ...

    def remove_widget(self, widget_id: int) -> None: ...

    def get_widget(self, id, layer=-1) -> WidgetLike: ...

    def get_all_widgets(self) -> list: ...


class TextManagerLike(ManagerLike, Protocol):
    def create_text_object(self, cords: tuple, length: tuple, window, text: str, size_index: int, outpost=10, delta=1,
                           center=(0, 0)): ...
import json
import os


from project.engine.managers.basic_manager import Manager


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_path():
    p = os.path.join(os.path.dirname(__file__), 'config.json')
    abs = os.path.abspath(p)
    return abs


class EngineManagerLike(Manager):
    able_to_change: bool
    def setup(self, settings: SettingsLike): ...

    def get_config_for_scene(self): ...

    def save_config_for_scene(self): ...



class SettingsLike(Protocol):
    open_settings: dict
    state_settings: dict
    game_settings: dict


class MainLike(Protocol):
    manager: MainManagerLike
    settings: SettingsLike
    events: EventBusLike
    cursor: CursorLike


class MainManagerLike(ManagerLike, Protocol):
    window_manager: WindowManagerLike
    input_manager: InputManagerLike
    scene_manager: SceneManagerLike
    time_manager: TimeManagerLike
    widget_manager: WidgetManagerLike
    text_manager: TextManagerLike
    engine_manager: EngineManagerLike
