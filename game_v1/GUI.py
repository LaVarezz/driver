
import pygame as pg
import Classes

def players(self):
    Classes.Warrior(9, 5, 1, persons=self.persons, fields=self.fields, game_object=self, cls='Warrior')
    Classes.Mage(0, 4, 0, persons=self.persons, fields=self.fields, game_object=self, cls='Mage')
    Classes.Hunter(1, 5, 0, persons=self.persons, fields=self.fields, game_object=self, cls="Hunter")
    Classes.Rogue(0, 3, 0, persons=self.persons, fields=self.fields, game_object=self, cls="Rogue")
    Classes.Necromancer(9, 4, 1, persons=self.persons, fields=self.fields, game_object=self, cls="Necromancer")
    Classes.Hunter(9, 6, 1, persons=self.persons, fields=self.fields, game_object=self, cls="Hunter")
    GUI()


class GUI:
    @staticmethod
    def draw(window, font, width, height, chosed_move, mover, size):
        font = pg.font.Font('sprites/main_font.otf', 28)
        '''передвижение'''
        movement_button = pg.rect.Rect(255, height-45, width*2-10, 40)
        pg.draw.rect(window, 'black', movement_button)

        text = font.render('Movement', 1, 'white')
        window.blit(text, (282, movement_button.centery-12))
        '''базовая атака'''
        basic_attack_button = pg.rect.Rect(255+width*2, height-45, width*2-10, 40)
        pg.draw.rect(window, 'black', basic_attack_button)

        text = font.render('Basic attack', 1, 'white')
        window.blit(text, (275+width*2, movement_button.centery-12))

        '''Первый навык'''
        first_skill_button = pg.rect.Rect(255 + width * 4, height - 45, width * 2 - 10, 40)
        pg.draw.rect(window, 'black', first_skill_button)

        text = font.render('First skill', 1, 'white')
        window.blit(text, (290 + width * 4, first_skill_button.centery - 12))

        '''Второй навык'''
        second_skill_button = pg.rect.Rect(255+width*6, height-45, width*2-10, 40)
        pg.draw.rect(window, 'black', second_skill_button)

        text = font.render('Second skill', 1, 'white')
        window.blit(text, (277+width*6, second_skill_button.centery-12))

        '''Третий навык'''
        third_skill_button = pg.rect.Rect(255+width*8, height-45, width*2-10, 40)
        pg.draw.rect(window, 'black', third_skill_button)

        text = font.render('Third skill', 1, 'white')
        window.blit(text, (284+width*8, third_skill_button.centery-12))


        frame_button = pg.rect.Rect(255+width*2*chosed_move, height-45, width*2-10, 40)
        pg.draw.rect(window, 'Orange', frame_button, 2)

        if mover.can_draw_avatar:
            frame_button_2 = pg.rect.Rect(250+size*mover.x, 50+size*mover.y, size, size)
            pg.draw.rect(window, 'white', frame_button_2, 2)


