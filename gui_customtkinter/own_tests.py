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


import customtkinter as ctk
from pymongo import MongoClient, collection

def connect_mongodb() -> collection.Collection:
    uri = "mongodb+srv://root:root123@testdb.abni7vh.mongodb.net/"
    client = MongoClient(uri)
    db = client["db_test"]
    return db["login"]
    

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("My Own Tests")
        self.geometry("1000x600")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1, 2), weight=1)
        
        self.usuario = ctk.CTkEntry(self, placeholder_text="Usuário", width=200)
        self.usuario.grid(row=0, column=0, padx=10, pady=10)
        self.senha = ctk.CTkEntry(self, placeholder_text="Senha", width=200)
        self.senha.grid(row=1, column=0, padx=10, pady=10)
        
        
colecao = connect_mongodb()

for doc in colecao.find():
    print(doc)

# app = App()
# app.mainloop()