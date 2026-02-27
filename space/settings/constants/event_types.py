from enum import Enum

from space.battle.events.either.changed_events.UI.pointed_ship_changed import PointedShipChanged
from space.battle.events.either.changed_events.UI.pointed_ship_changed_raw import PointedShipChangedRaw
from space.battle.events.either.changed_events.core.selected_move_changed import SelectedMoveChanged
from space.battle.events.either.changed_events.gameplay.selected_ship_changed import SelectedShipChanged
from space.battle.events.either.changed_events.UI.selected_ship_changed_raw import SelectedShipChangedRaw
from space.battle.events.either.changed_events.gameplay.settings_panel_changed import SettingsPanelChanged
from space.battle.events.either.ship_events.ship_damaged import ShipDamaged
class EventTypes(Enum):
    ship_damaged = ShipDamaged

    selected_ship_changed = SelectedShipChanged
    selected_move_changed = SelectedMoveChanged
    selected_ship_changed_raw = SelectedShipChangedRaw
    pointed_ship_changed = PointedShipChanged
    pointed_ship_changed_raw = PointedShipChangedRaw
    settings_panel_changed = SettingsPanelChanged

