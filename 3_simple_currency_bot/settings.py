my_token = "1818081328:AAFAPDBGdpbhEN5qEgeI6uzaTZFxmaRxyGs"
root_url = "https://api.telegram.org/bot" 
get_me_endpoint = "/getMe"
updates_endpoint = "/getUpdates"
message_endpoint = "/sendMessage"

ok_codes = (200,201,202,203,204,205)
available_currency_countries = ("uk","rb")
currency_necessary_keys = {"uk": ('txt', 'rate', 'cc', 'exchangedate'),
						   "rb": ('Date', 'Cur_Abbreviation', 'Cur_Scale', 'Cur_Name', 'Cur_OfficialRate')}

bank_root_urls = {"rb_root_url": "https://www.nbrb.by/api/exrates/rates/",
 				  "uk_root_url": "https://bank.gov.ua/NBUStatService/v1/statdirectory/"}
message_unknown_country = """Введите, пожалуйста, код страны,курс валют которой вас интересует.Пока доступны Беларусь (br) и Украина (uk).\n
							 Для этого отправьте сообщение /country uk или /country rb """

user_country = ""
hello_message = """Привет! Пока доступен следующий функцонал:\n
				   /start - начало работы \n
				   /country - задать боту свою страну для получения курса валют, доступны uk и rb \n
				   /курс - узнать урс валюты на сегодня, для выбранной страны, через аббревиатуру. Например /курс USD """