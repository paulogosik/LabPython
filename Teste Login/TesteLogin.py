# Importações ---------------------------------
import os
import re
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
    
def VerificarSenha(password):
        def Password():
                senha = input("=> Informe sua senha: ")
                return senha
        
        senha = Password()
        while senha != password:
                print(f"=> Senha incorreta! Deseja continuar?\n"
                f"         {color.g}[1] Continuar{color.end}\n"
                f"         {color.bo}{color.r}[2] Sair{color.end}")
                continuar = input("=> ")
                if continuar == 1:
                        Clear()
                        senha = Password()
                elif continuar == 2:
                        Clear()
                        break
        if senha == password:
            Clear()

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
        def UsersCriados():
                arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
                conteudo = arquivo.readlines()
                usersCriados = []
                for line in conteudo:
                        valores = line.split(";")
                        usersCriados.append(valores[1])
                return usersCriados
        usersCriados = UsersCriados()
        name = input("=> Informe o seu nome: ")
        
        def User():
            user = input("=> Informe o user desejado: ")
            return user
        
        user = User()
        user = user.lower()
        while user.lower() in usersCriados:
            print(f"=> Usuário já está em uso! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input("=> "))
            if continuar == 1:
                    Clear()
                    user = User()
            elif continuar == 2:
                    Clear()
                    break
                
        password = input("=> Informe a sua senha: ")
        password2 = input("=> Repita a sua senha: ")        
        while password != password2:
                Clear()
                print(f"{color.r}=> Senhas diferentes!{color.end}")
                password = input("=> Informe a sua senha: ")
                password2 = input("=> Repita a sua senha: ")
        user = user.lower()
        return name, user, password

def AtualizarDB(conta):
        arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "a", encoding="utf8")
        arquivo.write(f"\n{conta}")

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

def OPC_Login():
    Clear()
    name, user, password = verificarUser()
    Clear()
    print(f"{color.g}=> Usuário encontrado!{color.end}")
    password = re.sub('[\n]', '', password)
    VerificarSenha(password)
    return name, user, password

def OPC_CriarConta():
    Clear()
    name, user, password = CriarConta()
    conta = f"{name};{user};{password}"
    AtualizarDB(conta)


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
    Clear()
    print(f"{color.r}=> Opção Inválida!{color.end} Esolha uma das opções abaixo:\n"
          f"    {color.g}[1] Login\n"
          f"    [2] Criar conta\n{color.end}"
          f"    {color.bo}{color.r}[3] Sair{color.end}")
    opc = int(input("=> "))

if opc == 1:
    name, user, password = OPC_Login()
    print(f"{color.g}=> Seja bem-vindo!{color.end}{color.bo} {name}{color.end}")
    
elif opc == 2:
    OPC_CriarConta()
    Clear()
    print(f"=> Conta criada! Deseja fazer o login? \n"
      f"    {color.g}[1] Login\n"
      f"    {color.bo}{color.r}[2] Sair{color.end}")
    login = int(input("=> "))
    
    if login == 1:
        Clear()
        name, user, password = OPC_Login()
        print(f"{color.g}=> Seja bem-vindo!{color.end}{color.bo} {name}{color.end}")
    else:
        Clear()
        breakpoint
        
elif opc == 3:
    Clear()
    breakpoint