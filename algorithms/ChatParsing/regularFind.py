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
    for i in counts:
        result = re.findall(r'' + getRegular.find_word(i), message)    
        if result != []:
            return result
    
    

print(get_found_word(message))


