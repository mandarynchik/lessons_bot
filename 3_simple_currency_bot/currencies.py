import requests
from settings import ok_codes, bank_root_urls, currency_necessary_keys

def get_today_currencies(country_abbr, currency_abbr):
	root_url = bank_root_urls[f"{country_abbr}_root_url"]
	
	if country_abbr == "rb":
		url = f"{root_url}?periodicity=0"
	if country_abbr == "uk":
		url = f"{root_url}exchange?json"

	res = requests.get(url)
	res_code = res.status_code
	if res_code in ok_codes:
		raw_currencies = today_currencies = res.json()
		return raw_currencies
	else:
		print(f"Запрос не был выполнен со статусом {res_code}")



def today_currency_by_abbr(country_abbr, currency_abbr):
    today_currencies = get_today_currencies(country_abbr, currency_abbr)
    for curr in today_currencies:
        if country_abbr == "rb":
            if curr["Cur_Abbreviation"] == currency_abbr.upper():
                return curr
        if country_abbr == "uk":
            if curr["cc"] == currency_abbr.upper():
                return curr
                pass

def currency_message_to_user(today_currency_info, country_abbr):
	if type(today_currency_info) == dict:
		for key in currency_necessary_keys[country_abbr]:
			if key not in today_currency_info.keys():
				print(key)
				return False

		if country_abbr == "rb":
			money_abbr = today_currency_info['Cur_Abbreviation']
			country_money = "бел.руб"
			rate = today_currency_info["Cur_OfficialRate"]
			scale = today_currency_info["Cur_Scale"]

		if country_abbr == "uk":
			money_abbr = today_currency_info['cc']
			country_money = "грвн."
			rate = today_currency_info["rate"]
			scale = 1

		message = f"Cегодня {scale} {money_abbr} стоит {rate} {country_money}"
		return message
		pass
"""
result = today_currency_by_abbr("rb", "usd")
print(result)
res =currency_message_to_user(result, "rb")
print(res)
"""