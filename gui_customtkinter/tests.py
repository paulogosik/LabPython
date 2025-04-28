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
    
# import customtkinter as ctk

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
        
#         self.geometry("1000x600")
#         self.title("My App")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure((0, 1), weight=2)

#         # checkbox1 = ctk.CTkCheckBox(self, text="Checkbox 1")
#         # checkbox1.grid(row=0, column=1, padx=20, pady=(0, 20), sticky="w")
#         # checkbox2 = ctk.CTkCheckBox(self, text="Checkbox 2")
#         # checkbox2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
        
#         self.checkbox_frame = ctk.CTkFrame(self)
#         self.checkbox_frame.grid(row=0, column=0, padx=20, pady=(10, 10), sticky="s")
        
#         self.checkbox_1 = ctk.CTkCheckBox(self.checkbox_frame, text="CheckBox 1")
#         self.checkbox_1.grid(row=0, column=0, padx=20, pady=(10, 10))
        
#         self.checkbox_2 = ctk.CTkCheckBox(self.checkbox_frame, text="CheckBox 2")
#         self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 10))
        
#         btn_print = ctk.CTkButton(self, text="Printar 'teste'", command=self.botao_print)
#         btn_print.grid(row=1, column=0, padx=20, pady=20, sticky="n")
        
        
#     def botao_print(self) -> None:
#         print("teste")
        
# app = App()
# app.mainloop()        


# -----------------------------------------------------------------------------------------------

import customtkinter as ctk

class FrameCheckboxes(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.checkbox_1 = ctk.CTkCheckBox(self, text="CheckBox 1")
        self.checkbox_1.value = 1
        self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0))
        
        self.checkbox_2 = ctk.CTkCheckBox(self, text="CheckBox 2")
        self.checkbox_2.value = 2
        self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0))
        
        self.checkbox_3 = ctk.CTkCheckBox(self, text="CheckBox 3")
        self.checkbox_3.value = 3
        self.checkbox_3.grid(row=2, column=0, padx=10, pady=10)
        
        
    def get(self):
        checkboxes_marcadas = []
        
        if self.checkbox_1.get() == 1:
            checkboxes_marcadas.append(self.checkbox_1.value) #ou poderia usar checkbox_1.cget("text") para pegar o texto do cb
        if self.checkbox_2.get() == 1:
            checkboxes_marcadas.append(self.checkbox_2.value)
        if self.checkbox_3.get() == 1:
            checkboxes_marcadas.append(self.checkbox_3.value)
        
        return checkboxes_marcadas
    

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("My App")
        self.geometry("500x300")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)
        
        self.frame_checkbox = FrameCheckboxes(self)
        self.frame_checkbox.grid(row=0, column=0, padx=10, pady=(10, 10), sticky="s")
        
        self.botao_print = ctk.CTkButton(self, text="Enviar", command=self.botao_print)
        self.botao_print.grid(row=1, column=0, padx=10, pady=10, sticky="n")
    
    
    def botao_print(self) -> None:
        print(f"Checboxes Marcadas: {self.frame_checkbox.get()}")
    

app = App()
app.mainloop()


# -----------------------------------------------------------------------------------------------

