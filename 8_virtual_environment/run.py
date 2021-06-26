from logic.bot import TelegramBot
from logic.settings import telegram_bot_token

if __name__ == '__main__':
	bot = TelegramBot(token=telegram_bot_token, country="")
	bot.pooling()