import telebot
import config
import time
from telebot import types
import adv_functions
from telebot import apihelper
from time import time
import saveLogToFile
import re
import text_on_image

try:
    apihelper.proxy = config.proxy_const_ukr
except Exception:
    errorProxy = "Proxy UKR not working"
    saveLogToFile.save_log_to_file(config.file_path_name, errorProxy)
else:
    apihelper.proxy = config.proxy_const_ger

bot = telebot.TeleBot(config.token)
user_dict = {}


def log_new_message(message):
    print("\n ------")
    from datetime import datetime

    #Форматиррованная запись сохранения
    str_log = ("Сообщение от пользователя {0.first_name} {1.last_name}. id = {2}  Текст = {3.text}".format(message.from_user, message.from_user, str(message.from_user.id), message))
    
    print(str_log) #Вывод логов в файл
    saveLogToFile.save_log_to_file(config.file_path_name, str_log) #сохранение лога в файл


@bot.message_handler(commands=['example'])
def example_message(message):
    bot.send_message(message.chat.id, config.exmple_message, parse_mode = "HTML")

@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, config.strart_message, parse_mode = "HTML")

@bot.message_handler(commands=['rules'])
def rules_message(message):
    bot.send_message(message.chat.id, config.rules_message, parse_mode = "HTML")

@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    if message.chat.type != "private":
        user_name = message.new_chat_member.first_name
        bot.send_message(message.chat.id, config.greeting_message_public.format(user_name), parse_mode = "HTML")

@bot.message_handler(func=lambda message: message.entities is not None and message.chat.id == bot.get_chat('@Test_group_123zz').id)
def delete_links(message):
    for entity in message.entities:
        if entity.type in ["url", "text_link"]: 
            bot.delete_message(message.chat.id, message.message_id)
        else:
            return

@bot.message_handler(content_types=['sticker'])
def sticker_checker(message):
    if message.chat.id == bot.get_chat('@ksmagro').id:
        bot.delete_message(message.chat.id, message.message_id)
        bot.restrict_chat_member(bot.get_chat('@ksmagro').id, message.from_user.id, until_date=time()+60)

@bot.message_handler(commands=['start'])
def start_message(message):
    if message.chat.type == "private":
        log_new_message(message)
        user_dict[message.chat.id] = [message.chat.id]
        bot.send_message(message.chat.id, config.greeting_message.format(message.from_user, bot.get_me()), parse_mode = "HTML")
        bot.send_message(message.chat.id, config.сommands_message, parse_mode = "HTML")
        bot.send_message(message.chat.id, config.buy_sell_message, parse_mode = "HTML", reply_markup = config.buy_sell_keyboard) #buy_sell_keyboard

@bot.message_handler(content_types=['text'])
def choose_sell_buy(message):
    if message.chat.type == "private":
        log_new_message(message)

        if message.text == 'Покупка' and isinstance(message.text, str) and (message.chat.id in user_dict) == True:
            bot.register_next_step_handler(bot.send_message(message.chat.id, config.type_of_product, reply_markup = config.seed_keyboard), product_descriptions) #seed_keyboard
            user_dict[message.chat.id].append(message.text)
        elif message.text == 'Продажа' and isinstance(message.text, str) and (message.chat.id in user_dict) == True:
            bot.register_next_step_handler(bot.send_message(message.chat.id, config.type_of_product, reply_markup = config.seed_keyboard), product_descriptions) #seed_keyboard
            user_dict[message.chat.id].append(message.text)
        else:
            bot.send_message(message.chat.id, config.error_message, parse_mode = "HTML", reply_markup = config.start_keybord)
    else:
        result = re.findall(r'' + config.triger_words, message.text)    
        if result != []:
            bot.delete_message(message.chat.id, message.message_id)
            bot.restrict_chat_member(bot.get_chat('@ksmagro').id, message.from_user.id, until_date=time()+60)

def product_descriptions(message):
    log_new_message(message)
    user_dict[message.chat.id].append(message.text)
    flag = False
    
    for seed_count in config.seeds.keys():
        if message.text == seed_count:
            bot.register_next_step_handler(bot.send_message(message.chat.id, config.seeds[seed_count], reply_markup = types.ReplyKeyboardRemove()), get_contact)
            flag = True
            break
        
    if flag == False:
        bot.send_message(message.chat.id, config.error_message, parse_mode = "HTML", reply_markup = config.start_keybord)

def get_contact(message):
    log_new_message(message)
    if isinstance(message.text, str) and len(message.text) <= 300:
        user_dict[message.chat.id].append(message.text)
        bot.register_next_step_handler(bot.send_message(message.chat.id, config.get_contact_message), end_poll)
    else:
        bot.send_message(message.chat.id, config.error_message, parse_mode = "HTML", reply_markup = config.start_keybord)

def end_poll(message):
    log_new_message(message)
    if isinstance(message.text, str) and len(message.text) < 80:
        user_dict[message.chat.id].append(message.text)
        print(user_dict)
        bot.send_photo(message.chat.id, open(text_on_image.text_on_image_(user_dict[message.chat.id][0], user_dict[message.chat.id][1], user_dict[message.chat.id][2], user_dict[message.chat.id][3], user_dict[message.chat.id][4]), 'rb'))
        bot.register_next_step_handler(bot.send_message(message.chat.id, config.check_message + "\n" + adv_functions.list_to_string(user_dict[message.chat.id]), parse_mode="HTML", reply_markup = config.choose_end_keybord), delete_keybord)
    else:
        bot.send_message(message.chat.id, config.error_message ,parse_mode = "HTML", reply_markup = config.start_keybord)

def delete_keybord(message):
    log_new_message(message)
    if message.text == 'Всё верно!':  
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text="Перейти на объявление!", url="https://t.me/ksmagro")
        keyboard1 = types.InlineKeyboardMarkup()
        url_button1 = types.InlineKeyboardButton(text="Написать объявление", url="https://t.me/ksmagrobot")
        keyboard.add(url_button)
        keyboard1.add(url_button1)
        bot.send_message(message.chat.id, config.last_message, parse_mode = "HTML", reply_markup = keyboard)
        
        bot.send_photo(bot.get_chat('@ksmagro').id, open(text_on_image.text_on_image_(user_dict[message.chat.id][0], user_dict[message.chat.id][1], user_dict[message.chat.id][2], user_dict[message.chat.id][3], user_dict[message.chat.id][4]), 'rb'), config.who_send_message.format(message.from_user.first_name, message.from_user.last_name, message.from_user.username), parse_mode = "HTML", reply_markup=keyboard1)


        #bot.send_message(message.chat.id, config.last_message, parse_mode = "HTML", reply_markup = types.ReplyKeyboardRemove())

       #bot.send_message(bot.get_chat('@ksmagro').id, adv_functions.list_to_string(user_dict[message.chat.id]) + config.who_send_message.format(message.from_user.first_name, message.from_user.last_name, message.from_user.username), parse_mode = "HTML")
        
        del user_dict[message.chat.id]
        bot.send_message(message.chat.id, config.start_again_message, reply_markup = config.start_keybord) 

    elif message.text == 'Заполнить заново':
    
        del user_dict[message.chat.id]
        
        user_dict[message.chat.id] = [message.chat.id]
        bot.register_next_step_handler(bot.send_message(message.chat.id, config.buy_sell_message, parse_mode = "HTML", reply_markup = config.buy_sell_keyboard), choose_sell_buy) 




while True:
    try:
        bot.infinity_polling(True)
    except Exception as e:
        print(e)