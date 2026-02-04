''' Параметры игры '''
import os
import json
DEFAULT = {
  'speed': 1
}

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def merge_basic(user_cfg, basic_cfg):
    for element in user_cfg:
        data = user_cfg[element]
        if data is None:
            user_cfg[element] = basic_cfg[element]
    return user_cfg

def create_path():
    p = os.path.join(os.path.dirname(__file__), 'config.json')
    abs = os.path.abspath(p)
    return abs

class GameSettings:
    def __init__(self):
        self.__data = merge_basic(load_json(create_path()), DEFAULT)

    def __getitem__(self, key):
        return self.__data[key]