import os
import os.path
from sys import platform

def clear():
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win64":
        os.system('cls')
    elif platform == "win32":
        os.system('cls')
