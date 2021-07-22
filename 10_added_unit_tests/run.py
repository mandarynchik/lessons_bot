from logic.bot import TelegramBot
from logic.settings import telegram_bot_token

from logic.currencies import today_currency_by_abbr
print(today_currency_by_abbr("rb", "USD"))
print(today_currency_by_abbr("uk", "USD"))


if __name__ == '__main__':
	bot = TelegramBot(token=telegram_bot_token, country="")
	bot.pooling()