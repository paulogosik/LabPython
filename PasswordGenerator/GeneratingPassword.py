# Imports ---------------------------
import os
import random

# Functions ---------------------------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_password(size):
    i = 0
    while i < size:
        print(i)
        
        i += 1