import json

def save_json(dic, path, file):
    road = path+file
    with open(road, 'w') as f:
        json.dump(dic, f)