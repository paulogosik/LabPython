# COLOCANDO COR EM TEXTO
class color:
        p = '\033[95m'
        c = '\033[96m'
        dc = '\033[36m'
        bl = '\033[94m'
        g = '\033[92m'
        y = '\033[93m'
        r = '\033[91m'
        bo = '\033[1m'
        und = '\033[4m'
        end = '\033[0m'
        i = '\x1B[3m'

im = (f"{color.i}{color.c}Teste{color.end}")
print(f"The output is: {im}")



# with open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8") as teste:
#     conteudo = teste.readlines()
#     conteudo.append("\nteste;123")

# teste = open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "w", encoding="utf8")
# teste.writelines(conteudo)
# teste.close()

with open("//10.8.0.37/usuarios$/109103/Meus Documentos/testes/LabPython/Teste Login/database.txt", "r", encoding="utf8") as database:
    banco = database.readlines()
#     print(banco)
users = []
passwords = []
for line in banco:
    valores = line.split(";")
    user = valores[0]
    users.append(valores[0])
    password = valores[1]
    passwords.append(valores[1])
    print(f"=> User: {user}\n=> Password: {password}")
print(users)
print(passwords)

# Entendendo como funciona Append() em lista
# lista = []
# for x in range(0, 7):
#         print(x)
#         lista.append(x)
# print(lista)