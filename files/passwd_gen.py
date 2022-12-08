import string
from random import *

characters = list(string.ascii_letters + string.digits + "!@#$%^&*")

def passwd_gen():
    length = int(input("Enter the lenght of the password \n>> "))

    shuffle(characters)

    password = []

    for i in range(length):
        char = choice(characters)
        password.append(char)

    shuffle(password)

    print("Your password is " + "".join(password))
