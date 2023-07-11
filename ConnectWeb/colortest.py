import os

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class color:
   p = '\033[95m'; c = '\033[96m'
   dc = '\033[36m'; bl = '\033[94m'
   g = '\033[92m'; y = '\033[93m'
   r = '\033[91m'; bo = '\033[1m'
   und = '\033[4m'; end = '\033[0m'
   i = '\x1B[3m';  w = '\033[37m'
   
class bg:
    ba = '\033[40m'; r = '\033[41m'
    g = '\033[42m'; y = '\033[43m'
    bl = '\033[44m'; m = '\033[45m'
    c = '\033[46m'; w = '\033[47m' 

Clear()
print(f"{color.bo}{color.g}=[( class color )]={color.end}")    
print(f"{color.p}[color.p]{color.end}  -  {color.c}[color.c]{color.end}")
print(f"{color.dc}[color.dc]{color.end}  -  {color.bl}[color.bl]{color.end}")
print(f"{color.g}[color.g]{color.end}  -  {color.y}[color.y]{color.end}")
print(f"{color.r}[color.r]{color.end}  -  {color.bo}[color.bo]{color.end}")
print(f"{color.und}[color.und]{color.end}  -  {color.w}[color.w]{color.end}")
print(f"{color.i}[color.i]{color.end}  -  [color.end]")

print(f"\n")

print(f"{color.bo}{color.g}=[( class bg )]={color.end}")    
print(f"{bg.ba}[bg.ba]{color.end}  -  {bg.r}[bg.r]{color.end}")
print(f"{bg.g}[bg.g]{color.end}  -  {bg.y}[bg.y]{color.end}")
print(f"{bg.bl}[bg.bl]{color.end}  -  {bg.m}[bg.m]{color.end}")
print(f"{bg.c}[bg.c]{color.end}  -  {bg.w}[bg.w]{color.end}")

opc = input()