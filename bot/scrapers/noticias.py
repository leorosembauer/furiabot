from telebot import TeleBot
from telebot.types import Message
from bot.scrapers.noticias import get_latest_news

def register_handlers(bot: TeleBot):
    @bot.message_handler(commands=["start"])
    def start(message: Message):
        bot.send_message(message.chat.id, "Olá! Bem-vindo ao bot da FURIA CS! Qual seu nome?")

    @bot.message_handler(commands=["elenco"])
    def elenco(message: Message):
        jogadores = [
            "🧑‍💻 KSCERATO",
            "🧑‍💻 yuurih",
            "🧑‍💻 arT",
            "🧑‍💻 chelo",
            "🧑‍💻 FalleN",
        ]
        bot.send_message(message.chat.id, "Elenco atual da FURIA:\n" + "\n".join(jogadores))

    @bot.message_handler(commands=["redes"])
    def redes(message: Message):
        links = [
            "🐦 Twitter: https://twitter.com/furiagg",
            "📷 Instagram: https://instagram.com/furiagg",
            "▶️ YouTube: https://youtube.com/furia",
            "🟣 Twitch: https://twitch.tv/furiagg",
        ]
        bot.send_message(message.chat.id, "Siga a FURIA nas redes sociais:\n" + "\n".join(links))

    @bot.message_handler(commands=["noticias"])
    def send_latest_news(message: Message):
        noticias = get_latest_news()
        bot.send_message(message.chat.id, "\n\n".join(noticias))

    @bot.message_handler(func=lambda msg: True)
    def fallback(message: Message):
        bot.send_message(message.chat.id, "Comando não reconhecido. Use /start, /elenco, /redes ou /noticias.")
