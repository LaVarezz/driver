from xmlrpc.client import Boolean

from tools import possible_heal, possible_damage, death
class StatusEffect:
    def __init__(self, person, type, time, state_before, value, signature, dot=None, multiple=None):
        if multiple is None:
            multiple = []
        self.signature = signature
        self.type = type
        self.time = time
        self.person = person
        self.dot = dot
        self.value = value
        self.multiple_effect = multiple
        self.uncount = 1
        append = True
        if not self.dot:
            for effect in person.status_effects:
                if effect.signature == self.signature:
                    append = False
                    if self.multiple_effect:
                        if self.type == 'Defence':
                            effect.value += self.value
                            effect.time = 1
                            effect.uncount += 1
                        if self.type == 'Blood':
                            effect.value += self.value
                            effect.time = self.time
                            effect.uncount += 1
                    else:
                        effect.time = self.time

            if append:
                self.stateBefore = state_before
                if not isinstance(self.value, Boolean):
                    setattr(self.person, self.type.lower(), getattr(self.person, self.type.lower()) + value)
                else:
                    setattr(self.person, self.type.lower(), value)
                self.person.status_effects.append(self)
        else:
            self.person.status_effects.append(self)


    def update(self, game):
        if self.time: self.time -= 1
        else:
            for effect in self.person.status_effects:
                if self == effect:
                    if not self.dot:
                        setattr(self.person, self.type.lower(), getattr(self.person, self.type.lower())-self.value)
                    self.person.status_effects.remove(self)
                    print(f'effect {self.type} {self.uncount} has end')

        if self.dot:
            if self.type == 'Regeneration':
                va = possible_heal(self.person, self.value)
                self.person.health[0] += va
                print(f'{self.person} has been healed: + {va} health')
            elif self.type == 'Fire':
                if self.person.cls != 'Mage':
                    va = possible_damage(self, self.value, 0, 1, 0, 0)
                    self.person.health[0] -= va
                    print(f'{self.person} has been damaged by fire: -{va} health')
                    if self.person.health[0] <= 0:
                        death(game, self.person)
                else:
                    va = possible_heal(self.person, self.value//5)
                    self.person.health[0] += va
            elif self.type == 'Blood':
                va = possible_damage(self.person, self.value, 0, 1, self.person.shield, 0)
                self.person.health[0] -= va
                if self.person.health[0] <= 0:
                    death(game, self.person)
                print(f'{self.person} has been damaged by Blood: -{va} health')
            elif self.type == 'InvisibleInTree':
                contin = False
                for x in range(self.person.x-1, self.person.x+2):
                    for y in range(self.person.y-1, self.person.y+2):
                        if game.fields[x][y].object and game.fields[x][y].object.type == 'Tree':
                            contin = True
                if contin:
                    StatusEffect(self.person, 'can_be_attacked', 1, True, False, 'HuntersInvisible2')
                else:
                    self.person.can_be_attacked = True

    def __repr__(self):
        return f'{self.type}'
