import getRegular
import re


counts = ['пшеница', 'ячмень', 'соя','горох','кукуруза','семечка','лен','льна']

result = ""

message = """Срочно куплю кукурузу ГОСТ
2 тыс тонн
Влага 14, сор 5, зерновая 15
Декларация на продовольственное зерно

100% Предоплата СХТП
Вывозим только своим автотранспортом

Рязанская, Тульская, Липецкая, Тамбовская области"""

def get_found_word(message):
    for prod in counts:
        result = re.findall(r'' + getRegular.find_word(prod), message)    
        if result != []:
            return prod
'''
def test(message):
    for el in count_for_sell:
        result = re.findall(r'' + el, message)    
        if result != []:
            return result
'''

def get_sell_or_prod(message):
    if (re.findall(r'' + '[а-я]{0,2}[к][у][п]\w+', message)):
        return 'Покупка'
    if (re.findall(r'' + '\\b[п|П][р][о][д][а]\w+', message)):
        return 'Продажа'
    
    


