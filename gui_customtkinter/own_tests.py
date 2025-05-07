# # Inserir múltiplos
# colecao.insert_many([
#     {"nome": "Maria", "idade": 30},
#     {"nome": "Pedro", "idade": 22}
# ])

# # Buscar com filtro
# resultados = colecao.find({"idade": {"$gte": 25}})
# for pessoa in resultados:
#     print(pessoa)

# # Atualizar
# colecao.update_one({"nome": "João"}, {"$set": {"idade": 26}})

# # Deletar
# colecao.delete_one({"nome": "Pedro"})


# ------------------------------------------------------------------------------
# try:
#     colecao.delete_one({"nome": "Paulo Gosik"})
    
#     print("Usuários deletados com sucesso!")
    
# except Exception as e:
#     print(f"Erro ao deletar: {e}")


# ------------------------------------------------------------------------------
# for i in colecao.find({"_id": "userteste"}):
#     print(i["senha"])
#     senha = "teste123@".encode("utf-8")
#     print(senha)
#     print(bcrypt.checkpw(senha, i["senha"]))


# ------------------------------------------------------------------------------
# usuario = self.frame_criarconta.usuario.get().strip()
# nome = self.frame_criarconta.nome.get().strip()
# senha = self.frame_criarconta.senha.get().strip()

# if not usuario:
#     print("not usuario")
# if not nome:
#     print("not nome")
# if not senha:
#     print("not senha")


# ------------------------------------------------------------------------------
# def botao_criarconta(self) -> None:
#     try:
#         colecao.insert_one(self.frame_criarconta.get())
#         self.label_mensagem.configure(text="Usuário criado com sucesso!", text_color="green")
#     except Exception as e:
#         self.label_mensagem.configure(text=f"Erro: {e}", text_color="red")


# ------------------------------------------------------------------------------

import customtkinter as ctk
import bcrypt
from pymongo import MongoClient, collection
from pymongo.errors import DuplicateKeyError
import re

def connect_mongodb() -> collection.Collection:
    uri = "mongodb+srv://root:root123@testdb.abni7vh.mongodb.net/"
    client = MongoClient(uri)
    db = client["db_test"]
    return db["login"]


class FrameCriarConta(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        self.grid_columnconfigure(0, weight=1)
        
        self.usuario = ctk.CTkEntry(self, placeholder_text="Usuário", width=240)
        self.usuario.grid(row=0, column=0, padx=10, pady=(10, 0))
        
        self.email = ctk.CTkEntry(self, placeholder_text="E-mail", width=240)
        self.email.grid(row=1, column=0, padx=10, pady=(10, 0))
        
        self.nome = ctk.CTkEntry(self, placeholder_text="Nome Completo", width=240)
        self.nome.grid(row=2, column=0, padx=10, pady=(10, 0))
        
        self.senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=240)
        self.senha.grid(row=3, column=0, padx=10, pady=(10, 0))
        
        self.senha2 = ctk.CTkEntry(self, placeholder_text="Digite a senha novamente", show="*", width=240)
        self.senha2.grid(row=4, column=0, padx=10, pady=(10, 0))
        
        self.bota_facalogin = ctk.CTkButton(
            self,
            text="Já tem conta? Faça Login",
            fg_color="transparent",
            hover_color="gray14",
            command=master.botao_facalogin,
            text_color="#6495ED"
            )
        self.bota_facalogin.grid(row=5, column=0, pady=(40, 0))
        
        self.botao_enviar = ctk.CTkButton(
            self,
            text="Criar conta",
            command=master.botao_criarconta,
            width=240,
            fg_color="#6959CD",
            hover_color="#483D8B"
            )
        self.botao_enviar.grid(row=6, column=0)
        
        self.label_aviso = ctk.CTkLabel(self, text="", text_color="red")
        self.label_aviso.grid(row=7, column=0)
       
       
    def verificar_senha(self) -> bool:
        tem_maiuscula = re.search(r'[A-Z]', self.senha.get())
        tem_numero = re.search(r'[0-9]', self.senha.get())
        tem_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', self.senha.get())

        return all([tem_maiuscula, tem_numero, tem_especial])
       
       
    def senha_hashed(self) -> str:
        senha = self.senha.get().encode("utf-8")
        return bcrypt.hashpw(senha, bcrypt.gensalt())
        
        
    def get(self) -> dict:
        values = {
            "_id": self.usuario.get(),
            "email": self.email.get(),
            "nome": self.nome.get(),
            "senha": self.senha_hashed()
        }
        
        return values
        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Criar Conta")
        self.geometry("1280x720")
        # self.state("zoomed")
        self.iconbitmap("C:/Users/Teste/Documents/LabPython/gui_customtkinter/img/urano.ico")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        
        self.frame_criarconta = FrameCriarConta(self)
        self.frame_criarconta.grid(row=0, column=0)


    def botao_facalogin(self) -> None:
        print("Faça Login")

        
    def botao_criarconta(self) -> None:
        usuario = self.frame_criarconta.usuario.get().strip()
        email = self.frame_criarconta.email.get().strip()
        nome = self.frame_criarconta.nome.get().strip()
        senha1 = self.frame_criarconta.senha.get().strip()
        senha2 = self.frame_criarconta.senha2.get().strip()
        
        # Verifica se todos os campos estão preenchidos
        if not usuario or not email or not nome or not senha1 or not senha2:
            self.frame_criarconta.label_aviso.configure(text="Preencha todos os campos!", text_color="red")
            return
        
        # Verifica se todos os requisitos de senha estão válidos
        if not self.frame_criarconta.verificar_senha():
            self.frame_criarconta.label_aviso.configure(text="A senha deve conter letra maiúscula, número e caracter especial.",text_color="red")
            return
        
        # Verifica se as duas senhas são iguais
        if self.frame_criarconta.senha.get() != self.frame_criarconta.senha2.get():
            self.frame_criarconta.label_aviso.configure(text="As senhas não são iguais!", text_color="red")
            return
        
        # Tenta a conexão com o banco e cria/acusa o erro
        try:
            colecao.insert_one(self.frame_criarconta.get())
            self.frame_criarconta.label_aviso.configure(text="Usuário criado com sucesso!", text_color="green")
            
        except DuplicateKeyError as e:
            self.frame_criarconta.label_aviso.configure(text="Este nome de usuário já existe!", text_color="red")
        
        
colecao = connect_mongodb()
app = App()
app.mainloop()