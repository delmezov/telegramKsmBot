def find_word(string):
    reg_string = ""
    '''
    for i in string:
        reg_string += '[' + i + ']' + '{' + '1' + '}'
    '''
    reg_string = '[' + string + ']' + '{' + str(len(string)) + '}' + '\w+'
    return reg_string


