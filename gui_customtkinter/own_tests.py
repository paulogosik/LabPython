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

# try:
#     colecao.delete_one({"nome": "Paulo Gosik"})
    
#     print("Usuários deletados com sucesso!")
    
# except Exception as e:
#     print(f"Erro ao deletar: {e}")


import customtkinter as ctk
import bcrypt
from pymongo import MongoClient, collection

def connect_mongodb() -> collection.Collection:
    uri = "mongodb+srv://root:root123@testdb.abni7vh.mongodb.net/"
    client = MongoClient(uri)
    db = client["db_test"]
    return db["login"]


class FrameCriarConta(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master, fg_color="transparent")
        
        self._bg_color
        self.grid_columnconfigure(0, weight=1)
        
        self.usuario = ctk.CTkEntry(self, placeholder_text="Usuário", width=240)
        self.usuario.grid(row=0, column=0, padx=10, pady=(10, 0))
        
        self.nome = ctk.CTkEntry(self, placeholder_text="Nome", width=240)
        self.nome.grid(row=1, column=0, padx=10, pady=(10, 0))
        
        self.senha = ctk.CTkEntry(self, placeholder_text="Senha", show="*", width=240)
        self.senha.grid(row=2, column=0, padx=10, pady=(10, 0))
       
       
    def senha_hashed(self) -> str:
        senha = self.senha.get().encode("utf-8")
        return bcrypt.hashpw(senha, bcrypt.gensalt())
        
        
    def get(self) -> dict:
        values = {
            "_id": self.usuario.get(),
            "nome": self.nome.get(),
            "senha": self.senha_hashed()
        }
        
        return values
        

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("My Own Tests")
        self.geometry("1000x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        
        self.frame_criarconta = FrameCriarConta(self)
        self.frame_criarconta.grid(row=0, column=0, sticky="s")
        
        self.botao_enviar = ctk.CTkButton(self, text="Criar conta", command=self.botao_criarconta)
        self.botao_enviar.grid(row=1, column=0, pady=10, sticky="n")
        
        
    def botao_criarconta(self) -> None:
        # try:
        #     colecao.insert_one(self.frame_criarconta.get())
        #     print("Usuário criado com sucesso")
            
        # except Exception as e:
        #     print(f"Erro: {e}")
        print(self.frame_criarconta.get())
        
        
colecao = connect_mongodb()

app = App()
app.mainloop()