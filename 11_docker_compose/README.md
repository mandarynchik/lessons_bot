## Добавлено простое тестирование.

Добавлены примеры юнит-тестов с использованием unittest.

### Запуск тестов

python -m unittest tests/test_formatting_user_message.py

### Запуск

Подготока бота к запуску в контейнеру.
Перенос списка зависимостей из Pipenv в requirements.txt

```bash
pipenv run pip freeze > requirements.txt
```

Запуск бота в контейнере
```bash
sudo docker build -t bot_image:bot_image . && sudo docker run bot_image:bot_image
```