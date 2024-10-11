import mysql.connector

config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'localcmd',
    'raise_on_warnings': True
}

def verif_nome_usuario(usuario: str) -> bool:
    """Função para verificar se o usuário já existe no banco de dados.
    Returns:
        bool: True: Usuário já existe no banco | False: Usuário não existe no banco.
    """
    
    lista_usuarios = []
    
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute("SELECT usuario FROM users_homol WHERE funcao = 'comum'")
    resultados = cursor.fetchall()
    for row in resultados:
        lista_usuarios.append(row[0])
             
    cursor.close()
    conn.close()
    
    if usuario in lista_usuarios:
        return True
    else:
        return False


def insert_usuario_comum(nome: str, usuario: str, senha: str):
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    
    query = """INSERT INTO users_homol(nome, usuario, senha, funcao)
                VALUES (%s, %s, %s, 'comum')"""
    argumentos = (nome, usuario, senha)
    cursor.execute(query, argumentos)
    conn.commit()
        
    cursor.close()
    conn.close()