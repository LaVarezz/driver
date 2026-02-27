'''
Набор биндов для боевого состояния.
'''

import pygame as pg

from space.settings.constants.battle_constants import TurnPhase

binds = {}


def on_key(key):
    def binding(func):
        ''' Присваивает функцию бинду '''
        binds[key] = func
        return func

    return binding


''' Бинды на мышь '''

''' Нажатие '''


@on_key(pg.MOUSEBUTTONDOWN)
def mouse_down_click(self):
    self.mouse_state = pg.mouse.get_pressed()
    self.mouse_pos = pg.mouse.get_pos()
    if self.mouse_state[0]:
        lkm_down(self)


def lkm_down(self):
    cell = self.main.manager.cursor.cell
    if cell:
        self.main.manager.clicks.cell = cell
        self.main.manager.clicks.set_state(self.main.manager.cursor.selecting_state)
    else:
        self.main.manager.widgets.activate_widget(self.mouse_pos)


''' Удержание '''


@on_key('drag')
def mouse_down_drag(self):
    self.mouse_state = pg.mouse.get_pressed()
    self.mouse_pos = pg.mouse.get_pos()
    if self.mouse_state[1]:
        skm_down(self)


def skm_down(self):
    if not self.main.manager.overlay.check_pause():
        dx = -(self.main.mouse_pos[0] - self.main.mouse_old_pos[0]) // self.main.manager.camera.zoom
        dy = -(self.main.mouse_pos[1] - self.main.mouse_old_pos[1]) // self.main.manager.camera.zoom

        self.main.manager.camera.camera_x += dx
        self.main.manager.camera.camera_y += dy


def pkm_down(self):
    pass


@on_key(pg.MOUSEBUTTONUP)
def mouse_down(self):
    self.main.manager.widgets.deactivate_widgets()


''' Бинды на кнопки '''


@on_key(pg.K_RETURN)
def phase_turner(self):
    self.turn_phase = TurnPhase.END_TURN


@on_key(pg.K_ESCAPE)
def switch_parameters_panel(self):
    if self.settings_panel:
        self.main.manager.events.emit('settings_panel_changed', None, True, object=None)
    else:
        self.main.manager.events.emit('settings_panel_changed', None, True, object=None)


@on_key(pg.K_TAB)
def switch_control_panel(self):
    if self.control_panel:
        self.main.manager.cursor.select_ship(None)
        self.control_panel.kill_panel()


''' Тестовый режим '''


@on_key(pg.K_t)
def switching_test_mode(self):
    self = self.main
    ''' Отображение тестового режима '''
    if self.test_mode.show_debug_ui:
        self.test_mode.show_debug_ui = False
    else:
        self.test_mode.show_debug_ui = True


@on_key(pg.K_1)
def switching_show_fps(self):
    self = self.main
    if self.test_mode.show_fps:
        self.test_mode.show_fps = False
    else:
        self.test_mode.show_fps = True


@on_key(pg.K_2)
def switching_show_id(self):
    self = self.main
    if self.test_mode.show_id:
        self.test_mode.show_id = False
    else:
        self.test_mode.show_id = True


@on_key(pg.K_3)
def switching_show_grid_position(self):
    self = self.main
    if self.test_mode.show_grid_position:
        self.test_mode.show_grid_position = False
    else:
        self.test_mode.show_grid_position = True


@on_key(pg.K_4)
def switching_show_hp(self):
    self = self.main
    if self.test_mode.show_hp:
        self.test_mode.show_hp = False
    else:
        self.test_mode.show_hp = True


@on_key(pg.K_5)
def switching_show_collides(self):
    self = self.main
    if self.test_mode.show_collides:
        self.test_mode.show_collides = False
    else:
        self.test_mode.show_collides = True
