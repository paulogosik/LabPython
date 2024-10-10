import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'teste',
    'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

# try:
#     conn = mysql.connector.connect(**config)
#     if conn.is_connected():
#         print("Conexão bem-sucedida!")
# except mysql.connector.Error as err:
#     print(f"Erro ao conectar: {err}")

cursor = conn.cursor()

cursor.execute("SELECT * FROM tabela")
resultados = cursor.fetchall()

print("Nome | Descrição")
for linha in resultados:
    print(f"{linha[1]} | {linha[2]}")