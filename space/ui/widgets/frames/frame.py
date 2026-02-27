from space.battle.events.either.listeners.text_listener import TextListener
from space.ui.widgets.UIelement import UIelement
from space.game_objects.text_object.text_object import TextObject


class Frame(UIelement):
    def __init__(self, cords, size, main, text_data, parent=None, center: tuple = (False, False), font=1):
        super().__init__(cords, size, main, parent, center)
        self.mark = text_data

        self.listeners = []
        self.font = self.main.ws.GLOBAL_TEXT_CACHE[['little', 'default', 'big', 'extra'][font]]

        self.text_data = TextObject(self.main, [''], self.font)
        self.setup_text(text_data)

        self.parent = parent
    def setup_text(self, text_data):
        ready = []
        for element in text_data:
            if isinstance(element, tuple):
                lis_config = element[2]
                obj = TextListener(self.main, self, lis_config)
                self.main.manager.events.subscribe(element[1], obj, element[0])
                obj.sub = element[0]
                obj.event = element[1]
                obj.format = element[2]
                obj.looking_object = element[3]

                if self.main.manager.events.get_event(obj.event, True) == 1:
                    self.main.manager.events.emit(obj.event, obj.sub, True,
                                                  object=obj.looking_object)
                else:
                    obj.looking_parameter = getattr(obj.looking_object, element[4])
                    self.main.manager.events.emit(obj.event, obj.sub, True,
                                                  object=obj.looking_object, value=obj.looking_parameter.value)
                self.listeners.append(obj)
                ready.append(obj)
            else:
                ready.append(element)
        self.text_data = TextObject(self.main, ready, self.font)

    def update(self):
        pass

    def draw(self, window):
        self.surface.blit(self.text_data.surface, (0, 0))
        window.blit(self.surface, self.rect)

    def __repr__(self):
        return 'Frame'
