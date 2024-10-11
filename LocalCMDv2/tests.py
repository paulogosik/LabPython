import mysql.connector
import hashlib


# Configurações para o MySQL ============================
config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'teste',
    'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)


# Exceções para erros ============================
# try:
#     conn = mysql.connector.connect(**config)
#     if conn.is_connected():
#         print("Conexão bem-sucedida!")
# except mysql.connector.Error as err:
#     print(f"Erro ao conectar: {err}")


# Testando a conexão do banco de dados ==============================
# cursor = conn.cursor()

# cursor.execute("SELECT * FROM tabela")
# resultados = cursor.fetchall()

# print("Nome | Descrição")
# for linha in resultados:
#     print(f"{linha[1]} | {linha[2]}")
    

def encode_password(senha: str) -> str:
    hash_object = hashlib.sha256(senha.encode())
    return hash_object.hexdigest()

print("--------------------------------")
senha = "minha_senha_secreta"
senha_criptografada = encode_password(senha)
print(f'Senha criptografada: {senha_criptografada}')