from transliterate import to_latin, to_cyrillic

import telebot
TOKEN = '6365333074:AAHPyAKoWAuCW4zx4IWCS3HHmAnwa2WxGsM'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum asosiy oynaga xush kelibsiz")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)


bot.infinity_polling()





# word = input("So'z kiriting: ")
# if word.isascii():
#     new_word = to_cyrillic(word)
# else:
#     new_word = to_latin(word)
# print (new_word)