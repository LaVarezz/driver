import pygame as pg

from space.engine.debug.logs.main_log import log_info
from space.engine.scenes.scenes.battle_scene import BattleScene
from space.scripts.calculators.get_scripts import get_cell_rect, get_grid_position
from space.scripts.utils.exit import hardcore_exit
from space.scripts.utils.battle_utils.get_ship import get_object
from space.settings.constants.click_constants import ClickStates
from space.settings.constants.ship_constants import States
from space.settings.protocols.protocols import MainLike


class Cursor:
    def __init__(self, main: MainLike):
        try:
            self.main = main
            self.x, self.y = pg.mouse.get_pos()

            self.selected_cell = None
            self.selected_ship = None
            self.targeted_cell = None
            self.pointed_ship = None

            self.selecting_state = ClickStates.SelectShipState

        except Exception as e:
            log_info(f'Ошибка {e} при подключении курсора.')
            hardcore_exit(self.main, e)
            raise e
        else:
            log_info('Курсор подключен успешно')

    def update(self):
        self.x, self.y = pg.mouse.get_pos()
        self.create_quick_info_panel()
        if not self.main.manager.widgets.activate_widget(self.pos):
            self.selected_cell = self.main.manager.objects.get_cell(self.pos)

    def draw(self):
        if self.selected_cell:
            pg.draw.rect(self.main.window, 'blue', get_cell_rect(self.selected_cell), 2)

        if self.ship:
            cell = get_grid_position(get_object(self.main, self.ship), True)
            pg.draw.rect(self.main.window, 'green', get_cell_rect(cell, 2), 4)

    def remove_ship_from_select(self, ship):
        if self.selected_ship == ship:
            self.selected_ship = None
        if self.pointed_ship == ship:
            self.pointed_ship = None


    @property
    def pos(self):
        return self.x, self.y

    @property
    def cell(self):
        return self.selected_cell

    @property
    def ship(self):
        return self.selected_ship

    @property
    def target_cell(self):
        return self.targeted_cell

    def select_ship(self, obj=None):
        if not obj:
            self.selected_ship = self.pointed_ship
        else:
            self.selected_ship = self.main.manager.objects.normalize_object(obj)

    def select_cell(self):
        self.targeted_cell = self.cell

    def reset_cursor_choice(self):
        self.targeted_cell = None
        self.selecting_state = ClickStates.SelectShipState

    def create_quick_info_panel(self):
        if isinstance(self.main.scene, BattleScene):
            cell = self.main.manager.objects.get_cell((self.x, self.y))

            if cell and cell.content:
                if self.pointed_ship != cell.content:
                    self.pointed_ship = cell.content
                    if get_object(self.main, self.pointed_ship).state == States.IDLE:
                        self.main.manager.events.emit('pointed_ship_changed_raw', None, True, object=get_object(self.main, self.pointed_ship))

            else:
                if self.main.scene.game.quick_info_panel:
                    self.main.manager.events.emit('pointed_ship_changed_raw', None, True,
                                                    object=None)
                self.pointed_ship = None


    def __repr__(self):
        return 'Cursor object'

