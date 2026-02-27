from math import ceil
from random import randrange

from StatusEffect import StatusEffect
from effects_animation import create_effect
from game_field import Object
from personality import Person
from tools import possible_heal, possible_damage, check_longth, death, incount, status_effect_update


class Necromancer(Person):
    def first_skill(self, game_object):
        if not self.first_skill_cd:
            if self.mana[0] >= 20:
                unhealed = game_object.pressed_field.status
                if unhealed:
                    if unhealed.side == self.side and unhealed != self:
                        StatusEffect(unhealed, 'Damage', 3, unhealed.basic_dmg_cof, 0.5, 'necromancer_first_skill')
                        value = possible_heal(unhealed, 100)
                        unhealed.health[0] += value
                        self.health[0] -= possible_damage(self, possible_heal(unhealed, 100)*0.3, 0, self.basic_dmg_cof, 0, self.avoidance)
                        create_effect((unhealed.x, unhealed.y), (unhealed.x, unhealed.y), unhealed, self.game_object, False, False,
                                      self.game_object.regenerations, 'Regeneration', 0.2, 2)
                        self.mana[0] -= 20
                        if not game_object.test_mode:
                            self.first_skill_cd = 3
                        game_object.end_of_turn(self)

                        print(f'Necromancer has healed ahlive bones at {value} and boosted his damage on {int(unhealed.basic_dmg_cof-1)*100}%')

    def second_skill(self, game_object):
        if not self.second_skill_cd:
            if self.mana[0] >= 20:
                if not game_object.pressed_field.status:
                    if check_longth(game_object.pressed_field, self, 4, game_object):
                        self.add_new_creature(game_object.pressed_field, game_object.persons, game_object.fields)
                        self.mana[0] -= 20
                        if not game_object.test_mode:
                            self.second_skill_cd = 2
                        game_object.end_of_turn(self)
                        game_object.step_didnt_do = True

    def third_skill(self, game_object):
        global creature, value1, value2
        if not self.third_skill_cd:
            if self.mana[0] >= 20:
                for i in game_object.creatures:
                    for creature in i:
                        if creature.side == self.side:
                            value1 = 100
                            StatusEffect(creature, 'Shield', 3, creature.basic_dmg_cof, value1,
                                                     'necromancer_third_skill_shield')
                            value2 = 50
                            StatusEffect(creature, 'Regeneration', 4, creature.basic_dmg_cof, value2,
                                                     'necromancer_third_skill_regeneration', True)
                self.mana[0] -= 20
                print(self.mana[0])
                if not game_object.test_mode:
                    self.third_skill_cd = 3
                game_object.end_of_turn(self)
                game_object.step_didnt_do = True
                create_effect((creature.x, creature.y), (creature.x, creature.y), creature, self.game_object, False, False,
                              self.game_object.regenerations, 'Regeneration', 0.3, 2)
                print(f'Ahlive bones comed stronger! (+{value1} shield on 3 moves and +{value2} health per turn for 4 moves')

    def add_new_creature(self, pressed_field, persons, fields):
        pivo = Necropet(pressed_field.x, pressed_field.y, self.side, persons, game_object=self.game_object, fields=fields, summoner=True, cls='Necropet')
        self.game_object.summons.append(pivo)
        self.pet.append(pivo)
        print(f'Necromancer has raised ahlive bones at X: {pivo.x} Y: {pivo.y}')
        pressed_field.status = pivo


class Necropet(Person):
    def first_skill(self, game_object):
        nuclears = []
        for i in range(self.x - 1, self.x + 2):
            for j in range(self.y - 1, self.y + 2):
                person = game_object.fields[i][j].status
                if person:
                    if person != self:
                        nuclears.append(person)
        nuclear = None
        if nuclears:
            for nuclear in nuclears:
                nuclear.health[0] -= possible_damage(nuclear, ceil((self.health[1] - self.health[0]) / 4), 0, self.basic_dmg_cof, nuclear.shield, self.avoidance)
                if nuclear.health[0] <= 0:
                    death(game_object, [[game_object, nuclear]])
            print(
                f'Ahlive bones has nuked! - {possible_damage(nuclear, ceil((self.health[1] - self.health[0]) / 2), 0, self.basic_dmg_cof, nuclear.shield, 0)} truth damage! ')
        create_effect((self.x, self.y), (self.x, self.y), self, self.game_object, False, False,
                      self.game_object.blasts, 'Blast', 0.3, 0.5)

        game_object.end_of_turn(self, dead=[[game_object, self]])

    def second_skill(self, game_object):
        self.first_skill(game_object)

    def third_skill(self, game_object):
        self.first_skill(game_object)

    def passive_skill(self, game):
        for summon in game.summons:
            for x in range(self.x-1, self.x+2):
                for y in range(self.y-1, self.y+2):

                    if summon != self and summon.side == self.side:
                        if summon not in self.activated:
                            if abs(summon.x - x) <= 1 and abs(summon.y - y) <= 1:
                                StatusEffect(self, 'Defence', 1, self.defence, 10, 'Necropet sinner')
                                self.activated.append(summon)
                        else:
                            if abs(summon.x - self.x) > 1 or abs(summon.y - self.y) > 1:
                                self.activated.remove(summon)
                                StatusEffect(self, 'Defence', 0, self.defence, 0, 'Necropet sinner', False, True)
                            else:
                                StatusEffect(self, 'Defence', 1, self.defence, 0, 'Necropet sinner', False, True)

    def __repr__(self):
        return f'Nercomraзь, {self.x, self.y}'


class Warrior(Person):
    def first_skill(self, game):
        if self.mana[0] > 20:
            if not self.first_skill_cd:
                StatusEffect(self, 'Damage', 2, self.basic_dmg_cof, 0.4, 'warrior_first_skill')
                if not game.test_mode:
                    self.first_skill_cd += 3
                self.mana[0] -= 20
                print('Warrior has flamed his sword')
                game.end_of_turn(self)

    def second_skill(self, game):
        if not self.second_skill_cd:
            if self.mana[0] >= 20:
                target_field = game.pressed_field
                if not target_field.status and not target_field.object:
                    start_field = game.mover_person
                    if check_longth(target_field, start_field, 4, game):
                        reg_max_value = max(abs(target_field.x-start_field.x), abs(target_field.y-start_field.y))
                        reg_min_value = min(abs(target_field.x-start_field.x), abs(target_field.y-start_field.y))

                        if reg_min_value != reg_max_value: regroups = abs(reg_max_value) // (abs(reg_min_value)+1)
                        else: regroups = abs(target_field.x-start_field.x)
                        while True:
                            for i in range(regroups):
                                for i in game.creatures:
                                    for creature in i:
                                        if abs(creature.x-self.x) <= 1:
                                            if abs(creature.y - self.y) <= 1:
                                                if creature.side != self.side:
                                                    game.charge_attract.append(creature)

                                if (target_field.x != self.x or target_field.y != self.y) and not game.charge_stop:
                                    stop = False
                                    for i in range(self.x-1, self.x+2):
                                        for j in range(self.y-1, self.y+2):
                                            if game.fields[i][j] == target_field and target_field.status: stop = True
                                    if not stop:
                                        if target_field.x == self.x or abs(target_field.y-self.y) >= abs(target_field.x - self.x):
                                            cof = incount(target_field.y-start_field.y)
                                            self.movement(game, self.x, self.x, self.y, self.y+cof, True, self)
                                        elif target_field.y == self.y or abs(target_field.x - self.x) >= abs(target_field.y - self.y):
                                            cof = incount(target_field.x-start_field.x)
                                            self.movement(game, self.x, self.x+cof, self.y, self.y, True, self)
                                        else: break
                                else: break
                            if (self.x != target_field.x or self.y != target_field.y) and not game.charge_stop:
                                stop = False
                                for i in range(self.x - 1, self.x + 2):
                                    for j in range(self.y - 1, self.y + 2):
                                        if game.fields[i][j] == target_field and target_field.status: stop = True
                                if not stop:
                                    cofy = incount(target_field.y-start_field.y)
                                    cofx = incount(target_field.x-start_field.x)
                                    self.movement(game, self.x, self.x + cofx, self.y, self.y + cofy, True, self)
                                    for i in game.creatures:
                                        for creature in i:
                                            if abs(creature.x - self.x) <= 1:
                                                if abs(creature.y - self.y) <= 1:
                                                    if creature.side != self.side:
                                                        game.charge_attract.append(creature)
                                else: break
                            else: break
                        game.charge_stop = False
                        stuned = []
                        for person in set(game.charge_attract):
                            cofx = incount(person.x-self.x)
                            cofy = incount(person.y-self.y)
                            for i in range(3):
                                if (-1 < person.x+cofx < 10) and (-1 < person.y+cofy < 10):
                                    if not game.fields[person.x+cofx][person.y+cofy].status:
                                        person.movement(game, person.x, person.x+cofx, person.y, person.y+cofy, True, person)
                                    else:
                                        stuned.append(person)
                                        person.stun += 1
                                else:
                                    stuned.append(person)
                                    person.stun += 1
                        self.mana[0] -= 20
                        if not game.test_mode:
                            self.second_skill_cd = 3
                        game.charge_attract = []
                        game.end_of_turn(self)
                        print(f'Warrior has charged! {', '.join([str(x) for x in stuned])} has stuned.')

    def third_skill(self, game):
        if self.mana[0] > 40 and not self.third_skill_cd:
            self.mana[0] -= 40
            if not game.test_mode:
                self.third_skill_cd += 4
            print(self.shield)
            StatusEffect(self, 'Shield', 3, self.shield, 200, 'warrior_third_skill_shield')
            print(self.shield)
            StatusEffect(self, 'Reflect', 3, self.reflect, 0.3, 'warrior_third_skill_reflect')
            print(
                f'Warrior has raised his shield up! + {self.shield} shield for 4 moves and + {int(self.reflect * 100)}% reflect')
            game.end_of_turn(self)


class Mage(Person):
    def first_skill(self, game):
        if self.mana[0] > 20:
            if not self.first_skill_cd:
                if not game.pressed_field.object:
                    if check_longth(game.pressed_field, self, 3, game):
                        self.third_skill_cd += 3
                        self.mana[0] -= 20
                        for i in range(game.pressed_field.x-1, game.pressed_field.x+2):
                            for j in range(game.pressed_field.y-1, game.pressed_field.y+2):
                                if not game.fields[i][j].object:
                                    Object(i, j, 'Firewall', game.fields, game, time=3)
                        if not game.test_mode:
                            self.first_skill_cd = 3
                        game.end_of_turn(self)
                        print('YOU HAVE TO BE BURNED!!!')

    def second_skill(self, game):
        if self.mana[0] > 20:
            if not self.second_skill_cd:
                if not game.pressed_field.status:
                    if check_longth(self, game.pressed_field, 4, game):
                        create_effect((self.x, self.y), (self.x, self.y), self, self.game_object, False, False,
                                      self.game_object.blinks, 'Blink', 0.2, 2.5, double=True)
                        self.mana[0] -= 20
                        if not game.test_mode:
                            self.second_skill_cd = 3
                        print('CATCH ME, CATCH ME, CATCH ME!!!')

    def third_skill(self, game):
        if self.mana[0] > 20:
            if not self.third_skill_cd:
                for person in game.persons:
                    if person.side != self.side:
                        StatusEffect(person, 'Fire', 2, 100, 80, 'FireFireFire!!!', True)
                for x in range(0, 10):
                    for y in range(0, 10):
                        if not game.fields[x][y].object:
                            if not randrange(0, 2):
                                Object(x, y, 'Firewall', game.fields, game, time=3)
                if not game.test_mode:
                    self.third_skill_cd = 8
                self.mana[0] -= 20
                print('THIS LAND WILL BURN IN FIRE!!!')
                game.end_of_turn(self)


class Rogue(Person):
    def first_skill(self, game):
        if self.mana[0] > 20:
            if not self.first_skill_cd:
                if game.pressed_field.status:
                    if check_longth(game.pressed_field, self, 5, game):
                        cofx = -incount(self.x-game.pressed_field.x)
                        cofy = -incount(self.y-game.pressed_field.y)
                        if not game.fields[game.pressed_field.x+cofx][game.pressed_field.y+cofy].status:
                            self.can_be_attacked = False
                            self.image.set_alpha(0)
                            self.movement(game, self.x, game.pressed_field.x+cofx, self.y, game.pressed_field.y+cofy, True, self)
                            self.basic_attack(game)
                            self.can_be_attacked = True
                            self.mana[0] -= 20
                            if not game.test_mode:
                                self.first_skill_cd = 3


    def second_skill(self, game):
        if self.mana[0] > 20:
            if not self.second_skill_cd:
                self.mana[0] -= 20
                StatusEffect(self, 'can_be_attacked', 3, True, False, 'Rogue_invisible')

                if not game.test_mode:
                    self.second_skill_cd = 5
                game.end_of_turn(self)

    def third_skill(self, game):
        dead = []
        if self.mana[0] > 20:
            if not self.third_skill_cd:
                if game.pressed_field.status:
                    if check_longth(game.pressed_field, self, 1, game):
                        damaged = game.pressed_field.status
                        if damaged.status_effects:
                            for effect in damaged.status_effects:
                                if effect.type == 'Blood' and effect.uncount >= 2 and not self.can_be_attacked:
                                    va = possible_damage(damaged, ((damaged.health[1]-damaged.health[0])//10*effect.uncount), damaged.defence, 1, damaged.shield, 0)

                                    damaged.health[0] -= va
                                    print(f'Rogue has maked extra attack: -{va} health! Wooow')
                                    damaged.first_skill_cd += 2
                                    damaged.second_skill_cd += 2
                                    if damaged.health[0] <= 0:
                                        dead = [[game, damaged]]
                                    self.mana[0] -= 20
                                    if not game.test_mode:
                                        self.third_skill_cd = 3
                                    game.end_of_turn(self, dead)


class Hunter(Person):
    def first_skill(self, game):
        if self.mana[0] > 20:
            if not self.first_skill_cd:


                self.mana[0] -= 20
                game.end_of_turn(self)
                if not game.test_mode:
                    self.first_skill_cd = 3

    def second_skill(self, game):
        if self.mana[0] > 20:
            if not self.second_skill_cd:
                pet = self.pet[0]
                StatusEffect(pet, 'InvisibleInTree', 2, None, None, 'HuntersInvisible', True)
                StatusEffect(self, 'InvisibleInTree', 2, None, None, 'HuntersInvisible', True)
                status_effect_update(pet, 'HuntersInvisible', game)
                status_effect_update(self, 'HuntersInvisible', game)

                self.mana[0] -= 20
                game.end_of_turn(self)
                if not game.test_mode:
                    self.second_skill_cd = 5

    def third_skill(self, game):
        if self.mana[0] > 20:
            if not self.third_skill_cd:

                self.mana[0] -= 20
                if not game.test_mode:
                    self.third_skill_cd = 3


class HuntersPet(Person):
    def first_skill(self, game):
        if self.mana[0] > 20:
            if not self.first_skill_cd:
                if game.pressed_field.status:
                    if check_longth(game.pressed_field, self, 1, game):
                        undamaged = game.pressed_field.status
                        value = possible_damage(undamaged, 80, undamaged.defence, self.basic_dmg_cof, undamaged.shield, undamaged.avoidance)
                        undamaged.health[0] -= value
                        StatusEffect(undamaged, 'Immobilization', 2, 1, 0, 'HuntersPetImmobilization')
                        print(f'Wolf has byte {undamaged}: - {value} health and immobilized him for 2 turns!')

                self.mana[0] -= 20
                if not game.test_mode:
                    self.first_skill_cd = 3

    def second_skill(self, game):
        self.first_skill(game)

    def third_skill(self, game):
        self.first_skill(game)