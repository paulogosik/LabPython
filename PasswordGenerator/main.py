# Imports ---------------------------
import os
from random import randint

# Functions ---------------------------
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Characters tuples ---------------------------
especialChar = ("@", "!", "#", "$", "%", "*", "(", ")", "_")

size = int(input(f"=> Inform the size of the password: "))

i = 0
while 