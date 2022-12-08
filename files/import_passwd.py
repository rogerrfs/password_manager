from cryptography.fernet import Fernet
import json
from getpass import getpass

from files.create_key import key_name


cipher = Fernet(key_name)

def import_passwd():
    input_name = input("Enter the name of the password:\n>> ")
    filename = ".data/passwd/" + input_name + ".txt"
    create_passwd_ = getpass("Create a password. This password will be encrypted.\n>> ")

    with open(filename, "w") as f:
        f.write(create_passwd_)
        f.close()

    with open(filename, "rb") as ef:
        e_file = ef.read()

    ectypted_passwd = cipher.encrypt(e_file)

    with open(filename, "ab") as ef:
        ef.truncate(0)
        ef.write(ectypted_passwd)

    with open(".data/data.json",'r+') as jf:
        file_data = json.load(jf)
        file_data["created_passwords"].append(input_name)
        jf.seek(0)
        json.dump(file_data, jf, indent = 4)
    
    
    del(create_passwd_)
