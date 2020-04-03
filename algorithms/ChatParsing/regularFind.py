import getRegular
import re

find_num = '[-+]?[7|8]\s?[-]?[(]?[0-9][0-9][0-9]\s?[-]?[)]?\s?[-]?[0-9]\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9]'

counts = ['Пшеница', 'Ячмень', 'Соя','Горох','Кукуруза','Семечка','Лен','Льна']

result = ""


def get_found_word(message):
    for prod in counts:
        result = re.findall(r'' + getRegular.find_word(prod.lower()), message)    
        if result != []:
            return prod


def get_sell_or_prod(message):
    if (re.findall(r'' + '[а-я]{0,2}[к][у][п]\w+', message)):
        return 'Покупка'
    if (re.findall(r'' + '\\b[п|П][р][о][д][а]\w+', message)):
        return 'Продажа'
    
    


