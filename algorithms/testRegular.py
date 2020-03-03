import re
#Проверка
#Слишком плохой код
'''
str_ = 'Здравствуйте предлагаю пшеницу 3 класНатура 750-770 ЧП 200-360 Влага 13,5 Объем 800 тонн Цена с доставкой в Москве, Санкт-Петербурге, Астрахани 14200 р/тн с НДС'
reg = '[п]{1}[ш]{1}[е]{1}[н]{1}[и]{1}[ц]{1}\w+'
result = re.findall(r'' + reg, str_)
print(result)
#[П|п]{1}[ш|Ш]{1}[е|Е]{1}[н|Н]{1}[и|И]{1}[ц|Ц]{1}\w+
'''
string = "Пшениц"
string_ = ""

for i in string:
    string_ += i.lower()
string = string_

reString = ""

for i in string:
    reString += "[" + i + ']' + '{' + '1' + '}'

reString_ = reString + "\w+"

#print(reg)
print(reString_)

str_ = 'Здравствуйте предлагаю пшеницу 3 класНатура 750-770 ЧП 200-360 Влага 13,5 Объем 800 тонн Цена с доставкой в Москве, Санкт-Петербурге, Астрахани 14200 р/тн с НДС'
result_ = re.findall(r'' + reString_, str_)
print(result_)


''''
for i in len(re_string) :
    print(i)

re_string.lower()
print(re_string)

s = "str"
print(s[0].upper())

print(s)'''
