# Чтение из окружения
import os 

# print(os.environ)
env_values = os.environ
# print(type(env_values))
# print(env_values.get("ZSH"))


## Загрузка значений в окружение
import dotenv #одна из библиотек для загрузки данных в окружение
dotenv.load_dotenv(".env")
print(env_values.get("WEATHER_TOKEN"))

# pipenv автоматически прогружает .env-файл
