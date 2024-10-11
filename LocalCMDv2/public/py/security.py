import hashlib
import string

def encode_password(senha: str) -> str:
    hash_object = hashlib.sha256(senha.encode())
    return hash_object.hexdigest()


def verif_maiuscula(senha: str) -> bool:
    return any(char.isupper() for char in senha)


def verif_numero(senha: str) -> bool:
    return any(char.isdigit() for char in senha)


def verif_char_especial(senha: str) -> bool:
    caracteres_especiais = string.punctuation
    return any(char in caracteres_especiais for char in senha)


def criar_senha() -> str:    
    while True:
        senha = str(input(f"*A senha deve conter no mínimo: 1 letra maiúscula, 1 número e 1 caracter especial.*\n=>Insira a sua senha: "))
        if verif_maiuscula(senha) and verif_numero(senha) and verif_char_especial(senha):
            return encode_password(senha)