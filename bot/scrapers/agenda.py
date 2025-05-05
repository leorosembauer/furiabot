# bot/scrapers/agenda.py

import requests
from bs4 import BeautifulSoup

def get_furia_matches():
    url = "URL_DA_AGENDA_DA_FURIA"  # Substitua com a URL real
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extraia os dados da agenda conforme a estrutura da página
        matches = soup.find_all('div', class_="match_class")  # Exemplo de como pode ser
        return "\n".join([match.text for match in matches])  # Ajuste conforme o formato
    else:
        return "Não conseguimos obter os dados da agenda da FURIA agora."
