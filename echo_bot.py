# -*- coding: utf-8 -*-
import telebot
import requests

bot = telebot.TeleBot("1919563245:AAEBEBAxcI6f5z2GO4k1loaKseUka1tlmGE")
url = "https://fish-text.ru/get?format=html&number=1"

@bot.message_handler(commands=['start'])
def handle_start(message): 
 bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def handle_help(message): 
 bot.reply_to(message, 'Сообщение справки по использованию бота для, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "Аленка": 
       bot.send_message(message.from_user.id, "Поверь мир прекрасен!")
    else:
       bot.reply_to(message, 'А здесь бот выдает умные мысли')
       response = requests.request("POST", url)
       bot.reply_to(message, response.text)

bot.polling(none_stop=True, interval=0)
