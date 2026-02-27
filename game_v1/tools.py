from math import atan2, degrees, ceil
from random import randrange

'''определяет нажатое поле'''
def which_field(mouse_press, mouse_pressed, mouse_x, mouse_y, size, fields) -> '"field"':
    if mouse_press[0] and not mouse_pressed[0]:
        returner = [[], []]
        mouse_pressed[0] = True
        if 250 < mouse_x < 1150:
            if 50 < mouse_y < 950:
                returner[0] = fields[((mouse_x - 250) // size)][((mouse_y - 50) // size)]
        if 255 < mouse_x < 1145:
            if 950 < mouse_y < 995:
                returner[1] = (mouse_x - 250) // (size * 2) + 1
        return returner
    elif not mouse_press[0]:
        mouse_pressed[0] = False

'''перекрашивает поле'''
def color_changer(field, color) -> None:
    if field.color != color:
        field.color = color
    else:
        field.color = 'Gray'

'''обновляет обьекты на экране'''
def update_objects(self):
    self.outpost = 0
    self.window.blit(self.image_background, (self.outpost, 0))
    for i in self.fields:
        for field in i:
            if -1 < field.x < 10:
                if -1 < field.y < 10:
                    field.draw(self.window, self.font, self)
    for person in self.creatures:
        for j in person:
            j.update(self)
    self.gui.draw(self.window, None, self.size, self.height, self.mover_person.move_type, self.mover_person,
                  self.size)
    for effect in self.effects:
        effect.update()
        effect.draw()
    for object in self.objects:
        object.draw()


''' возвращает ходящего в данный ход и обновление хода '''
def turner(self):
    if self.new_move:
        self.new_move = False
        self.didnt_move = []
        for i in self.creatures:
            for j in i:
                self.didnt_move.append(j)
        self.already_moved = []
        update_states(self, self.creatures)
    self.step_didnt_do = False
    self.new_move = False
    self.qwerty = self.didnt_move[0]
    return self.didnt_move[0]

'''обнолвляет очередь'''
def passer(self):
    if self.qwerty in self.didnt_move:
        self.didnt_move.remove(self.qwerty)
    if not self.didnt_move:
        self.new_move = True

def dot_update(game, person):
    dead = []
    if person.positive_dots:
        person.health[0] += person.positive_dots
    if person.negative_dots:
        person.health[0] -= person.negative_dots
        if person.health[0] <= 0:
            dead = [[game, game.mover_person]]
    return dead

''' проверка на дальность '''
def check_longth(pressed_field, start_field, longth, game):
    if not game.test_mode:
        return abs(pressed_field.x - start_field.x) <= longth and abs(pressed_field.y - start_field.y) <= longth
    else:
        return True

''' Обновление статусных эффектов '''
def status_effect_update(person, eff, game, ):
    for effect in person.status_effects:
        if effect.signature.lower() == eff.lower():
            effect.update(game)

''' рaсстчет урона '''
def possible_damage(damaged_person, damage, defence, basic_dmg_cof, shield, avoidance):
    dmg_cof_random = randrange(75, 125)
    must_damage = ceil(damage * dmg_cof_random // 100 * basic_dmg_cof - defence)
    avoid_real = randrange(0, 101)
    if must_damage < 20:
        must_damage = 20
    if shield != 0:
        if avoid_real > avoidance:
            must_damage_after_penetration = shield - must_damage
            if shield - must_damage < 0:
                damaged_person.shield = 0
            else:
                damaged_person.shield -= must_damage
            if must_damage_after_penetration <= 0:
                return -must_damage_after_penetration
            else:
                return 0
        else:
            print('Avoided! ')
            return 0
    else:
        if avoid_real > avoidance:
            return must_damage
        else:
            print('Avoided! ')
            return 0

''' рассчет лечения '''
def possible_heal(healed_person, healing):
    if healed_person.health[0] + healing < healed_person.health[1]:
        return healing
    else:
        return healed_person.health[1] - healed_person.health[0]

'''информация'''
def info(self):
    turn = 0
    true_cords = []
    false_cords = []
    print(' ' * 16, 'Info!')
    print('-' * 40)

    for i in self.creatures:
        for person in i:
            print('-' * 10)
            print(person)
            print(f'Cords: x:{person.x} y:{person.y}, Health: {person.health[0]}, Mana: {person.mana}')
            print(f'Defence: {person.defence}, Shield: {person.shield}, damage cof: {person.basic_dmg_cof}, Avoidance: {person.avoidance}')
            print('Effects: ')
            if person.status_effects:
                for effect in person.status_effects:
                    print(effect, effect.uncount, end=', ')
                print()
            true_cords.append([person.x, person.y])

    for i in self.fields:
        for j in i:
            if j.status:
                if [j.x, j.y] not in true_cords:
                    false_cords.append([i, j])
    if false_cords:
        print('Artefacts: ')
        for i in false_cords:
            print(i[-1])
    if self.test_mode:
        print(f'Passue: {', '.join([str(x) for x in self.didnt_move])}')
        print(f'Already moved: {', '.join([str(x) for x in self.already_moved])}')

''' рассчет тангенса угла наклона '''
def tan_counter(x, y):
    return degrees(atan2(y, x))

''' рассчет коэффициента перемещения '''
def incount(x):
    if x > 0: return 1
    elif x < 0: return -1
    else: return 0

def death(self, dead):
    self.fields[dead.x][dead.y].status = None
    if dead in self.didnt_move:
        self.didnt_move.remove(dead)
    if dead in self.already_moved:
        self.already_moved.remove(dead)

    if dead in self.creatures[0]:
        self.creatures[0].remove(dead)
        self.turn += 2
    elif dead in self.creatures[1]:
        self.creatures[1].remove(dead)
    print(f'{dead} x: {dead.x} y: {dead.y} has dead')

'''обновляет эффекты на персонаже'''
def update_states(self, persons):
    for i in persons:
        for person in i:

            if person.first_skill_cd: person.first_skill_cd -= 1
            if person.second_skill_cd: person.second_skill_cd -= 1
            if person.third_skill_cd: person.third_skill_cd -= 1

            if person.health[0] + person.health[2] <= person.health[1]: person.health[0] += person.health[2]
            else: person.health[0] = person.health[1]

            if person.mana[0] + person.mana[2] <= person.mana[1]: person.mana[0] += person.mana[2]
            else: person.mana[0] = person.mana[1]


    for object in self.objects:
        object.update()

    print('End of turn!')
    print('-'*20)

''' определение атрибутов '''
