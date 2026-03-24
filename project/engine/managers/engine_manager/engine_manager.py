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

        self.stick_lines = {
            'x': [],
            'y': []
        }

        self.able_to_change = False

    def setup(self, settings):
        self.able_to_change = self.main.settings.open_settings['able_to_change']
        self.main.events.subscribe(self, EventTypes.SCENEHASCHANGED)

    def save_config_to_json(self):
        log_info('creating json file: start')
        data = {}
        for scene in self.__data.keys():
            # КОСТЫЫЫЫЫЛЬ!
            if scene == self.main.manager.scene_manager.current_scene:

                data[scene] = {
                    'widgets':
                        {'buttons': {}, 'panels': {}, "labels": {}}
                }

                ''' сохранение кнопок '''
                for button_id in self.__data[scene]['widgets']['buttons']:
                    button = self.main.manager.widget_manager.get_widget(button_id)
                    data[scene]['widgets']['buttons'][button.id] = button.get_data_json_like()

                ''' сохранение текстовых полей '''
                for label_id in self.__data[scene]['widgets']['labels']:
                    label = self.main.manager.widget_manager.get_widget(label_id)
                    data[scene]['widgets']['labels'][label_id] = label.get_data_json_like()

                ''' сохранение панелей '''
                for panel_id in self.__data[scene]['widgets']['panels']:
                    panel = self.main.manager.widget_manager.get_widget(panel_id)
                    data[scene]['widgets']['panels'][panel.id] = panel.get_data_json_like()

                self.__data[scene] = data[scene]
            path = create_path()
            with open(path, 'w', encoding="utf-8") as f:
                json.dump(self.__data, f, indent=4)

            log_info('creating json file: finish')
            log_info('interface has saved')

    def trigger(self, msg, data):
        " принимает сырые данные и создает виджеты, затем создает событие со всеми созданными виджетами"
        if msg == EventTypes.SCENEHASCHANGED:
            d = {
                'widgets': [],
                'panels': []
            }
            scene = data['scene']
            local_config = self.__data[scene]
            ''' виджеты '''
            widgets = local_config["widgets"]

            ''' Panel's serialize '''
            for panel_id in widgets["panels"]:
                panel = widgets["panels"][panel_id]
                d['widgets'].append(
                    WidgetTypes.PanelWidget.value(self.main, panel["position"], panel["size"], panel_id, panel["layer"],
                                                  panel['panel'],
                                                  panel["moveable"], panel["visible"], panel["enabled"],
                                                  panel['anchor'], panel['offset']))
            self.main.events.push_emit(EventTypes.SCENEOBJECTSCREATED, d)
            ''' Label's serialize '''
            for label_id in widgets["labels"]:
                label = widgets["labels"][label_id]
                d['widgets'].append(
                    WidgetTypes.LabelWidget.value(self.main, label["position"], label["size"], label_id, label["layer"], label["panel"],
                                                  label["anchor"], label["offset"], label["moveable"], label["visible"], label["enabled"],
                                                  label["text_pattern"], label["text_anchor"], label["text_size"]))

            ''' Button's serialize '''
            for button_id in widgets["buttons"]:
                button = widgets["buttons"][button_id]
                dt = button["command"]['data']
                d['widgets'].append(WidgetTypes.ButtonWidget.value(self.main, button["position"], button["size"],
                                                                   button_id, button["text"],
                                                                   (self.commands[button["command"]["action"]], dt,
                                                                    button["command"]["action"]), button["layer"],
                                                                   button["panel"],
                                                                   button['moveable'], button["visible"],
                                                                   button["enabled"], button['anchor'],
                                                                   button['offset']))

            self.main.events.emit(EventTypes.SCENEOBJECTSCREATED, d)
            return True
        return False
    def __getitem__(self, key):
        return self.__data[key]

    def __iter__(self):
        return iter(self.__data)
