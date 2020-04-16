import getRegular
import re
import geos_names

find_num = '[-+]?[7|8]\s?[-]?[(]?[0-9][0-9][0-9]\s?[-]?[)]?\s?[-]?[0-9]\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9]'

counts = ['Пшеница', 'Ячмень', 'Соя','Горох','Кукуруза','Семечка','Лен','Льна']

geos = ['район','край','область','обл','республика','р-ка']

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

def get_found_place(message):
    for el in geos:
        result = re.findall(r'' + getRegular.find_geo(el.lower()), message)    
        if result != []:
            #print(result[0])
            
            message = clean_message(message)
            message = message.split()
            for i in range(len(message)):
                if result[0] in message[i]:
                    message[i] = result[0]
            
            if el == "область" or el == "обл":
                #print(message)
                try_geo = get_found_geos_name(message[message.index(result[0])-1],geos_names.obl)
                if try_geo:
                    return try_geo + " " + "обл"
                else:
                    try:
                        return "обл" + " " + get_found_geos_name(message[message.index(result[0])+1],geos_names.resp)
                    except TypeError:
                        return message[message.index(result[0])-1] + " " + "обл"
                    except IndexError:
                        return message[message.index(result[0])-1] + " " + "обл"
            if el == "край":
                try_geo = get_found_geos_name(message[message.index(result[0])-1],geos_names.reg)
                if try_geo:
                    return try_geo + " " + "край"
                else:
                    try:
                        return "край" + " " + get_found_geos_name(message[message.index(result[0])+1],geos_names.resp)
                    except TypeError:
                        return message[message.index(result[0])-1] + " " + "край"
                    except IndexError:
                        return message[message.index(result[0])-1] + " " + "обл"
            
            if el == "республика" or el == "р-ка":
                try_geo = get_found_geos_name(message[message.index(result[0])-1],geos_names.resp)
                if try_geo:
                    return try_geo + " " + "республика"
                else:
                    try:
                        return "республика" + " " + get_found_geos_name(message[message.index(result[0])+1],geos_names.resp)
                    except TypeError:
                        return message[message.index(result[0])-1] + " " + "республика"
                    except IndexError:
                        return message[message.index(result[0])-1] + " " + "обл"
            else:
                return message[message.index(result[0])-1] + " " + result[0]

def get_found_geos_name(message, geo_names):
    for geo in geo_names:
        result = re.findall(r'' + getRegular.find_geo_name(geo.lower()), message)    
        if result != []:
            return geo
            
def remove_emoji(string):
    emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', string)
    
    
def clean_message(message):
    message = message.replace('.'," ")
    message = message.replace(','," ")
    message = message.replace('!'," ")
    message = message.replace('?'," ")
    message = message.replace('-'," ")
    message = message.replace('\n'," ")
    message = message.replace(')'," ")
    message = message.replace('('," ")
    message = message.replace(';'," ")
    message = message.replace(':'," ")
    message = remove_emoji(message)

    return message

