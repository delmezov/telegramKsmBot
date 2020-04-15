import telebot
import config
import time
from telebot import types

bot = telebot.TeleBot(config.token)

group_id = '492199201'
group_id_int = -1 * int(group_id)


@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id, "<b>Добро пожаловать {0.first_name}!</b>\nВас приветствует {1.first_name}.\n --------------------------------------------------------------------------------------\nЯ помогу выставить ваше объявление просто следйуте инструкциям: ".format(message.from_user, bot.get_me()), parse_mode = "HTML")
     
@bot.message_handler(content_types=['new_chat_members'])
def add_user_message(message):
    if message.chat.type != "private" and message.chat.id == group_id_int:
        bot.delete_message(message.chat.id,message.message_id)
        print(message.chat.id)

@bot.message_handler(content_types=['left_chat_member'])
def left_user_message(message):
    if message.chat.type != "private" and message.chat.id == group_id_int:
        bot.delete_message(message.chat.id,message.message_id)


bot.polling(none_stop=True)
