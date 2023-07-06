# pyinstaller --onefile NomeArquivo.py/ pyinstaller --onefile -w NomeArquivo.py
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
    
def MudarSenha():
        def MudarSenhaDB(userE, senhaE):
                contas = []
                arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r+", encoding="utf8")
                conteudo = arquivo.readlines()
                for line in conteudo:     
                        valores = line.split(";")
                        if userE in valores:
                                senhaAntiga = valores[2]
                                valores = [f"{valores[0]}", f"{valores[1]}", f"{senhaE}\n"]
                                contas.append(valores)
                        else:
                                contas.append(valores)
                
                arquivo.truncate(0)
                arquivo.seek(0)
                for line in contas:
                        arquivo.writelines(f"{line[0]};{line[1]};{line[2]}")

                return senhaAntiga
        Clear()
        def verificarUser():
                def Login():
                        arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
                        conteudo = arquivo.readlines()
                        conta = False
                        userE = input(f"{color.y}>>{color.end} Informe o user que vai ter a senha trocada: ")
                        for line in conteudo:
                                valores = line.split(";")
                                if userE == valores[1]:
                                        conta = True
                                        breakpoint
                        return conta, userE
                conta, userE = Login()
                while conta == False:
                        print(f"{color.y}>>{color.end} Usuário não encontrado! Deseja continuar?\n"
                        f"         {color.g}[1] Continuar{color.end}\n"
                        f"         {color.bo}{color.r}[2] Sair{color.end}")
                        continuar = int(input("=> "))
                        if continuar == 1:
                                Clear()
                                conta, userE = Login()
                        elif continuar == 2:
                                Clear()
                                exit()
                return userE

        userE = verificarUser()
        password = input(f"{color.y}>>{color.end} Informe a sua senha: ")
        password2 = input(f"{color.y}>>{color.end} Repita a sua senha: ")        
        while password != password2:
                Clear()
                print(f"{color.y}>> Senhas diferentes!{color.end}")
                password = input(f"{color.y}>>{color.end} Informe a sua senha: ")
                password2 = input(f"{color.y}>>{color.end} Repita a sua senha: ")
        senhaE = password
        
        senhaAntiga = MudarSenhaDB(userE, senhaE)
        return senhaAntiga, senhaE

def ExcluirConta():
        def ExcluirContaDB(userE, password):
                contas = []
                arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r+", encoding="utf8")
                conteudo = arquivo.readlines()
                for line in conteudo:     
                        valores = line.split(";")
                        if (userE not in valores) and (password not in valores):
                                contas.append(valores)
                
                arquivo.truncate(0)
                arquivo.seek(0)
                for line in contas:
                        arquivo.writelines(f"{line[0]};{line[1]};{line[2]}")

                return contas
        def VerificarSenha(password):
                def Password():
                        senha = input(f"{color.y}>>{color.end} Informe a senha do usuário: ")
                        return senha
                
                senha = Password()
                while senha != password:
                        Clear()
                        print(f"{color.y}>>{color.end} Senha incorreta! Deseja continuar?\n"
                        f"         {color.g}[1] Continuar{color.end}\n"
                        f"         {color.bo}{color.r}[2] Sair{color.end}")
                        continuar = int(input(f"{color.y}>>{color.end} "))
                        if continuar == 1:
                                Clear()
                                senha = Password()
                        elif continuar == 2:
                                Clear()
                                exit()
                if senha == password:
                        Clear()
        def verificarUser():
                def Login():
                        arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
                        conteudo = arquivo.readlines()
                        conta = False
                        userE = input(f"{color.y}>>{color.end} Informe o user a ser excluído: ")
                        for line in conteudo:
                                valores = line.split(";")
                                if userE == valores[1]:
                                        password = valores[2]
                                        conta = True
                                        breakpoint
                        return conta, userE, password
                conta, userE, password = Login()
                while conta == False:
                        print(f"{color.y}>>{color.end} Usuário não encontrado! Deseja continuar?\n"
                        f"         {color.g}[1] Continuar{color.end}\n"
                        f"         {color.bo}{color.r}[2] Sair{color.end}")
                        continuar = int(input("=> "))
                        if continuar == 1:
                                Clear()
                                conta, userE = Login()
                        elif continuar == 2:
                                Clear()
                                exit()
                return userE, password
        userE, password = verificarUser()
        password = password.strip("\n")
        VerificarSenha(password)
        ExcluirContaDB(userE, password)
        return userE
   
def VerificarSenha(password):
        def Password():
            senha = input("=> Informe sua senha: ")
            return senha
        
        senha = Password()
        while senha != password:
            Clear()
            print(f"=> Senha incorreta! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input("=> "))
            if continuar == 1:
                    Clear()
                    senha = Password()
            elif continuar == 2:
                    Clear()
                    exit()
        if senha == password:
            Clear()

def VerificarSenhaAdmin(password):
        def Password():
            senha = input(f"{color.y}>>{color.end} Informe sua senha: ")
            return senha
        
        senha = Password()
        while senha != password:
            Clear()
            print(f"{color.y}>>{color.end} Senha incorreta! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input(f"{color.y}>>{color.end} "))
            if continuar == 1:
                    Clear()
                    senha = Password()
            elif continuar == 2:
                    Clear()
                    exit()
        if senha == password:
            Clear()

def verificarUserAdmin():
    adms = BuscarADMs()
    def Login():
            arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
            conteudo = arquivo.readlines()
            conta = False
            userE = input(f"{color.y}>>{color.end} Informe o user que será Admin: ")
            for line in conteudo:
                    valores = line.split(";")
                    if userE == valores[1]:
                            conta = True
                            breakpoint
            return conta, userE
    conta, userE = Login()
    while conta == False:
            print(f"{color.y}>>{color.end} Usuário não encontrado! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input("=> "))
            if continuar == 1:
                    Clear()
                    conta, userE = Login()
            elif continuar == 2:
                    Clear()
                    exit()
    while userE in adms:
        print(f"{color.y}>>{color.end} Usuário é um Admin! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
        continuar = int(input(f"{color.y}>>{color.end} "))
        if continuar == 1:
                Clear()
                conta, userE = Login()
        elif continuar == 2:
                Clear()
                exit()
    return userE

def verificarUserDelAdmin():
    adms = BuscarADMs()
    def Login():
            arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
            conteudo = arquivo.readlines()
            conta = False
            userE = input(f"{color.y}>>{color.end} Informe o user para tirar a função Admin: ")
            for line in conteudo:
                    valores = line.split(";")
                    if userE == valores[1]:
                            conta = True
                            breakpoint
            return conta, userE
    conta, userE = Login()
    while conta == False:
            print(f"{color.y}>>{color.end} Usuário não encontrado! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input("=> "))
            if continuar == 1:
                    Clear()
                    conta, userE = Login()
            elif continuar == 2:
                    Clear()
                    exit()
    while userE not in adms:
        print(f"{color.y}>>{color.end} Usuário não é um Admin! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
        continuar = int(input(f"{color.y}>>{color.end} "))
        if continuar == 1:
                Clear()
                conta, userE = Login()
        elif continuar == 2:
                Clear()
                exit()
    return userE
    
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
                    exit()
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
                    exit()
        password = input("=> Informe a sua senha: ")
        password2 = input("=> Repita a sua senha: ")        
        while password != password2:
                Clear()
                print(f"{color.r}=> Senhas diferentes!{color.end}")
                password = input("=> Informe a sua senha: ")
                password2 = input("=> Repita a sua senha: ")
        user = user.lower()
        return name, user, password

def CriarAdmin():
    def VerificarSenhaAdmin(password):
        def Password():
            senha = input(f"{color.y}>>{color.end} Informe sua senha: ")
            return senha
        senha = Password()
        while senha != password:
            Clear()
            print(f"{color.y}>>{color.end} Senha incorreta! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input(f"{color.y}>>{color.end} "))
            if continuar == 1:
                    Clear()
                    senha = Password()
            elif continuar == 2:
                    Clear()
                    exit()
        if senha == password:
            Clear()
    userE = verificarUserAdmin()
    VerificarSenhaAdmin(password)
    arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/adms.txt", "r+", encoding="utf8")
    adms = arquivo.readlines()
    arquivo.writelines(f"{userE}\n")
    return userE

def DeleteAdmin():
    def VerificarSenhaAdmin(password):
        def Password():
            senha = input(f"{color.y}>>{color.end} Informe sua senha: ")
            return senha
        senha = Password()
        while senha != password:
            Clear()
            print(f"{color.y}>>{color.end} Senha incorreta! Deseja continuar?\n"
            f"         {color.g}[1] Continuar{color.end}\n"
            f"         {color.bo}{color.r}[2] Sair{color.end}")
            continuar = int(input(f"{color.y}>>{color.end} "))
            if continuar == 1:
                    Clear()
                    senha = Password()
            elif continuar == 2:
                    Clear()
                    exit()
        if senha == password:
            Clear()
    userE = verificarUserDelAdmin()
    VerificarSenhaAdmin(password)
    arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/adms.txt", "r+", encoding="utf8")
    adms = arquivo.readlines()
    admsTemp = []
    for adm in adms:
            adm = adm.strip("\n")
            if adm != userE:
                    admsTemp.append(adm)
    arquivo.truncate(0)
    arquivo.seek(0)
    for adm in admsTemp:
            arquivo.writelines(f"{adm}\n")
    return userE

def AtualizarDB(conta):
        arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r+", encoding="utf8")
        arquivo.close()
        
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

def BuscarContas():
    contas = []
    arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
    conteudo = arquivo.readlines()
    for line in conteudo:
        valores = line.split(";")
        contas.append(valores)
    
    return contas

def BuscarADMs():
    arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/adms.txt", "r+", encoding="utf8")
    conteudo = arquivo.readlines()
    adms = []
    for adm in conteudo:
            adm = adm.strip("\n")
            adms.append(adm)
    return adms

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
    
def MenuADM():
    logs = ["sair", "clear", "names", "users", "inf", "acts", "cpw", "dact", "vadmin", "cradm", "deadm"]
    log = input(f"{color.y}>> {color.end}")
    while log not in logs:
        log = input(f"{color.y}>> {color.end}")
        
    if log == "clear":
        Clear()
    elif log == "names":
        i = 1
        for name in names:
            print(f"    {color.bl}{i}.{color.end} {name}")
            i += 1
    elif log == "users":
        i = 1
        for user in users:
            print(f"    {color.bl}{i}.{color.end} {user}")
            i += 1
    elif log == "inf":
        Clear()
        print(f"{color.y}>> {color.end} Funções:")
        for log in logs:
            print(f"   • {color.y}[{log}]{color.end}")
    elif log == "acts":
        i = 1
        contas = BuscarContas()
        for conta in contas:
            conta[2] = conta[2].strip("\n")
            print(f"   {color.y}{i}. Nome:{color.end} {conta[0]} | "
                  f"{color.y}User:{color.end} {conta[1]} | "
                  f"{color.y}Senha:{color.end} {conta[2]}")
            i += 1
    elif log == "cpw":
        senhaAntiga, senhaE = MudarSenha()
        senhaAntiga = senhaAntiga.strip("\n")
        Clear()
        print(f"{color.y}>> Senha alterada com sucesso! {color.end}")
        print(f"{color.y}>> Senha antiga: {color.end}{senhaAntiga}")
        print(f"{color.y}>> Senha atual: {color.end}{senhaE}")
    elif log == "dact":
        Clear()
        userE = ExcluirConta()
        print(f"{color.y}>> Conta excluída com sucesso! {color.end}")
    elif log == "vadmin":
        Clear()
        print(f"{color.y}>> {color.end}Admins:")
        adms = BuscarADMs()
        i = 1
        for adm in adms:
            print(f"    {color.y}{i}.{color.end} {adm}")
            i += 1
    elif log == "cradm":
        Clear()
        userE = CriarAdmin()
        print(f"{color.y}>> {userE}{color.end} agora é um Admin.")
    elif log == "deadm":
        Clear()
        userE = DeleteAdmin()
        print(f"{color.y}>> {userE}{color.end} não é mais um Admin.")
               
    return log

def Menu(name, user, password):
    logs = ["sair", "clear", "names", "inf", "my inf"]
    log = input(f"{color.bl}>> {color.end}")
    while log not in logs:
        log = input(f"{color.bl}>> {color.end}")
        
    if log == "clear":
        Clear()
    elif log == "names":
        i = 1
        for name in names:
            print(f"    {color.bl}{i}.{color.end} {name}")
            i += 1
    elif log == "inf":
        Clear()
        print(f"{color.bl}>> {color.end} Funções:")
        for log in logs:
            print(f"   • {color.bl}{log}{color.end}")
    elif log == "my inf":
        print(f"{color.bl}>> Nome:{color.end} {name} | "
                f"{color.bl}User:{color.end} {user} | "
                f"{color.bl}Senha:{color.end} {password}")
        
    return log
    

# Inicialização - Menu Inicial -----------------------
Clear()
names = BuscarNames()
users = BuscarUsers()
passwords = BuscarPasswords()
contas = BuscarContas()
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
    else:
        Clear()
        exit()
        
elif opc == 3:
    Clear()
    exit()

adm = False

adms = BuscarADMs()

if user in adms:
    adm = True
    print(f"{color.g}=> Seja bem-vindo!{color.end}{color.bo} {name}{color.end}{color.y} [ADM] {color.end}")
else: 
    print(f"{color.g}=> Seja bem-vindo!{color.end}{color.bo} {name}{color.end}")

if adm == True:
    log = MenuADM()
    while log != "sair":
        log = MenuADM()
    Clear()
elif adm == False:    
    log = Menu(name, user, password)
    while log != "sair":
        log = Menu(name, user, password)
    Clear()