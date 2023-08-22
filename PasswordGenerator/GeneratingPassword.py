# Imports ---------------------------
import random

# Characters tuples ---------------------------
especialChar = ["@", "!", "#", "$", "%", "*", "(", ")", "_"]
upperChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lowerChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Functions ---------------------------
def generate_password(size):
    password = []
    i = 0
    while i < size:
        option = random.randint(0,1)
        if option == 0:
            password.append(random.choice(lowerChar))
        elif option == 1:
            password.append(random.choice(upperChar))    
        i += 1
    return password