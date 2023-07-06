# pyinstaller --onefile NomeArquivo.py/ pyinstaller --onefile -w NomeArquivo.py
# Importações ---------------------------------
import os
import re
import webbrowser
from time import sleep

# Classe para cores ---------------------------------
class color:
   p = '\033[95m'; c = '\033[96m'
   dc = '\033[36m'; bl = '\033[94m'
   g = '\033[92m'; y = '\033[93m'
   r = '\033[91m'; bo = '\033[1m'
   und = '\033[4m'; end = '\033[0m'
   i = '\x1B[3m';  w = '\033[37m'
   
class bg:
    bl = '\033[40m'; r = '\033[41m'
    g = '\033[42m'; y = '\033[43m'
    bl = '\033[44m'; m = '\033[45m'
    c = '\033[46m'; w = '\033[47m' 

# Criação de opções --------------------------------
options = ["Y", "N"]
      
# Criação de funções --------------------------------
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicialização - Menu Inicial -----------------------
Clear()
while True:
    videoSearch = input(f"{color.y}>>{color.end} Type something to search: ").strip()
    webLink = f"https://www.youtube.com/results?search_query={videoSearch}"
    
    sleep(0.5)
    print("Searching...")
    sleep(1)
    webbrowser.open(webLink)
    
    continueChoice = str(input(">> Do you want to continue? [Y/N] "))
    continueChoice = continueChoice.upper()
    
    while continueChoice not in options:
        Clear()
        continueChoice = str(input("*Choose between 'Y' or 'N'*\n>> Do you want to continue? [Y/N] "))
        continueChoice = continueChoice.upper()
        Clear()
    
    if continueChoice == "N":
        break