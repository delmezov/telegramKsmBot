import regularFind
import re

def message_parsing(message):
    place = regularFind.get_found_place(message.lower())
    num = re.findall(r'' + regularFind.find_num, message)
    prod = regularFind.get_found_word(message.lower())
    buy_sell_ = regularFind.get_sell_or_prod(message.lower())
    
    if ((num) and (prod) and (buy_sell_) and (place)):
        return([num[0], prod, buy_sell_, place])