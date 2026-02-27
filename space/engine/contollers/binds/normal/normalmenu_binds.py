import pygame as pg

binds = {}


def on_key(key):
    def binding(func):
        ''' Присваивает функцию бинду '''
        binds[key] = func
        return func

    return binding


''' Бинды на мышь '''


@on_key(pg.MOUSEBUTTONDOWN)
def normal_mouse_down(self):
    self.mouse_state = pg.mouse.get_pressed()
    self.mouse_pos = pg.mouse.get_pos()
    if self.mouse_state[0]:
        lkm_down(self)


def lkm_down(self):
    self.main.manager.widgets.activate_widget(self.mouse_pos)


@on_key(pg.MOUSEBUTTONUP)
def mouse_down(self):
    self.main.manager.widgets.deactivate_widgets()

