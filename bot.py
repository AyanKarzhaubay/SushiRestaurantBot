import telebot
from telebot import types

TOKEN = '5424950727:AAGwWkQ28qm10cGC5p8Efb8JkHljNc7XDtk'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я бот суши-ресторана. Как я могу помочь?")

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = (
        "Доступные команды:\n"
        "/start - Начать общение с ботом\n"
        "/menu - Показать меню\n"
        "/help - Показать это сообщение помощи\n\n"
        "Вы также можете выбрать одну из категорий в меню, чтобы увидеть соответствующие изображения."
    )
    bot.send_message(message.chat.id, help_text)

@bot.message_handler(commands=['menu'])
def show_menu(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Сеты')
    btn2 = types.KeyboardButton('Суши и роллы')
    btn3 = types.KeyboardButton('Пицца')
    btn4 = types.KeyboardButton('Крылышки, снэки, напитки')
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, "Выберите категорию:", reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Сеты':
        with open('images/set1.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('images/set2.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    if message.text == 'Суши и роллы':
        with open('images/rolls1.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('images/rolls2.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'Пицца':
        with open('images/pizza1.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
        with open('images/pizza2.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    elif message.text == 'Крылышки, снэки, напитки':
        with open('images/fastfood.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo)
    else:
        bot.reply_to(message, "Извините, я вас не понял. Выберите категорию из меню.")


bot.polling(none_stop=True)