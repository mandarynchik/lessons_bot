import requests

# step1 collection of inspirational quotes


inspirational_quotes = ["Be yourself; everyone else is already taken.― Oscar Wilde",
                        "You've gotta dance like there's nobody watching, Love like you'll never be hurt,Sing like there's nobody listening,And live like it's heaven on earth.― William W. Purkey",
                        "Be the change that you wish to see in the world. ― Mahatma Gandhi"
                        "Without music, life would be a mistake.― Friedrich Nietzsche, Twilight of the Idols"
                        "I have not failed. I've just found 10,000 ways that won't work.― Thomas A. Edison"
                        ]
# step2 send message

token = "5013724612:AAEoqRNEn4Ue3RGiyTqAJn7ZKXlPQE-IjiM"
root_url = "https://api.telegram.org/bot"
message_endpoint = "/sendMessage"
chat_id = "468282070"
text_message = inspirational_quotes[0]


def send_message(chat_id, text_message, token):
    send_message_url = f"{root_url}{token}{message_endpoint}"
    res = requests.post(send_message_url, data={"chat_id": chat_id, "text": text_message})


send_message(chat_id, text_message, token)
