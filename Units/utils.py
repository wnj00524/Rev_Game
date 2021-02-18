import json
import os

def save_setting(file, to_write):
    data = {}
    if os.path.isfile(file):
        with open(file) as json_file:
            data = json.load(json_file)
    data.update(to_write)
    with open(file, "w") as json_file:
        json.dump(data, json_file)


def read_setting(file, setting):
    setting = str(setting).lower()
    data = {}
    val = None
    if os.path.isfile(file):
        with open(file) as json_file:
            data = json.load(json_file)
        val = data.get(setting)
    return val

