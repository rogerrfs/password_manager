from getpass import getpass
import hashlib

from files.clear import clear


def login():
    with open(".data/passwd/passwd.txt", "r") as file:
        file_ = file.read()

    while True:
        log_in = getpass("Enter your password \n>> ")
        log_in_encrypted = hashlib.md5(log_in.encode())
        log_in_final = log_in_encrypted.hexdigest()
        if log_in_final in file_:
            print("The password is correct!")

            with open(".data/temp_file.txt", "a") as tf:
                tf.write(log_in)

            clear()
            return

        else:
            print("The password is incorrect, please try again.")
