# Importações ---------------------------------
import os
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
    
    
# Criação de funções --------------------------------
def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def verificarUser():
    def Login():
        arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
        conteudo = arquivo.readlines()
        conta = None
        userQ = input("=> Informe seu user: ")
        for line in conteudo:
                valores = line.split(";")
                
                if userQ == valores[1]:
                        name = valores[0]
                        user = valores[1]
                        password = valores[2]
                        conta = [name, user, password]
                        breakpoint
        return conta
    conta = Login()
    while conta == None:
            print(f"=> Usuário não encontrado! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input("=> "))
            if continuar == 1:
                    Clear()
                    conta = Login()
            elif continuar == 2:
                    Clear()
                    break
    return conta[0], conta[1], conta[2]              

def CriarConta():
    print("hello, world")

def EntrarConta():
    print("hello, world")

def BuscarPasswords():
    passwords = []
    arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for line in conteudo:
        valores = line.split(";")
        passwords.append(valores[2])
    
    return passwords
    
def BuscarUsers():
    users = []
    arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for line in conteudo:
        valores = line.split(";")
        users.append(valores[1])
    
    return users

def BuscarNames():
    names = []
    arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for line in conteudo:
        valores = line.split(";")
        names.append(valores[0])
    
    return names   


# Inicialização - Menu Inicial -----------------------
names = BuscarNames()
users = BuscarUsers()
passwords = BuscarPasswords()
print(f"==[ Bem-vindo à {color.i}{color.c}IM!{color.end}. Como posso te ajudar? ]==\n"
      f"    {color.g}[1] Login\n"
      f"    [2] Criar conta\n{color.end}"
      f"    {color.bo}{color.r}[3] Sair{color.end}")
opc = int(input("=> "))


opcoes = [1, 2, 3]
while opc not in opcoes:
    print(f"{color.r}=> Opção Inválida!{color.end} Esolha uma das opções abaixo:\n"
          f"    {color.g}[1] Login\n"
          f"    [2] Criar conta\n{color.end}"
          f"    {color.bo}{color.r}[3] Sair{color.end}")
    opc = int(input("=> "))

if opc == 1:
    Clear()
    name, user, password = verificarUser()
    Clear()
    print(f"{color.g}=> Usuário encontrado!{color.end} Seja bem-vindo, {name}.")
    
elif opc == 2:
    Clear()
    print("Opção 2")
    
elif opc == 3:
    Clear()
    print("Opção 3")
