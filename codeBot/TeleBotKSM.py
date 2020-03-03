import telebot
import constants
import saveLogToFile


bot = telebot.TeleBot(constants.token)

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
        





bot.polling()
