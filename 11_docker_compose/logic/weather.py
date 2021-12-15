import requests
import datetime

from . settings import weather_root_url, weather_token, ok_codes, logger

def get_current_weather(city:str)->dict:
	url = f"{weather_root_url}?q={city}&appid={weather_token}&units=metric"
	try:
		res = requests.get(url)
		if res.status_code in ok_codes:
			weather_in_city = res.json()
			return weather_in_city
		else:
			logger.error(f"Неудача с запросом: статус {res.status_code}")
	except Exception as e:
		error_message = f"Some troubles with request to {updates_url}: {e}"
		logger.error(error_message)
		raise Exception(error_message)
	
def create_weather_message(city:str)->str:
	raw_weather = get_current_weather(city)
	if type(raw_weather) == dict:

		median_temp = raw_weather["main"]["temp"]
		weather_description = raw_weather["weather"][0]["description"]

		sunrise_unix_time = raw_weather["sys"]["sunrise"]
		sunrise_timestamp = datetime.datetime.fromtimestamp(sunrise_unix_time)
		sunrise_human_datetime = sunrise_timestamp.strftime('%H:%M:%S')

		sunset_unix_time = raw_weather["sys"]["sunset"]
		sunset_timestamp = datetime.datetime.fromtimestamp(sunset_unix_time)
		sunset_human_datetime = sunset_timestamp.strftime('%H:%M:%S')

		weather_message = f"В {city} сейчас {weather_description}, средняя температура {median_temp}.\n Рассвет: {sunrise_human_datetime}, закат: {sunset_human_datetime}"
		return weather_message
	else:
		return False