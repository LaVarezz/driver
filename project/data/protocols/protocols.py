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
    widget_id = int

    def update(self): ...

    def draw(self, window): ...


class EventBusLike(Protocol):
    def subscribe(self, listener: HasTrigger, event_type: EnumLike) -> None: ...

    def unsubscribe(self, listener: HasTrigger, event_type: EnumLike | None = None) -> None: ...

    def emit(self, msg: EnumLike, data: dict) -> None: ...

    def current_len(self) -> int: ...

    def next_len(self) -> int: ...


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
    def create_widget(self, widget: WidgetLike, layer: int) -> None: ...

    def remove_widget(self, widget_id: int) -> None: ...

class SettingsLike(Protocol):
    open_settings: dict
    state_settings: dict
    game_settings: dict

class MainLike(Protocol):
    main_manager: MainManagerLike
    settings: SettingsLike


class MainManagerLike(ManagerLike, Protocol):
    window_manager: WindowManagerLike
    input_manager: InputManagerLike
    scene_manager: SceneManagerLike
    time_manager: TimeManagerLike
    widget_manager: WidgetManagerLike

