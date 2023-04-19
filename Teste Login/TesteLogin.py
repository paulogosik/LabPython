# Criação de funções
def CriarConta():
    name = input("=> Informe o seu nome: ")
    name = name.title()
    user = input("=> Informe o seu user")

# Classe para cores
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
   

# Inicialização - Menu Inicial
print(f"{color.w}==[ Bem-vindo à {color.i}{color.c}IM!{color.end}. Como posso te ajudar? ]==\n"
      f"    [1] Login\n"
      f"    [2] Criar conta\n"
      f"    {color.bo}{color.r}[3] Sair{color.end}")
opc = input("=> ")

print('')