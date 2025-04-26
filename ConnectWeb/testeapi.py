import requests

# Exemplo de API pública
url = "https://jsonplaceholder.typicode.com/posts"

# Fazendo a requisição
response = requests.get(url)

# Convertendo a resposta em JSON
dados = response.json()

# Usando os dados
for item in dados[:5]:  # Pegando só os 5 primeiros itens
    print(f'Título: {item["title"]}')