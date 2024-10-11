import mysql.connector
import hashlib

# Conectando ao banco de dados ===========================
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'teste',
    'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

# Função para criptografar a senha ===========================
def encode_password(senha: str) -> str:
    hash_object = hashlib.sha256(senha.encode())
    return hash_object.hexdigest()