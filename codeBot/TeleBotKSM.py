import telebot
import config
import saveLogToFile
from telebot import types

bot = telebot.TeleBot(config.token)

buy_sell_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
buy_sell_keyboard.row('Покупка', 'Продажа')

seed_keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
seed_keyboard.row('Рис', 'Соя', 'Горох', 'Ячмень')
saved_string = ""

choose_end_keybord = telebot.types.ReplyKeyboardMarkup(True, True)
choose_end_keybord.row('Всё верно!', 'Заполнить заново')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать {0.first_name}! вас приветствует {1.first_name}. Я помогу выставить ваше объявление просто следйуте инструкциям: ".format(message.from_user, bot.get_me()))
    bot.send_message(message.chat.id, "1) Покупаем или продаём(Выберите кнопку)", reply_markup=buy_sell_keyboard)

@bot.message_handler(content_types=['text'])
def choose_sell_buy(message):
    global saved_string
    if message.text == 'Покупка':
        bot.register_next_step_handler(bot.send_message(message.chat.id, "2) Выберите продукт для покупки: ", reply_markup=seed_keyboard), product_descriptions)
        saved_string += message.text
    elif message.text == 'Продажа':
        bot.register_next_step_handler(bot.send_message(message.chat.id, "2) Выберите продукт для продажи: ", reply_markup=seed_keyboard), product_descriptions)
        saved_string += '\n' + message.text

def product_descriptions(message):
    global saved_string
    saved_string += '\n' + message.text
    bot.register_next_step_handler(bot.send_message(message.chat.id, "3) Укажите основные характеристики товара(Цена/Вес/Регион)", reply_markup = types.ReplyKeyboardRemove()), get_contact)
    

def get_contact(message):
    global saved_string
    saved_string += '\n' + message.text
    bot.register_next_step_handler(bot.send_message(message.chat.id, "4) Укажите контактные данные:"), end_poll)

def end_poll(message):
    global saved_string
    saved_string += '\n' + message.text
    bot.register_next_step_handler(bot.send_message(message.chat.id, "Спасибо за терпение, проверьте всё ли верно:\n " + saved_string, reply_markup=choose_end_keybord), delete_keybord)
    #bot.register_next_step_handler(bot.send_message((message.chat.id, "Спасибо за терпение, проверьте всё ли верно:\n " + saved_string), reply_markup = choose_end_keybord), delete_keybord)

    print(saved_string)
    saved_string = ""

def delete_keybord(message):
    bot.send_message(message.chat.id, "Спасибо ваше объявление отправлено", reply_markup = types.ReplyKeyboardRemove())



                
bot.polling(none_stop=True)



'''
def log_new_message(message):
    print("\n ------")
    from datetime import datetime

    #Форматиррованная запись сохранения
    str_log = ("Сообщение от пользователя {0.first_name} {1.last_name}. id = {2}  Текст = {3.text}".format(message.from_user, message.from_user, str(message.from_user.id), message))
    
    print(str_log) #Вывод логов в файл
    saveLogToFile.save_log_to_file(constants.file_path_name, str_log) #сохранение лога в файл

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Добро пожаловать на канал {0.first_name}, ознокомтись с правилами нашей группы:!\n Я - {1.first_name}".format(message.from_user, bot.get_me()))
    

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text:
        bot.send_message(constants.chat_ksm_test_004, message.text)
        log_new_message(message)
        '''



