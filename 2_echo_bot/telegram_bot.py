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


def echo_message(token):
	updates = get_updates(token)
	chat_id = updates["result"][-1]["message"]["chat"]["id"]  
	last_message_text = updates["result"][-1]["message"]["text"]
	send_message(chat_id, last_message_text, token)


last_message_number = 0
while True:
    updates = get_updates(my_token)
    message_id = updates["result"][-1]["message"]["message_id"]

    if message_id > last_message_number:
        echo_message(my_token)
        last_message_number = message_id
        