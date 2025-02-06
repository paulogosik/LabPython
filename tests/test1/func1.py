import json

def line(c: str="-", n: int=30) -> None:
    print(c*n)
    

def fazer_login():
    print("")


def criar_conta():
    print("")
    

def menu() -> int:
    print("")
    line(c="*")
    print("Seja bem-vindo ao sistema de Login e Criação de Conta\n"
        "Escolha apenas uma opção para continuar:\n"
        "\t[ 1 ] Fazer login\n"
        "\t[ 2 ] Criar uma conta\n"
        "\t[ Outros ] Sair\n")
    opc = int(input(">>> "))
    
    if opc == 1:
        fazer_login()
    elif opc == 2:
        criar_conta()
    else:
        exit