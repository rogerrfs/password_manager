import json
import os

from files.clear import clear

def delete_from_json(arg):
    with open('.data/data.json') as js:
        data = json.load(js)

    n = 0

    for passwd in data["created_passwords"]:
        if passwd == arg:
            data["created_passwords"].pop(n)
            break
        else:
            n += 1

    with open('.data/data.json', 'w') as file: 
        json.dump(data, file)  


def delete_passwd():
    passwd_name = input("Enter the name of the passwdord you want to delete.\n>> ")

    confirmation = input("Are you sure you want to delete the passwdord? (y/n) or (yes/no)\n>> ")

    path = (".data/passwd/" + passwd_name + ".txt")
   
    if confirmation == 'y' or 'yes':

        if os.path.exists(path):

            os.remove(path)

            delete_from_json(passwd_name)

        else:
            print("\nPassword not recognized.\nPlease try again.")
            input("Press enter to continue ")
    
    else:
        pass

    