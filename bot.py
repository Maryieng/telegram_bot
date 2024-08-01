import logging
import telebot
import pymongo

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
BOT_TOKEN = "6415992798:AAFqG3jayhSejPGUnYrazNt22dk4ekWnkwY"
MONGO_URI = "mongodb://localhost:27017/bot"

client = pymongo.MongoClient(MONGO_URI)
db = client.get_database("my_bot")
messages_collection = db.get_collection("messages")

bot = telebot.TeleBot(BOT_TOKEN)

waiting_for_message = False

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message,
        "Добро пожаловать! \nЧтобы посмотреть список сообщений, отправьте '/messages'\n Чтобы"
        " отправить новое сообщение, отправьте '/send'."
    )

@bot.message_handler(commands=['messages'])
def get_messages(message):
    messages = messages_collection.find({})
    message_list = "Список сообщений:\n"
    for message_item in messages:
        message_list += f"- {message_item.get('author', 'Неизвестный автор')}: {message_item['text']}\n"
    bot.reply_to(message, message_list)

@bot.message_handler(commands=['send'])
def send_message(message):
    global waiting_for_message
    waiting_for_message = True
    bot.reply_to(message, "Введите ваше сообщение:")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    global waiting_for_message
    if waiting_for_message:
        messages_collection.insert_one(
            {"text": message.text, "author": message.from_user.username}
        )
        bot.reply_to(message, "Сообщение успешно отправлено!")
        waiting_for_message = False
    else:
        bot.reply_to(message,
            "Неверная команда. Используйте '/messages' для просмотра списка сообщений или"
            " '/send' для отправки нового сообщения."
        )

bot.polling()
