import requests
import os

# Coloque sua chave da API da PandaScore aqui
API_TOKEN = os.getenv("PANDASCORE_TOKEN")
TEAM_NAME = "FURIA"
BASE_URL = "https://api.pandascore.co/csgo/matches/upcoming"

def get_upcoming_matches():
    headers = {"Authorization": f"Bearer {API_TOKEN}"}
    params = {"per_page": 5}  # Limita para os próximos 5 jogos

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        response.raise_for_status()
        matches = response.json()

        furia_matches = [m for m in matches if TEAM_NAME.lower() in (
            m['opponents'][0]['opponent']['name'].lower() if m['opponents'] else ""
            or m['opponents'][1]['opponent']['name'].lower() if len(m['opponents']) > 1 else ""
        )]

        if not furia_matches:
            return ["Nenhum jogo da FURIA encontrado nos próximos dias."]

        output = []
        for match in furia_matches:
            time = match['begin_at'] or "Horário não disponível"
            opponent = match['opponents'][1]['opponent']['name'] if len(match['opponents']) > 1 else "Desconhecido"
            output.append(f"🗓️ {time} vs {opponent}")

        return output
    except Exception as e:
        return [f"Erro ao buscar jogos: {e}"]
