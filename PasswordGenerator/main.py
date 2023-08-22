# Imports ---------------------------
import GeneratingPassword # type: ignore
import os

# Class ---------------------------
class color:
   p = '\033[95m'; c = '\033[96m'
   dc = '\033[36m'; bl = '\033[94m'
   g = '\033[92m'; y = '\033[93m'
   r = '\033[91m'; bo = '\033[1m'
   und = '\033[4m'; end = '\033[0m'
   i = '\x1B[3m';  w = '\033[37m'
   
# Functions ---------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Run ---------------------------
clear()
size = int(input(f"{color.i}=> Inform the size of the password: {color.end}"))

GeneratingPassword.generate_password(size)