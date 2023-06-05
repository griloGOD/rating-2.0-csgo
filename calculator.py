import requests
from bs4 import BeautifulSoup
import re

# Faz uma solicitação HTTP ao site
url = "https://gamersclub.com.br/lobby/partida/19483035"
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Extrai o conteúdo HTML da resposta
    html_content = response.text

    # Utiliza o BeautifulSoup para analisar o conteúdo HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Encontra todos os elementos de texto no conteúdo HTML
    text_elements = soup.find_all(text=True)

    # Percorre os elementos de texto e encontra os números usando uma expressão regular
    numbers = []
    for element in text_elements:
        # Utiliza uma expressão regular para encontrar números
        matches = re.findall(r"\d+", element)
        numbers.extend(matches)

    # Exibe os números encontrados
    print(numbers)
else:
    print("Erro ao fazer a solicitação HTTP:", response.status_code)
