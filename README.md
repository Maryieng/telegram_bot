## Telegram Bot с FastAPI, Redis, MongoDB и Nginx

Этот проект представляет собой пример Telegram бота, построенного с использованием FastAPI, Redis, MongoDB и Nginx.

Функционал:

• Сохранение сообщений: Бот может сохранять сообщения, отправленные пользователем, в базу данных MongoDB.
• Хранение данных: Используется Redis для кэширования данных.
• Развертывание с Nginx: Приложение развернуто с использованием Nginx для обратной проксировки, что обеспечивает дополнительную безопасность и возможность работы с HTTPS. 

Технологии:

• FastAPI: Веб-фреймворк для Python, обеспечивающий высокую производительность и простоту использования.
• Python-Telegram-Bot: Библиотека для работы с Telegram API.
• MongoDB: База данных NoSQL для хранения сообщений.
• Redis: Кэш данных для повышения производительности.
• Nginx: Веб-сервер для проксирования запросов к приложению FastAPI, а также для работы с SSL (HTTPS).

Установка:

1. Создайте виртуальное окружение:
python3 -m venv .venv
source .venv/bin/activate

3. Установите зависимости:
pip install -r requirements.txt


Запуск:

1. Запустите MongoDB:
   mongod
   
2. **Запустите Redis:**
   redis-server


Развертывание:

• Docker: В проекте есть файл docker-compose.yml для развертывания бота с использованием Docker. 
Развертывание с Nginx:

1. Установите Docker
2. Установите Docker Compose
3. Установите Nginx
4. Установите Certbot
5. Запустите Docker Compose
6. Получение SSL-сертификата
7. Конфигурация Nginx для HTTPS: 
  * Измените файл nginx.conf, добавьте секцию ssl и укажите пути к сертификатам.
  * Перенаправьте HTTP-трафик на HTTPS.
8. Перезапустите Nginx


Использование:

• Добавить бота в чат: Найдите бота в Telegram и добавьте его в нужный чат.
• Отправить сообщение: Напишите любое сообщение в чат с ботом. Бот сохранит сообщение в MongoDB.

Дополнительная информация:

• Документация FastAPI: https://fastapi.tiangolo.com/
• Документация Python-Telegram-Bot: https://python-telegram-bot.readthedocs.io/en/stable/
• Документация MongoDB: https://www.mongodb.com/docs
• Документация Redis: https://redis.io/docs
• Документация Nginx: https://nginx.org/en/docs/
• Документация Certbot: https://certbot.eff.org/
