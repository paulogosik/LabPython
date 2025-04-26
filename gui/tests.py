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

import customtkinter as ctk

# o 'app' é quando você cria uma janela, e pode usar ele mesmo para controlar a janela
app = ctk.CTk()
app.geometry("1000x600")


app.mainloop()