import os
import re
# SUBSTITUINDO CARACTERES ESPECIFICOS -----------------------------------------
        # import re
        # text = ["Ola\n", "Teste\n"]
        # print(text)
        # text = text[1]
        # text = re.sub('[\n]', '', text)
        # print(text)
        
# COLOCANDO COR EM TEXTO -----------------------------------------
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

def Clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# APRENDENDO A MANIPULAR ARQUIVOS .TXT -----------------------------------------
# with open("public/database.txt", "r", encoding="utf8") as teste:
#     conteudo = teste.readlines()
#     conteudo.append("\nteste;123")

# teste = open("public/database.txt", "w", encoding="utf8")
# teste.writelines(conteudo)
# teste.close()

# ATRIBUINDO ElEMENTOS DE UMA LISTA À VARIÁVEIS -----------------------------------------
# with open("public/database.txt", "r", encoding="utf8") as database:
#     banco = database.readlines()
# users = []
# passwords = []
# for line in banco:
#     valores = line.split(";")
#     user = valores[0]
#     users.append(valores[0])
#     password = valores[1]
#     passwords.append(valores[1])
#     print(f"=> User: {user}\n=> Password: {password}")
# print(users)
# print(passwords)

# passwords = []
# arquivo = open("public/database.txt", "r", encoding="utf8")
# conteudo = arquivo.readlines()
# for line in conteudo:
#         valores = line.split(";")
#         passwords.append(valores[2])
# print(passwords)

# ENTENDENDO COMO FUNCIONA APPEND() EM LISTA -----------------------------------------
# lista = []
# for x in range(0, 7):
#         print(x)
#         lista.append(x)
# print(lista)

# ACESSANDO ELEMENTOS ESPECÍFICOS EM UMA LISTA -----------------------------------------
# lista = ["banana", "maçã", "abacaxi", "manga"]
# elemento = "melão"
# conteudo = ""
# for i in lista:
#         if i == elemento:
#                 conteudo = i
#                 print(f"=> Elemento encontrado: {i}")
# if conteudo == "":
#         print("=> Elemento não encontrado")

# WHILE PARA ACESSAR ELEMENTOS ESPECÍFICOS -----------------------------------------
# opc = int(input("=>"))
# opcoes = [1, 2, 3]
# while opc in opcoes:
#         opc = int(input("=> "))
# print("opção certa")

# WHILE ENQUANTO FOR TRUE -----------------------------------------
        # execucao = True

        # while execucao:
        # print("=> Repetindo...")
        # opcao = str(input('Deseja continuar a repetir? [S/N] ')).upper().strip()
        # if opcao == 'N':
        #         execucao = False
        #         exit('Obrigado por usar nosso programa.')

# BUSCAR DADOS RELACIONADOS [USER, SENHA] -----------------------------------------
# def verificarUser():
#         def Login():
#                 arquivo = open("public/database.txt", "r", encoding="utf8")
#                 conteudo = arquivo.readlines()
#                 conta = None
#                 senha = None
#                 userQ = input("=> Informe seu user: ")
#                 for line in conteudo:
#                         valores = line.split(";")
                        
#                         if userQ == valores[1]:
#                                 name = valores[0]
#                                 user = valores[1]
#                                 password = valores[2]
#                                 conta = [name, user, password]
#                                 breakpoint
#                 return conta

#         conta = Login()
#         while conta == None:
#                 print("=> Usuário não encontrado! Deseja continuar?\n"
#                 "         [1] Continuar\n"
#                 "         [2] Sair")
#                 continuar = int(input("=> "))
#                 if continuar == 1:
#                         os.system('cls' if os.name == 'nt' else 'clear')
#                         conta = Login()
#                 elif continuar == 2:
#                         os.system('cls' if os.name == 'nt' else 'clear')
#                         break
                        
#         return conta[0], conta[1], conta[2]

# name, user, password = verificarUser()
# os.system('cls' if os.name == 'nt' else 'clear')
# print(f"=> {name}!")

# print(password)
# password = re.sub('[\n]', '', password)
# print(password)

# def VerificarSenha(password):
#         def Password():
#                 senha = input("=> Informe sua senha: ")
#                 return senha
        
#         senha = Password()
#         print(f"Senha: {senha}")
#         print(f"Password: {password}")
#         while senha != password:
#                 print("=> Senha incorreta! Deseja continuar?\n"
#                 "         [1] Continuar\n"
#                 "         [2] Sair")
#                 continuar = int(input("=> "))
#                 if continuar == 1:
#                         os.system('cls' if os.name == 'nt' else 'clear')
#                         senha = Password()
#                 elif continuar == 2:
#                         os.system('cls' if os.name == 'nt' else 'clear')
#                         break
# VerificarSenha(password)

# CRIAÇÃO DE CONTA -----------------------------------------
# def CriarConta():
#         def UsersCriados():
#                 arquivo = open("public/database.txt", "r", encoding="utf8")
#                 conteudo = arquivo.readlines()
#                 usersCriados = []
#                 for line in conteudo:
#                         valores = line.split(";")
#                         usersCriados.append(valores[1])
#                 return usersCriados
#         usersCriados = UsersCriados()
#         print(usersCriados)
#         name = input("=> Informe o seu nome: ")
#         user = input("=> Informe o user desejado: ")
        
#         while user in usersCriados:
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 print(f"=> {user} já está em uso!")
#                 user = input("=> Informe o user desejado: ")
                
#         password = int(input("=> Informe a sua senha (somente números): "))
#         password2 = int(input("=> Repita a sua senha: "))
        
#         while password != password2:
#                 os.system('cls' if os.name == 'nt' else 'clear')
#                 print(f"=> Senhas diferentes!")
#                 password = int(input("=> Informe a sua senha (somente números): "))
#                 password2 = int(input("=> Repita a sua senha: "))
                
#         return name, user, password
# name, user, password = CriarConta()
# os.system('cls' if os.name == 'nt' else 'clear')
# print(f"=> Nome: {name}")
# print(f"=> User: {user}")
# print(f"=> Senha: {password}")

# ATUALIZAR NA DATABASE -----------------------------------------
# def CriarConta():
#         def UsersCriados():
#                 arquivo = open("public/database.txt", "r", encoding="utf8")
#                 conteudo = arquivo.readlines()
#                 usersCriados = []
#                 for line in conteudo:
#                         valores = line.split(";")
#                         usersCriados.append(valores[1])
#                 return usersCriados
#         usersCriados = UsersCriados()
#         name = input("=> Informe o seu nome: ")
        
#         def User():
#             user = input("=> Informe o user desejado: ")
#             return user
        
#         user = User()
#         user = user.lower()
#         while user.lower() in usersCriados:
#             print(f"=> Usuário já está em uso! Deseja continuar?\n"
#             f"         {color.g}[1] Continuar{color.end}\n"
#             f"         {color.bo}{color.r}[2] Sair{color.end}")
#             continuar = int(input("=> "))
#             if continuar == 1:
#                     Clear()
#                     user = User()
#             elif continuar == 2:
#                     Clear()
#                     break
                
#         password = int(input("=> Informe a sua senha (somente números): "))
#         password2 = int(input("=> Repita a sua senha: "))          
#         while password != password2:
#                 Clear()
#                 print(f"{color.r}=> Senhas diferentes!{color.end}")
#                 password = int(input("=> Informe a sua senha (somente números): "))
#                 password2 = int(input("=> Repita a sua senha: "))
#         user = user.lower()
#         return name, user, password

# Clear()
# name, user, password = CriarConta()
# conta = f"{name};{user};{password}"
# print(conta)

# def AtualizarDB(conta):
#         arquivo = open("public/database.txt", "a", encoding="utf8")
#         arquivo.write(f"\n{conta}")

# AtualizarDB(conta)

# EXCLUIR NA DATABASE -----------------------------------------
# def ExcluirConta():
#         def ExcluirContaDB(userE, password):
#                 contas = []
#                 arquivo = open("public/database.txt", "r+", encoding="utf8")
#                 conteudo = arquivo.readlines()
#                 for line in conteudo:     
#                         valores = line.split(";")
#                         if (userE not in valores) and (password not in valores):
#                                 contas.append(valores)
                
#                 arquivo.truncate(0)
#                 arquivo.seek(0)
#                 for line in contas:
#                         arquivo.writelines(f"{line[0]};{line[1]};{line[2]}")

#                 return contas
#         def VerificarSenha(password):
#                 def Password():
#                         senha = input(f"{color.y}>>{color.end} Informe a senha do usuário: ")
#                         return senha
                
#                 senha = Password()
#                 while senha != password:
#                         Clear()
#                         print(f"{color.y}>>{color.end} Senha incorreta! Deseja continuar?\n"
#                         f"         {color.g}[1] Continuar{color.end}\n"
#                         f"         {color.bo}{color.r}[2] Sair{color.end}")
#                         continuar = int(input(f"{color.y}>>{color.end} "))
#                         if continuar == 1:
#                                 Clear()
#                                 senha = Password()
#                         elif continuar == 2:
#                                 Clear()
#                                 break
#                 if senha == password:
#                         Clear()
#         def verificarUser():
#                 def Login():
#                         arquivo = open("public/database.txt", "r", encoding="utf8")
#                         conteudo = arquivo.readlines()
#                         conta = False
#                         userE = input(f"{color.y}>>{color.end} Informe o user a ser excluído: ")
#                         for line in conteudo:
#                                 valores = line.split(";")
#                                 if userE == valores[1]:
#                                         password = valores[2]
#                                         conta = True
#                                         breakpoint
#                         return conta, userE, password
#                 conta, userE, password = Login()
#                 while conta == False:
#                         print(f"{color.y}>>{color.end} Usuário não encontrado! Deseja continuar?\n"
#                         f"         {color.g}[1] Continuar{color.end}\n"
#                         f"         {color.bo}{color.r}[2] Sair{color.end}")
#                         continuar = int(input("=> "))
#                         if continuar == 1:
#                                 Clear()
#                                 conta, userE = Login()
#                         elif continuar == 2:
#                                 Clear()
#                                 break
#                 return userE, password
#         userE, password = verificarUser()
#         password = password.strip("\n")
#         VerificarSenha(password)
#         ExcluirContaDB(userE, password)
#         return userE
# userE = ExcluirConta()
# print(f"{color.y}>> Conta excluída com sucesso! {color.end}")

# MUDANDO SENHA NA DATABASE -----------------------------------------
# def MudarSenha():
#         def MudarSenhaDB(userE, senhaE):
#                 contas = []
#                 arquivo = open("public/database copy.txt", "r+", encoding="utf8")
#                 conteudo = arquivo.readlines()
#                 for line in conteudo:     
#                         valores = line.split(";")
#                         if userE in valores:
#                                 senhaAntiga = valores[2]
#                                 valores = [f"{valores[0]}", f"{valores[1]}", f"{senhaE}\n"]
#                                 contas.append(valores)
#                         else:
#                                 contas.append(valores)
                
#                 arquivo.truncate(0)
#                 arquivo.seek(0)
#                 for line in contas:
#                         arquivo.writelines(f"{line[0]};{line[1]};{line[2]}")

#                 return senhaAntiga
#         Clear()
#         def verificarUser():
#                 def Login():
#                         arquivo = open("public/database.txt", "r", encoding="utf8")
#                         conteudo = arquivo.readlines()
#                         conta = False
#                         userE = input(f"{color.y}>>{color.end} Informe o user que vai ter a senha trocada: ")
#                         for line in conteudo:
#                                 valores = line.split(";")
#                                 if userE == valores[1]:
#                                         conta = True
#                                         breakpoint
#                         return conta, userE
#                 conta, userE = Login()
#                 while conta == False:
#                         print(f"{color.y}>>{color.end} Usuário não encontrado! Deseja continuar?\n"
#                         f"         {color.g}[1] Continuar{color.end}\n"
#                         f"         {color.bo}{color.r}[2] Sair{color.end}")
#                         continuar = int(input("=> "))
#                         if continuar == 1:
#                                 Clear()
#                                 conta, userE = Login()
#                         elif continuar == 2:
#                                 Clear()
#                                 break
#                 return userE

#         userE = verificarUser()
#         password = input(f"{color.y}>>{color.end} Informe a sua senha: ")
#         password2 = input(f"{color.y}>>{color.end} Repita a sua senha: ")        
#         while password != password2:
#                 Clear()
#                 print(f"{color.y}>> Senhas diferentes!{color.end}")
#                 password = input(f"{color.y}>>{color.end} Informe a sua senha: ")
#                 password2 = input(f"{color.y}>>{color.end} Repita a sua senha: ")
#         senhaE = password
        
#         senhaAntiga = MudarSenhaDB(userE, senhaE)
#         return senhaAntiga, senhaE
# senhaAntiga, senhaE = MudarSenha()
# senhaAntiga = senhaAntiga.strip("\n")
# Clear()
# print(f"{color.y}>> Senha alterada com sucesso! {color.end}")
# print(f"{color.y}>> Senha antiga: {color.end}{senhaAntiga}")
# print(f"{color.y}>> Senha atual: {color.end}{senhaE}")

# EDITAR ADMS ------------------------------------------------
# RETIRAR USERS COMO ADM ================
# arquivo = open("public/adms.txt", "r+", encoding="utf8")
# adms = arquivo.readlines()
# admsTemp = []
# userOutADM = 'admin'
# for adm in adms:
#         adm = adm.strip("\n")
#         if adm != userOutADM:
#                 admsTemp.append(adm)
# arquivo.truncate(0)
# arquivo.seek(0)
# for adm in admsTemp:
#         arquivo.writelines(f"{adm}\n")
        
# # ADICIONAR USERS COMO ADM =====================
# arquivo = open("public/adms.txt", "r+", encoding="utf8")
# adms = arquivo.readlines()
# userInADM = 'admin'
# arquivo.writelines(f"{userInADM}\n")

# # BUSCANDO USERS ADM ===================
# arquivo = open("public/adms.txt", "r+", encoding="utf8")
# conteudo = arquivo.readlines()
# adms = []
# for adm in adms:
#         adm = adm.strip("\n")
#         adms.append(adm)
# print(adms)

# TIRAR ESPAÇOS --------------------------------