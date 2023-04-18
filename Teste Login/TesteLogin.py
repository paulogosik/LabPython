# Criação de funções
def CriarConta():
    name = input("=> Qual o seu nome? ")

# Classe para cores
class color:
   p = '\033[95m'; c = '\033[96m'
   dc = '\033[36m'; bl = '\033[94m'
   g = '\033[92m'; y = '\033[93m'
   r = '\033[91m'; bo = '\033[1m'
   und = '\033[4m'; end = '\033[0m'
   i = '\x1B[3m'
   

# Inicialização - Menu Inicial
print(f"==[ Bem-vindo à {color.i}{color.c}IM!{color.end}. Como posso te ajudar? ]==\n"
      f"    [1] Login\n"
      f"    [2] Criar conta")
opc = input("=> ")

print('')