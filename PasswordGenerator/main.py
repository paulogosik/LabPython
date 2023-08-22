# Imports ---------------------------
import GeneratingPassword # type: ignore
import os
from tqdm import tqdm
import time

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

while size < 6 or size > 24:
    clear()
    size = int(input(f"{color.i}{color.r}The password needs to be bigger than 6 and smaller than 24.{color.end}\n{color.i}=> Inform the size of the password: {color.end}"))

weakPassword = GeneratingPassword.generate_weak_password(size)
mediumPassword = GeneratingPassword.generate_medium_password(size)
strongPassword = GeneratingPassword.generate_strong_password(size)

clear()
result = 0
for i in tqdm(range(3), ncols=80, unit="Mb"):
    time.sleep(1)
    result += i

clear()
weak = f"{color.r}Weak{color.end}"
medium = f"{color.y}Medium{color.end}"
strong = f"{color.g}Strong{color.end}"

print(f"{color.w}-" * 40)
print(f"{color.i}{color.w}{'PASSWORDS':^40}{color.end}")
print(f"{color.w}-" * 40)

print(f"{weak:.<25}", end='')
print(f"{weakPassword:.>24}")
print(f"{medium:.<25}", end='')
print(f"{mediumPassword:.>24}")
print(f"{strong:.<25}", end='')
print(f"{strongPassword:.>24}")

print(f"{color.w}-" * 40)