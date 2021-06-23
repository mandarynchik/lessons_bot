import requests

my_token = "1818081328:AAFAPDBGdpbhEN5qEgeI6uzaTZFxmaRxyGs"
root_url = "https://api.telegram.org/bot" 
get_me = "/getMe"
updates_endpoint = "/getUpdates"
message_endpoint = "/sendMessage"

OK_CODES = (200,201,202,203,204,205)

def get_updates(token):
	updates_url = f"{root_url}{token}{updates_endpoint}"

	res = requests.get(updates_url)
	if res.status_code in OK_CODES:
		result = res.json()
		return result
	else:
		print(f"Неудача с запросом: статус {res.status_code}")


def send_message(chat_id, text_message, token):
	send_message_url = f"{root_url}{token}{message_endpoint}"
	res = requests.post(send_message_url, data={"chat_id":chat_id, "text":text_message})
	if res.status_code in OK_CODES:
		return True
	else:
		print(f"Не удалось послать сообщение - ошибка с кодом {res.status_code}")



updates = get_updates(my_token)
chat_id = updates["result"][-1]["message"]["chat"]["id"]  
message = "Hello!"
send_message(chat_id, message, my_token)