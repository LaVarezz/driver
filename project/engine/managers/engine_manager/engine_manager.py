import json
import os

from project.data.protocols.protocols import MainLike
from project.engine.events.event_types import EventTypes
from project.engine.managers.basic_manager import Manager
from project.engine.managers.widget_manager.widgets.buttons.commands.command_types import commands
from project.engine.managers.widget_manager.widgets.widget_types import WidgetTypes
from project.engine.utills.logging.log import log_info


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_path():
    p = os.path.join(os.path.dirname(__file__), 'config.json')
    abs = os.path.abspath(p)
    return abs


class EngineManager(Manager):
    def __init__(self, main: MainLike):
        super().__init__()
        self.main = main
        self.__data = load_json(create_path())
        self.commands = commands
        self.able_to_change = False

    def setup(self, settings):
        print(self.__data)
        self.main.events.subscribe(self, EventTypes.SCENEHASCHAMGED)

    def save_config_to_json(self):
        log_info('creating interface json file: start')
        data = {}
        for scene in self.__data.keys():
            data[scene] = {
                'widgets':
                    {'buttons': {}, }
            }

            ''' сохранение кнопок '''
            for widget_id in self.__data[scene]['widgets']['buttons']:
                widget = self.main.manager.widget_manager.get_widget(widget_id)
                data[scene]['widgets']['buttons'][widget.id] = widget.get_data_json_like()

            self.__data[scene] = data[scene]
        print(self.__data)
        path = create_path()
        with open(path, 'w', encoding="utf-8") as f:
            json.dump(self.__data, f, indent=4)

        log_info('creating interface json file: finish')

    def trigger(self, msg, data):
        " принимает сырые данные и создает виджеты, затем создает событие со всеми созданными виджетами"
        if msg == EventTypes.SCENEHASCHAMGED:
            d = {
                'widgets': []
            }
            scene = data['scene']
            local_config = self.__data[scene]
            ''' виджеты '''
            widgets = local_config["widgets"]
            for button_id in widgets["buttons"]:
                button = widgets["buttons"][button_id]
                dt = button["command"]['data']
                d['widgets'].append((WidgetTypes.ButtonWidget.value(self.main, button["position"], button["size"],
                                                                    button_id, button["text"],
                                                                    (self.commands[button["command"]["action"]], dt, button["command"]["action"]), button["layer"], button['moveable'])))
            self.main.events.emit(EventTypes.SCENEOBJECTSCREATED, d)

    def __getitem__(self, key):
        return self.__data[key]

    def __iter__(self):
        return iter(self.__data)
