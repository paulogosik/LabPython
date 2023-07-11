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
    ba = '\033[40m'; r = '\033[41m'
    g = '\033[42m'; y = '\033[43m'
    bl = '\033[44m'; m = '\033[45m'
    c = '\033[46m'; w = '\033[47m' 

class char:
    key = '{' ; ckey = '}'

# Criação de opções --------------------------------
options = ["Y", "N"]
      
# Criação de funções --------------------------------
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def YouTubeSearch():
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

def GoogleSearch():
    Clear()
    while True:
        search = input(f"{color.y}>>{color.end} Type something to search: ").strip()
        webLink = f"https://www.google.com/search?q={search}"
        
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
        
# Inicialização - Menu Inicial -----------------------
while True:
    Clear()
    print(f"{color.r}{color.bo}==================({char.key}< CONNECT_WEB >{char.ckey})=================={color.end}")
    print(f"{color.y}>>{color.end}    {color.i}{color.g}[cw --open -ggl]{color.end} To open the Google website\n"
          f"{color.y}>>{color.end}    {color.i}{color.g}[cw --search -ggl]{color.end} To search something on Google\n"
          f"{color.y}>>{color.end}    {color.i}{color.g}[cw --open -yt]{color.end} To open the YouTube website\n"
          f"{color.y}>>{color.end}    {color.i}{color.g}[cw --search -yt]{color.end} To search something on YouTube")
    opc = input(f"{color.y}{color.i}>> ")
    
    if opc == "exit":
        Clear()
        break
    elif opc == "cw --open -ggl":
        webbrowser.open_new_tab("https://google.com")
    elif opc == "cw --search -ggl":
        GoogleSearch()
    elif opc == "cw --open -yt":
        webbrowser.open_new_tab("https://youtube.com")
    elif opc == "cw --search -yt":
        YouTubeSearch()