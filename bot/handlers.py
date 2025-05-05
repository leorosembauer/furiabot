from telebot.types import Message
from .bot_config import bot

# Variáveis para armazenar dados temporários do usuário
user_data = {}

# Função de reiniciar a interação
@bot.message_handler(commands=['reset'])
def reset(message: Message):
    user_data[message.chat.id] = {}  # Limpa os dados do usuário
    bot.send_message(message.chat.id, "🔄 O bot foi resetado. Vamos começar de novo!")
    bot.send_message(message.chat.id, "👋 Qual seu nome?")
    
# Comando /start
@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.send_message(message.chat.id, "👊 Salve! Eu sou o bot da FURIA CS. Use /ajuda para ver o que posso fazer!")

# Comando /ajuda
@bot.message_handler(commands=['ajuda'])
def ajuda(message: Message):
    ajuda_texto = (
        "🔥 Comandos disponíveis:\n"
        "/elenco – Ver o elenco atual\n"
        "/curiosidades – Curiosidades da FURIA CS\n"
        "/agenda – Próximos jogos\n"
        "/ranking – Ranking HLTV\n"
        "/clipes – Vídeos recentes\n"
        "/noticias – Últimas notícias\n"
        "/alerta – Receber lembrete de jogo\n"
        "/reset – Reiniciar o bot"
    )
    bot.send_message(message.chat.id, ajuda_texto)

# Função para armazenar o nome do usuário
@bot.message_handler(func=lambda message: message.chat.id in user_data and 'name' not in user_data[message.chat.id])
def ask_name(message: Message):
    user_data[message.chat.id]['name'] = message.text
    bot.send_message(message.chat.id, f"👍 Olá, {message.text}! Agora, me diga: qual seu gênero? (masculino/feminino)")
    
# Função para armazenar o gênero do usuário
@bot.message_handler(func=lambda message: message.chat.id in user_data and 'gender' not in user_data[message.chat.id])
def ask_gender(message: Message):
    if message.text.lower() not in ['masculino', 'feminino']:
        bot.send_message(message.chat.id, "⚠️ Gênero inválido. Por favor, responda com 'masculino' ou 'feminino'.")
        return
    user_data[message.chat.id]['gender'] = message.text.lower()
    bot.send_message(message.chat.id, "👏 Muito bem! Agora você pode usar os comandos /ajuda, /elenco, /agenda e outros.")

# Comando /elenco
@bot.message_handler(commands=['elenco'])
def elenco(message: Message):
    elenco = [
        "🇧🇷 KSCERATO 🦁",
        "🇧🇷 yuurih 🧠",
        "🇧🇷 arT 🎯",
        "🇧🇷 chelo 🔥",
        "🇧🇷 FalleN 🧙"
    ]
    bot.send_message(message.chat.id, "🎮 Elenco atual da FURIA:\n" + "\n".join(elenco))

# Comando /curiosidades
@bot.message_handler(commands=['curiosidades'])
def curiosidades(message: Message):
    lista = [
        "1️⃣ A FURIA foi fundada em 2017.",
        "2️⃣ O KSCERATO é um dos jogadores mais consistentes do Brasil.",
        "3️⃣ arT é conhecido por seu estilo agressivo e imprevisível.",
        "4️⃣ A FURIA foi semifinalista na IEM Rio Major 2022.",
        "5️⃣ FalleN, 'O Professor', entrou em 2023 para liderar o time.",
        "6️⃣ A base de fãs da FURIA é uma das mais apaixonadas do CS.",
        "7️⃣ yuurih é multicampeão nacional com a organização.",
        "8️⃣ A logo da FURIA representa uma pantera.",
        "9️⃣ A FURIA investe forte em análise de dados nos jogos.",
        "🔟 O chelo é conhecido pelo clutch nervoso e mira firme."
    ]
    bot.send_message(message.chat.id, "📌 Curiosidades sobre a FURIA CS:\n\n" + "\n".join(lista))

# Comando /agenda
@bot.message_handler(commands=['agenda'])
def agenda(message: Message):
    jogos = [
        "🗓️ 06/05 - FURIA vs G2 - 18h",
        "🗓️ 08/05 - FURIA vs Vitality - 16h",
        "🗓️ 10/05 - FURIA vs NAVI - 20h"
    ]
    bot.send_message(message.chat.id, "📅 Próximos jogos da FURIA:\n\n" + "\n".join(jogos))
