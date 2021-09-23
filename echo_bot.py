# -*- coding: utf-8 -*-
import config
import telebot
from telebot import types
import requests

bot = telebot.TeleBot(config.token)
url = "https://fish-text.ru/get?format=html&number=1"

markup = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
itembtn1 = types.KeyboardButton('Фраза для отчета')
itembtn2 = types.KeyboardButton('Аленка')
markup.add(itembtn1, itembtn2)

@bot.message_handler(commands=['start'])
def handle_start(message): 
 bot.reply_to(message, 'Hello, ' + message.from_user.first_name)

@bot.message_handler(commands=['help'])
def handle_help(message): 
 bot.reply_to(message, 'Сообщение справки по использованию бота для, ' + message.from_user.first_name,reply_markup=markup)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    if message.text == "Аленка": 
       response = requests.get('http://free-generator.ru/generator.php?action=compliment&pol=1&type=2')
       data = response.json()
       compliment = data["compliment"]
       bot.send_message(message.from_user.id, compliment["compliment"])
    else:
       #       bot.reply_to(message, 'А здесь бот выдает умные мысли')  
       response = requests.request("POST", url)
       bot.send_message(message.from_user.id, response.text)

bot.polling(none_stop=True, interval=0)
