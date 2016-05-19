import os, pwd, json
from yubi_lock.api import BASE_DIR


def get_username():
    return pwd.getpwuid(os.getuid())[0]


def store_key(ident):
    with open(os.path.join(BASE_DIR, "data/keys.json")) as file:
        existing_data = json.load(file)

    existing_data.append(ident)

    with open(os.path.join(BASE_DIR, "data/keys.json"), 'w') as file:
        json.dump(existing_data, file)
