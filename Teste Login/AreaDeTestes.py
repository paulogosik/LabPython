import os
# SUBSTITUINDO CARACTERES ESPECIFICOS -----------------------------------------
        # import re
        # text = ["Ola\n", "Teste\n"]
        # print(text)
        # text = text[1]
        # text = re.sub('[\n]', '', text)
        # print(text)
        
# COLOCANDO COR EM TEXTO -----------------------------------------
# class color:
#         p = '\033[95m'
#         c = '\033[96m'
#         dc = '\033[36m'
#         bl = '\033[94m'
#         g = '\033[92m'
#         y = '\033[93m'
#         r = '\033[91m'
#         bo = '\033[1m'
#         und = '\033[4m'
#         end = '\033[0m'
#         i = '\x1B[3m'

# im = (f"{color.i}{color.c}Teste{color.end}")
# print(f"The output is: {im}")


# APRENDENDO A MANIPULAR ARQUIVOS .TXT -----------------------------------------
# with open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8") as teste:
#     conteudo = teste.readlines()
#     conteudo.append("\nteste;123")

# teste = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "w", encoding="utf8")
# teste.writelines(conteudo)
# teste.close()

# ATRIBUINDO ElEMENTOS DE UMA LISTA À VARIÁVEIS -----------------------------------------
# with open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8") as database:
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
# arquivo = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8")
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
# while opc not in opcoes:
#         opc = int(input("=> "))
# print("opção certa")

# BUSCAR DADOS RELACIONADOS -----------------------------------------
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
        print("=> Usuário não encontrado! Deseja continuar?\n"
        "         [1] Continuar\n"
        "         [2] Sair")
        continuar = int(input("=> "))
        if continuar == 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                conta = Login()
        elif continuar == 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                break
                
if conta != None:
        print("=> Usuário encontrado!") 
        print(conta)