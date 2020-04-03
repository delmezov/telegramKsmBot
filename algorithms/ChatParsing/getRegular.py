import re

glasn = 'ауоыиэяюёе'
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


'''
def find_word(string):
    reg_string = ""
    glasn = ['ауоыиэяюёе']
    if string[-1] in glasn:
    for i in string:
        reg_string += '[' + i + ']' + '{' + '1' + '}'
    return reg_string
    '''
