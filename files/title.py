from sys import platform
from art import *
import os
import os.path


def p_title():
    tprint("PasswdManager")
    print("By Roger Fibla")
    print("\n\nPress intro to continue")
    input("")
    
    if platform == "linux" or platform == "linux2":
        os.system('clear')
    elif platform == "win64":
        os.system('cls')
