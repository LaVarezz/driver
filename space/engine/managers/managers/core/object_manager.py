from random import randrange

from space.engine.debug.logs.main_log import log_info
from space.scripts.calculators.is_object_on_screen import check_if_object_on_screen
from space.settings.constants.battle_constants import Types
from space.settings.settings.battle_settings.env import Env

''' Класс для работы со всеми обьектами на экране(например, удалить после завершения боя '''


class VisibleObject():
    __slots__ = ('objects', 'main', 'ships', 'cells', 'player_ships', 'enemy_ships', 'void_ships', 'images')

    def __init__(self, main):
        self.player_ships = []
        self.enemy_ships = []
        self.void_ships = []
        self.ships = {}
        self.cells = []
        self.objects = []

        for x in range(Env.field_size[0]):
            temp = []
            for y in range(Env.field_size[1]):
                temp.append([])
            self.cells.append(temp)
        self.main = main

    def add_object(self, obj):
        self.objects.append(obj)
        if obj.type == Types.SHIP:
            if obj.side == 0:
                self.player_ships.append(obj)
            elif obj.side == 1:
                self.enemy_ships.append(obj)
            elif obj.side == 2:
                self.void_ships.append(obj)
            self.ships[obj.id] = obj
        elif obj.type == Types.CELL:
            self.cells[obj.x][obj.y] = obj

    def remove_object(self, obj):
        if obj in self.objects:
            self.objects.remove(obj)
        if obj.type == Types.SHIP:
            if obj.side == 0:
                self.player_ships.remove(obj)
            elif obj.side == 1:
                self.enemy_ships.remove(obj)
            elif obj.side == 2:
                self.void_ships.remove(obj)
            del self.ships[obj.id]


    def get_object(self, id):
        ''' Возвращает обьект по ключу(id). Пока работает только на кораблях! '''
        try:
            obj = self.ships[id]
            return obj
        except:
            print()

    def normalize_object(self, object):
        ''' Возвращает id обьекта или обьект, если обьект уже является id'''
        return object.id if not isinstance(object, str) else object

    def create_id(self, object):
        ''' Создает id для объекта из 12 цифр:
        - корабли: по 2 символа: фракция, класс, тип, номер, 4 рандомные цифры
        - прочие объекты пока не имеют айди.
        но пока 12 рандомных цифр
        '''
        s = ''
        for i in range(12):
            s += str(randrange(0, 10))
        return s

    def get_cell(self, pos):
        if not hasattr(self.main.scene, 'game'):
            return None

        camera = self.main.manager.camera
        bs = self.main.scene.game.bs
        cell_size = int(bs.field_size * camera.zoom)

        # учёт камеры и паддингов
        x = pos[0] - bs.padx + camera.camera_x
        y = pos[1] - bs.pady + camera.camera_y

        dx = x // cell_size
        dy = y // cell_size

        if 0 <= dx < bs.BATTLEFIELD_SIZE_X and 0 <= dy < bs.BATTLEFIELD_SIZE_Y:
            return self.cells[int(dx)][int(dy)]
        return None


    def update_visible_objects(self):
        for obj in self.objects:
            obj.is_visible = check_if_object_on_screen(obj, obj.game)

    def destroy_objects(self):
        self.player_ships = []
        self.enemy_ships = []
        self.void_ships = []
        self.ships = {}
        self.cells = []
        self.objects = []

        log_info('Все обьекты на экране уничтожены... ')

    def update(self):
        if not self.main.manager.overlay.check_pause():
            for obj in self.objects:
                obj.update()

    def draw(self):
        for obj in self.objects:
            if obj.is_visible:
                obj.draw()


class Object:
    def __init__(self, cords, type):
        self.x, self.y = cords
        self.type = type
        self.is_visible = True
