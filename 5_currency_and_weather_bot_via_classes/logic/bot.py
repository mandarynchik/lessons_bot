import requests
from . settings import telegram_bot_token, ok_codes, hello_message, message_unknown_country,available_currency_countries
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
		res = requests.get(updates_url)
		if res.status_code in ok_codes:
			result = res.json()
			return result
		else:
			print(f"Неудача с запросом: статус {res.status_code}")

	def send_message(self, chat_id:str, text_message:str)->bool:
		send_message_url = f"{self.root_url}{self.token}{self.message_endpoint}"
		res = requests.post(send_message_url, data={"chat_id":chat_id, "text":text_message})
		if res.status_code in ok_codes:
			return True
		else:
			print(f"Не удалось послать сообщение - ошибка с кодом {res.status_code}")
	
	def process_message(self, chat_id:str, message_text:str)->None:
		if "/start" in message_text:
			self.send_message(chat_id, hello_message)
		if "/курс" in message_text:
			if len(message_text) == 9:
				currency_abbr = message_text[-3:]
				if self.user_country:
					raw_result = today_currency_by_abbr(self.user_country, currency_abbr)
					result = currency_message_to_user(raw_result, self.user_country)
					self.send_message(chat_id, result)
				else:
					self.send_message(chat_id, message_unknown_country)
			else:
				print("Убедитесь, что собщение составленно в верном формате: например '/курс USD' ")
	
		if "/country" in message_text:
			if message_text[-2:] in available_currency_countries:
				self.user_country = message_text[-2:]

		if "/weather" in message_text:
			city = message_text[9::]
			weather_message = create_weather_message(city)
			if weather_message:
				self.send_message(chat_id, weather_message)

	def pooling(self):
		last_message_number = 0
		while True:
			updates = self.get_updates()
			message_id = updates["result"][-1]["message"]["message_id"]
			chat_id = updates["result"][-1]["message"]["chat"]["id"] 
			last_message_text = updates["result"][-1]["message"]["text"]

			if message_id > last_message_number:
				self.process_message(chat_id, last_message_text)
				last_message_number = message_id