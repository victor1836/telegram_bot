import telebot

bot = telebot.TeleBot("1919563245:AAEBEBAxcI6f5z2GO4k1loaKseUka1tlmGE")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()