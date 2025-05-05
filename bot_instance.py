import telebot
from telebot import types
import time

TOKEN = '7842705162:AAF3WDBvVx5sXgVRh98c8cSsa8HnAU2YrJA'  # Substitua pelo token real
bot = telebot.TeleBot(TOKEN)

user_data = {}

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_data[chat_id] = {'step': 'ask_name'}
    bot.send_message(chat_id, "Olá! Qual é o seu nome?")

@bot.message_handler(commands=['reset'])
def reset(message):
    chat_id = message.chat.id
    user_data.pop(chat_id, None)
    user_data[chat_id] = {'step': 'ask_name'}
    bot.send_message(chat_id, "🔄 Bot resetado! Qual é o seu nome?")

@bot.message_handler(commands=['ranking'])
def ranking(message):
    texto = "📊 Ranking atual da FURIA na HLTV:\n\n9. FURIA 🐍"
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['alerta'])
def alerta(message):
    bot.send_message(message.chat.id, "🔔 Alerta configurado! Você será avisado antes do próximo jogo da FURIA.")

@bot.message_handler(commands=['curiosidades'])
def curiosidades(message):
    fatos = [
        "🐍 A FURIA foi fundada em 2017.",
        "🌎 A sede fica no Brasil e nos EUA.",
        "🧠 O estilo de jogo é conhecido por ser agressivo.",
        "🎯 Já venceram times top 5 em Majors.",
        "🧢 O CEO também é ex-jogador profissional.",
        "🔥 Já chegaram ao top 3 do ranking HLTV.",
        "🕹️ A FURIA tem times em outros jogos como Valorant.",
        "💼 Eles têm uma casa gaming nos EUA.",
        "🎙️ Jogadores da FURIA são presença constante em podcasts de CS.",
        "⚡ O lema da FURIA é 'Somos FURIA'."
    ]
    resposta = "\n\n".join(f"🔹 {f}" for f in fatos)
    bot.send_message(message.chat.id, f"🤔 Curiosidades sobre a FURIA:\n\n{resposta}")

@bot.message_handler(commands=['elenco'])
def elenco(message):
    jogadores = [
        "🧠 KSCERATO",
        "🎯 yuurih",
        "💥 arT",
        "🧱 drop",
        "🔫 chelo",
        "🎧 guerri (coach)"
    ]
    texto = "🎮 Elenco atual da FURIA:\n\n" + "\n".join(jogadores)
    bot.send_message(message.chat.id, texto)

@bot.message_handler(commands=['ajuda', 'help'])
def ajuda(message):
    comandos = [
        "/start - Iniciar conversa",
        "/reset - Reiniciar cadastro",
        "/ranking - Ver ranking HLTV",
        "/alerta - Ativar lembrete de jogo",
        "/curiosidades - Fatos sobre a FURIA",
        "/elenco - Ver elenco do time",
        "/ajuda - Ver todos os comandos"
    ]
    bot.send_message(message.chat.id, "📋 Comandos disponíveis:\n\n" + "\n".join(comandos))

@bot.message_handler(func=lambda m: True)
def handle_messages(message):
    chat_id = message.chat.id
    texto = message.text.strip()

    if chat_id in user_data:
        step = user_data[chat_id].get('step')

        if step == 'ask_name':
            user_data[chat_id]['name'] = texto
            user_data[chat_id]['step'] = 'ask_gender'

            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            markup.add('Masculino', 'Feminino', 'Outro')
            bot.send_message(chat_id, f"Prazer, {texto}! Agora me diga seu gênero:", reply_markup=markup)

        elif step == 'ask_gender':
            user_data[chat_id]['gender'] = texto
            user_data[chat_id]['step'] = 'done'
            nome = user_data[chat_id].get('name', 'Usuário')
            bot.send_message(chat_id, f"✅ Tudo certo, {nome}! Gênero registrado como: {texto}.")
            bot.send_message(chat_id, "ℹ️ Use o comando /ajuda para ver a lista de comandos disponíveis.")

        else:
            bot.send_message(chat_id, "Comando não reconhecido. Use /ajuda para ver as opções.")
    else:
        bot.send_message(chat_id, "Use /start para começar ou /reset para reiniciar.")

if __name__ == '__main__':
    print("🔧 Iniciando bot...")
    time.sleep(1)
    print("✅ Bot da FURIA está ONLINE e aguardando comandos no Telegram.")
    print("📱 Use /start para testar.")
    bot.infinity_polling()
