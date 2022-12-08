import json

from files.clear import clear


def display_passwd():
    with open('.data/data.json') as jf:
        data = json.load(jf)

    num = 0

    for name in data["created_passwords"]:
        num += 1

        print(f"{num}. '{name}'\n")
    return