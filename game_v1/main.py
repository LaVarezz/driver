
import random

import pygame as pg

import game_field
from tools import passer, death, which_field, turner, info, update_objects, check_longth
import GUI

test_mode = 1
stop_the_game = False

def downloader(self):
    ''' изображения '''
    self.image_background = pg.image.load('sprites/game_background_1.png')
    self.image_background = pg.transform.scale(self.image_background, (1400, 1000))
    self.flameshots = [
        pg.image.load('sprites/flameshot/flameshot_1.png'),
        pg.image.load('sprites/flameshot/flameshot_2.png'),
        pg.image.load('sprites/flameshot/flameshot_3.png'),
        pg.image.load('sprites/flameshot/flameshot_4.png'),
        pg.image.load('sprites/flameshot/flameshot_5.png'),
        pg.image.load('sprites/flameshot/flameshot_6.png'),
        pg.image.load('sprites/flameshot/flameshot_7.png'),
        pg.image.load('sprites/flameshot/flameshot_8.png'),
        pg.image.load('sprites/flameshot/flameshot_9.png')
    ]
    self.regenerations = [
        pg.image.load('sprites/regeneration/regen_1.png.'),
        pg.image.load('sprites/regeneration/regen_2.png.'),
        pg.image.load('sprites/regeneration/regen_3.png.'),
        pg.image.load('sprites/regeneration/regen_4.png.'),
        pg.image.load('sprites/regeneration/regen_5.png.'),
        pg.image.load('sprites/regeneration/regen_6.png.'),
        pg.image.load('sprites/regeneration/regen_7.png.'),
        pg.image.load('sprites/regeneration/regen_8.png.'),
        pg.image.load('sprites/regeneration/regen_9.png.'),
        pg.image.load('sprites/regeneration/regen_10.png'),
    ]
    self.blasts = [
        pg.image.load('sprites/blast/strike_01.png'),
        pg.image.load('sprites/blast/strike_02.png'),
        pg.image.load('sprites/blast/strike_03.png'),
        pg.image.load('sprites/blast/strike_04.png'),
        pg.image.load('sprites/blast/strike_05.png')
    ]
    self.slashes = [
        pg.image.load('sprites/slash3/horizonal_slash_01.png'),
        pg.image.load('sprites/slash3/horizonal_slash_02.png'),
        pg.image.load('sprites/slash3/horizonal_slash_03.png'),
        pg.image.load('sprites/slash3/horizonal_slash_04.png'),
        pg.image.load('sprites/slash3/horizonal_slash_05.png')
    ]
    self.rocks = [
        pg.image.load('sprites/rocks/rock1.png'),
        pg.image.load('sprites/rocks/rock2.png'),
        pg.image.load('sprites/rocks/rock3.png'),
        pg.image.load('sprites/rocks/rock4.png'),
    ]
    self.punches = [
        pg.image.load('sprites/punch2/punch_action_01.png'),
        pg.image.load('sprites/punch2/punch_action_01.png'),
        pg.image.load('sprites/punch2/punch_action_01.png'),
        pg.image.load('sprites/punch2/punch_action_01.png'),
        pg.image.load('sprites/punch2/punch_action_02.png'),
        pg.image.load('sprites/punch2/punch_action_02.png'),
        pg.image.load('sprites/punch2/punch_action_03.png'),
        pg.image.load('sprites/punch2/punch_action_03.png'),
        pg.image.load('sprites/punch2/punch_action_04.png'),
        pg.image.load('sprites/punch2/punch_action_04.png'),
        pg.image.load('sprites/punch2/punch_action_05.png'),
        pg.image.load('sprites/punch2/punch_action_05.png'),
        pg.image.load('sprites/punch2/punch_action_06.png'),
        pg.image.load('sprites/punch2/punch_action_06.png'),
    ]
    self.blinks = []
    for i in range(1, 19):
        str = f'sprites/blinks/blink_{i}.png'
        self.blinks.append(pg.image.load(str))
    self.fires = [
        pg.image.load('sprites/fire/fire1.png'),
        pg.image.load('sprites/fire/fire2.png'),
        pg.image.load('sprites/fire/fire3.png'),
        pg.image.load('sprites/fire/fire4.png'),
        pg.image.load('sprites/fire/fire5.png'),
    ]
    self.trees = []
    for i in ['Large Spruce Tree - COLD - 000', 'Slim Spruce Tree - teal - 000']:
        for j in range(1, 10):
            str = f'sprites/trees/{i}{j}.png'
            self.trees.append(pg.image.load(str))
    self.grasses = [
        pg.image.load('sprites/grass/grass-alternative-1.png'),
        pg.image.load('sprites/grass/pond1.png'),
    ]

    self.grasses = [
        pg.image.load('sprites/grass/grass-alternative-1.png'),
        pg.image.load('sprites/grass/pond1.png'),
    ]


class Game:
    def __init__(self):
        pg.init()
        downloader(self)


        ''' параметры окна '''
        self.width, self.height = (1400, 1000)
        self.FPS = 60
        self.size = (min(self.width, self.height) - 100) // 10
        self.font = pg.font.Font('sprites/main_font.otf', 24)
        self.window = pg.display.set_mode((self.width, self.height))
        self.clock = pg.time.Clock()

        ''' логические переменные '''
        self.mouse_pressed = [False, False, False]
        self.new_move = False
        self.step_didnt_do = True

        self.pressed_field = None
        self.pressed_button = None
        self.charge_stop = False
        self.test_mode = test_mode
        self.can_continue = True

        ''' числовые переменные '''
        self.turn = 0
        self.press_timer = 0
        self.outpost = 0
        self.game_time = 0
        self.mover_person = []

        ''' списки '''
        self.fields = []
        self.persons = []
        self.summons = []
        self.creatures = [self.persons, self.summons]
        self.didnt_move = []
        self.already_moved = []
        self.effects = []
        self.status_effects = []
        self.charge_attract = []
        self.objects = []
        self.removed_effects = []



    ''' обработчик скиллов '''
    def click(self):
        if self.can_continue:
            if self.mover_person.move_type == 0 and not self.pressed_field.status and check_longth(self.pressed_field, self.mover_person, self.mover_person.speed, self):
                self.mover_person.movement(self)
            elif self.mover_person.move_type == 1 or (self.mover_person.move_type == 0 and self.pressed_field.status):
                self.mover_person.basic_attack(self)
            elif self.mover_person.move_type == 2:
                self.mover_person.first_skill(self)
            elif self.mover_person.move_type == 3:
                self.mover_person.second_skill(self)
            elif self.mover_person.move_type == 4:
                self.mover_person.third_skill(self)

    ''' конец хода '''
    def end_of_turn(self, person, dead=None):
        for obj in game.objects:
            obj.check_contact()
        for effect in person.status_effects:
            effect.update(self)
        if person.cls in ['Necropet']:
            person.passive_skill(game)
        if dead:
            for d in dead:
                death(d[0], d[1])
        else:
            self.already_moved.append(self.mover_person)
        self.turn += 1
        passer(self)
        game.step_didnt_do = True

    ''' пре-основной цикл '''
    def pre_starter(self):
        self.play = True
        for i in range(-1, 11):
            fields_temporary = []
            for j in range(-1, 11):
                fields_temporary.append(game_field.Field(i, j, self.size, self))
            self.fields.append(fields_temporary)
        for i in self.creatures:
            for j in i:
                j.draw(self)

        ''' игрок и противник '''
        GUI.players(self)
        self.gui = GUI.GUI()

        for i in range(5):
            while True:
                x = random.randrange(0, 10)
                y = random.randrange(0, 10)
                if not self.fields[x][y].status and not self.fields[x][y].object:
                    game_field.Object(x, y, 'Rock', self.fields, self)
                    break

        for i in range(9):
            while True:
                x = random.randrange(0, 10)
                y = random.randrange(0, 10)
                if not self.fields[x][y].status and not self.fields[x][y].object:
                    game_field.Object(x, y, 'Tree', self.fields, self)
                    break

    """ основной цикл """
    def starter(self):
        while self.play:
            ''' сбор данных '''
            self.mouse_x, self.mouse_y = pg.mouse.get_pos()
            self.mouse_press = pg.mouse.get_pressed()
            packed = which_field(self.mouse_press, self.mouse_pressed, self.mouse_x, self.mouse_y, self.size, self.fields)
            if packed:
                self.pressed_field = packed[0]
                self.pressed_button = packed[1]
            if self.pressed_button:
                self.mover_person.move_type = self.pressed_button-1
                self.pressed_button = None

            ''' События раз в ход '''
            if self.step_didnt_do:
                self.mover_person = turner(self)
                if self.mover_person.stun:
                    self.mover_person.stun -= 1
                    self.end_of_turn(self.mover_person)


            ''' обработка кнопок '''
            keys = pg.key.get_pressed()
            inf = keys[pg.K_i]
            reset1 = keys[pg.K_e]
            reset2 = keys[pg.K_w]
            reset3 = keys[pg.K_q]

            ''' определение типа и места хода и обновление таймера задержки'''
            if self.pressed_field and self.mouse_press[0] and not self.press_timer:
                self.press_timer = 30
                self.click()

            else:
                if self.press_timer:
                    self.press_timer -= 1

            ''' тестовый режим '''
            if self.test_mode == 2 and self.turn == 0:
                self.pressed_field = self.fields[3][3]


            ''' информация '''
            if inf and not self.press_timer:
                self.press_timer = 30
                info(self)

            ''' клик мышки для отладки '''
            if self.mouse_press[2] and not self.press_timer:
                print(self.mouse_x, self.mouse_y, )
                self.press_timer = 30

            ''' системые обновления '''
            update_objects(self)
            exit(self)
            pg.display.update()
            self.clock.tick(self.FPS)

            ''' сброс до заводских'''
            if (reset1 or reset2 or reset3) and not self.press_timer:
                if reset2:
                    self.test_mode = 1
                    self.press_timer = 15
                elif reset3:
                    self.play = False
                    for i in range(10):
                        print()
                    print('Game has reset')
                elif reset1:
                    self.test_mode = 0
                    self.press_timer = 15

        pg.quit()

'''выход из игры хз зачем'''
def exit(self):
    global stop_the_game
    for event in pg.event.get():
        if event.type == pg.QUIT:
            self.play = False
            stop_the_game = True



while not stop_the_game:
    game = Game()
    game.pre_starter()
    game.starter()
