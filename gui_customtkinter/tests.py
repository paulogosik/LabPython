# import customtkinter as ctk
# import requests

# # Configurar aparência
# ctk.set_appearance_mode("System")
# ctk.set_default_color_theme("blue")

# # Função para buscar dados
# def buscar_dados():
#     response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
#     if response.status_code == 200:
#         dados = response.json()
#         label_resultado.configure(text=f'Título: {dados["title"]}')
#     else:
#         label_resultado.configure(text="Erro ao buscar dados!")

# # Criar janela
# app = ctk.CTk()
# app.geometry("1000x600")
# app.title("API com Tkinter")

# # Botão
# botao_buscar = ctk.CTkButton(app, text="Buscar Dados", command=buscar_dados)
# botao_buscar.pack(pady=20)

# # Resultado
# label_resultado = ctk.CTkLabel(app, text="")
# label_resultado.pack(pady=10)

# # Rodar app
# app.mainloop()

# -----------------------------------------------------------------------------------------------

# import customtkinter as ctk

# #função para o botão
# def botao_print() -> None:
#     print("teste")

# # o 'app' é quando você cria uma janela, e pode usar ele mesmo para controlar a janela
# app = ctk.CTk()
# app.geometry("1000x600")
# app.title("My App")
# # app.grid_columnconfigure(0, weight=1) # configurando a coluna 0 com o peso 1 (inteira), página inteira horizontalmente
# # app.grid_rowconfigure(0, weight=1) # configurando a linha 1 para pegar a página inteira verticalmente

# # criando um botão e chamando a função dele
# btn_print = ctk.CTkButton(app, text="Printar 'teste'", command=botao_print)
# btn_print.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
#     # sticky vai grudar dos lados da coluna
#     # columnspan=2 vai fazer a coluna ter o tamanho de 2 colunas

# #criando checkboxes
# checkbox1 = ctk.CTkCheckBox(app, text="Checkbox 1")
# checkbox1.grid(row=1, column=0, padx=20, pady=(0, 20))
# checkbox2 = ctk.CTkCheckBox(app, text="Checkbox 2")
# checkbox2.grid(row=1, column=1, padx=20, pady=(0, 20))

# app.mainloop()

# -----------------------------------------------------------------------------------------------
    # Usando classe para organizar melhor
    
import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        def botao_print() -> None:
            print("teste")
        
        self.geometry("1000x600")
        self.title("My App")
        self.grid_columnconfigure((0, 1), weight=1)

        btn_print = ctk.CTkButton(self, text="Printar 'teste'", command=botao_print)
        btn_print.grid(row=0, column=0, padx=20, pady=20, columnspan=2)

        checkbox1 = ctk.CTkCheckBox(self, text="Checkbox 1")
        checkbox1.grid(row=1, column=0, padx=20, pady=(0, 20))
        checkbox2 = ctk.CTkCheckBox(self, text="Checkbox 2")
        checkbox2.grid(row=1, column=1, padx=20, pady=(0, 20))
        
app = App()
app.mainloop()        
        