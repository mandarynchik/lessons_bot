import requests

from . settings import telegram_bot_token, ok_codes, hello_message, message_unknown_country,available_currency_countries, something_went_message, logger
from . import settings
from . weather import create_weather_message
from . currencies import today_currency_by_abbr, currency_message_to_user

class TelegramBot:
	def __init__(self, token="", country=""):
		self.token = token
		self.user_country = country
		self.root_url = "https://api.telegram.org/bot"
		self.updates_endpoint = "/getUpdates"
		self.message_endpoint = "/sendMessage" 
		pass

	def get_updates(self)->dict:
		updates_url = f"{self.root_url}{self.token}{self.updates_endpoint}"
		try:
			res = requests.get(updates_url)
			if res.status_code in ok_codes:
				result = res.json()
				return result
			else:
				logger.error(f"Неудача с запросом: статус {res.status_code}")
		except Exception as e:
			error_message = f"Some troubles with request to {updates_url}: {e}"
			logger.error(error_message)
			raise Exception(error_message)


	def send_message(self, chat_id:str, text_message:str)->bool:
		send_message_url = f"{self.root_url}{self.token}{self.message_endpoint}"
		try:
			res = requests.post(send_message_url, data={"chat_id":chat_id, "text":text_message})
			if res.status_code in ok_codes:
				return True
			else:
				logger.error(f"Неудача с запросом: статус {res.status_code}")
		except Exception as e:
			error_message = f"Some troubles with request to {updates_url}: {e}"
			logger.error(error_message)
			raise Exception(error_message)


	def process_message(self, chat_id:str, message_text:str)->None:
		if "/start" in message_text:
			self.send_message(chat_id, hello_message)
		if "/курс" in message_text:
			if len(message_text) == 9:
				currency_abbr = message_text[-3:]
				if self.user_country:
					raw_result = today_currency_by_abbr(self.user_country, currency_abbr)
					if raw_result:
						result = currency_message_to_user(raw_result, self.user_country)
						if result:
							self.send_message(chat_id, result)
						else:
							self.send_message(chat_id, something_went_message)
				else:
					self.send_message(chat_id, message_unknown_country)
			else:
				self.send_message(chat_id, something_went_message)
					
		if "/country" in message_text:
			if message_text[-2:] in available_currency_countries:
				self.user_country = message_text[-2:]

		if "/weather" in message_text:
			city = message_text[9::]
			if city:
				weather_message = create_weather_message(city)
				if weather_message:
					self.send_message(chat_id, weather_message)
				else:
					self.send_message(chat_id, something_went_message)
			else:
				self.send_message(chat_id, something_went_message)


	def pooling(self):
		last_message_number = 0
		while True:
			updates = self.get_updates()
			if updates["result"]:
				message_id = updates["result"][-1]["message"]["message_id"]
				chat_id = updates["result"][-1]["message"]["chat"]["id"] 
				last_message_text = updates["result"][-1]["message"]["text"]

				if message_id > last_message_number:
					self.process_message(chat_id, last_message_text)
					last_message_number = message_id