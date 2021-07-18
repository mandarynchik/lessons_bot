import requests
import settings
from settings import my_token, root_url, updates_endpoint, message_endpoint, ok_codes, hello_message, message_unknown_country,available_currency_countries
from currencies import today_currency_by_abbr, currency_message_to_user

def get_updates(token):
	updates_url = f"{root_url}{token}{updates_endpoint}"
	res = requests.get(updates_url)
	if res.status_code in ok_codes:
		result = res.json()
		return result
	else:
		print(f"Неудача с запросом: статус {res.status_code}")


def send_message(chat_id, text_message, token):
	send_message_url = f"{root_url}{token}{message_endpoint}"
	res = requests.post(send_message_url, data={"chat_id":chat_id, "text":text_message})
	if res.status_code in ok_codes:
		return True
	else:
		print(f"Не удалось послать сообщение - ошибка с кодом {res.status_code}")

def pooling(token):
	last_message_number = 0
	while True:
		updates = get_updates(token)
		if updates["result"]:
			"""
			Telegram чистит записи  сообщения примерно раз в сутки,
			поэтому можем получить ситуацию когда ответ будет
			{"ok":true,"result":[]}
			тогда updates["result"][-1]  вызовет падение. 
			"""
			message_id = updates["result"][-1]["message"]["message_id"]
			chat_id = updates["result"][-1]["message"]["chat"]["id"] 
			last_message_text = updates["result"][-1]["message"]["text"]

			if message_id > last_message_number:
				process_message(chat_id, last_message_text, token)
				last_message_number = message_id


def process_message(chat_id, message_text, token):
	if "/start" in message_text:
		send_message(chat_id, hello_message, token)
	if "/курс" in message_text:
		if len(message_text) == 9:
			currency_abbr = message_text[-3:]
			if settings.user_country:
				raw_result = today_currency_by_abbr(settings.user_country, currency_abbr)
				result = currency_message_to_user(raw_result, settings.user_country)
				send_message(chat_id, result, token)
			else:
				send_message(chat_id, message_unknown_country, token)
		else:
			print("Убедитесь, что собщение составленно в верном формате: например '/курс USD' ")
	
	if "/country" in message_text:
		if message_text[-2:] in available_currency_countries:
			settings.user_country = message_text[-2:]

pooling(my_token)