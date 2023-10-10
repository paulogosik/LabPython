# Imports ---------------------------
import random

# Characters tuples ---------------------------
especialChar = ["@", "!", "$", "%", "*", "(", ")", "_"]
upperChar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']
lowerChar = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v', 'w', 'x', 'y', 'z']
numChar = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
char_ascii = [" ", "!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", '.', '/', "0", "1", "2", "3",
              "4", "5", "6", "7", "8", "9", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F", "G", "H",
              "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "[", "\\", "]",
              "^", "_", "`", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
              "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~"]


# Functions ---------------------------
# Weak Password
def generate_weak_password(size):
    password = []
    i = 0
    while i < size:
        option = random.randint(0, 1)
        if option == 0:
            password.append(random.choice(lowerChar))
        elif option == 1:
            password.append(random.choice(upperChar))
        i += 1

    password = ''.join(password)
    return password


# Medium Password
def generate_medium_password(size):
    password = []
    i = 0
    while i < size:
        if i == 0:
            password.append(random.choice(numChar))
        else:
            option = random.randint(0, 2)
            if option == 0:
                password.append(random.choice(lowerChar))
            elif option == 1:
                password.append(random.choice(upperChar))
            elif option == 2:
                password.append(random.choice(numChar))
        i += 1

    password = ''.join(password)
    return password


# Strong Password
def generate_strong_password(size):
    password = []
    i = 0
    while i < size:
        if i == 0:
            password.append(random.choice(especialChar))
        elif i == 1:
            password.append(random.choice(numChar))
        else:
            option = random.randint(0, 3)
            if option == 0:
                password.append(random.choice(lowerChar))
            elif option == 1:
                password.append(random.choice(upperChar))
            elif option == 2:
                password.append(random.choice(numChar))
            elif option == 3:
                password.append(random.choice(especialChar))
        i += 1

    password = ''.join(password)
    return password


def encode_password(typed_password):
    password = []

    for pos, char in enumerate(typed_password):
        for p, c in enumerate(char_ascii):
            if c == char:
                password.append(char_ascii[p + 3])

    password.reverse()

    len_password = len(password) - 1
    last_pos = password.pop(len_password)
    first_pos = password.pop(0)

    password.append(first_pos)
    password.insert(0, last_pos)
    final_password = ''.join(password)

    return final_password
