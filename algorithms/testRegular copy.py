import re

string = "Семечк"
string_ = ""

for i in string:
    string_ += i.lower()

reString = '[' + string_ + ']' + '{' + str(len(string_)) + '}' + '\w+'

str_ = 'Здравствуйте предлагаю семечка 3 класНатура 750-770 ЧП 200-360 Влага 13,5 Объем 800 тонн Цена с доставкой в Москве, Санкт-Петербурге, Астрахани 14200 р/тн с НДС'
result_ = re.findall(r'' + reString, str_)

print(result_)
print(reString)

