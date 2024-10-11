import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'teste',
    'raise_on_warnings': True
}
conn = mysql.connector.connect(**config)


def insert_usuario_comum(nome: str, usuario: str, senha: str, funcao = "comum"):
    