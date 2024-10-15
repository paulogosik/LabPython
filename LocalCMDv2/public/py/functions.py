import os
import public.py.security as sec
import public.py.db as db

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    

def criar_usuario_comum():
    nome = str(input(f"=> Informe o seu nome: "))
    print("----------------------")
    usuario = verif_usuario()
    print("----------------------")
    senha = sec.criar_senha()
    
    db.insert_usuario_comum(nome, usuario, senha)
    print("----------------------")
    print(f"Usuário [{usuario}] criado com sucesso!")
    

def verif_usuario() -> str:
    while True:
        usuario = str(input(f"=> Informe o seu nome de usuário: "))
        
        if db.verif_nome_usuario(usuario):
            print("Este nome de usuário já esta em uso!")
        else:
            return usuario
        

def criar_admin():
    usuario = verif_usuario()
    print("----------------------")
    if db.verif_admin(usuario):
        
    print("----------------------")
    print(f"Usuário [{usuario}] promovido para administrador com sucesso!")