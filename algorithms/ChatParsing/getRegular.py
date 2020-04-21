import re

glasn = 'ауоыиэяюёейь'
glasn_mas = list(glasn)

def find_word(string):
    reg_string = ""
    if string[-1] in glasn_mas:
        for i in string[:-1]:
            reg_string += '[' + i + ']' + '{' + '1' + '}'
        reg_string += '[' + glasn + ']'
    else:
        for i in string:
            reg_string += '[' + i + ']' + '{' + '1' + '}'
        reg_string += '[' + glasn + ']?'

    reg_string = '\\b' + reg_string + '\\b'
    return reg_string


def find_geo(string):
    reg_string = ""
    if string[-1] in glasn_mas:
        for i in string[:-1]:
            reg_string += '[' + i + ']' + '{' + '1' + '}'
        reg_string += '[' + glasn + ']'
    else:
        for i in string:
            reg_string += '[' + i + ']' + '{' + '1' + '}'
        reg_string += '[' + glasn + ']?'

    reg_string = '\\b' + reg_string
    #print(reg_string)
    return reg_string
    
def find_geo_name(string):
    
    reg_string = ""
    if len(string) > 4:
        for i in string[:-2]:
                reg_string += '[' + i + ']' + '{' + '1' + '}'
        reg_string = reg_string + '\S+'
    else:
        for i in string[:-1]:
                reg_string += '[' + i + ']' + '{' + '1' + '}'
        reg_string = '\\b' + reg_string + '\S+'

    return reg_string

print(find_geo_name('воронежская'))