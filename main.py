import telebot
from telebot import types



bot = telebot.TeleBot('6102660581:AAFhoZ_EwY9uLOb3dVd4HlP3-2FvJ1JjFm0')

@bot.message_handler(commands= ['start'])
def url(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Поздороваться')
    markup.add(btn1)
    bot.send_message(message.from_user.id, 'Привет, винегрет, сто килограмм котлет, жопа пирожки!!!!', replay_markup = markup)
@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == 'Поздороваться':
        bot.send_message((message.from_user.id, 'Сам жопа вонючка'))


bot.polling(none_stop=True, interval=0)
