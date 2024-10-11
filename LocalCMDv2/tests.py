import mysql.connector
import public.py.security as sec
import public.py.functions as func
import public.py.db as db

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
    

# Criptografando a senha =================================
# print("--------------------------------")
# senha = "minha_senha_secreta"
# senha_criptografada = sec.encode_password(senha)
# print(f'Senha criptografada: {senha_criptografada}')


# Função para criar a senha ======================
# def criar_senha() -> str:    
#     while True:
#         senha = str(input(f"*A senha deve conter no mínimo: 1 letra maiúscula, 1 número e 1 caracter especial.*\n=>Insira a sua senha: "))
#         if sec.verif_maiuscula(senha) and sec.verif_numero(senha) and sec.verif_char_especial(senha):
#             break

#     return senha
        

# Criando um usuário ============================= //TODO 1
def criar_usuario_comum():
    nome = str(input(f"=> Informe o seu nome: "))
    usuario = str(input(f"=> Informe o seu nome de usuário: "))
    senha = sec.criar_senha()
    
    db.insert_usuario_comum(nome, usuario, senha)
    

# Parte para testes ========================
func.clear()


# Comentários -=-=--=-=-=-==-==-=-==--=-=-=-=-=-=-=-=-=-=-=-=-=-=-
'''
    //TODO 1: 
    Estou no meio do desenvolvimento da função 'criar_usuario_comum'.
    Preciso colocar uma validação para ver se o usuário não existe.
'''