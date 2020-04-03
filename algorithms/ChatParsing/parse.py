from bs4 import BeautifulSoup
import requests
import regularFind
import re

adv_dict = {}
find_num = '[-+]?[7|8]\s?[-]?[(]?[0-9][0-9][0-9]\s?[-]?[)]?\s?[-]?[0-9]\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9]'
buy_or_sell = '(\\b[п][о][к][у][п]\w+\\b)|(\\b[п][р][о][д][а]\w+\\b)|(\\b[к][у][п][л]?[и]?\w+\\b)'

def get_html(url):
    r = open(url, 'r')
    return r.read()

page = get_html('messages41.html')
soup = BeautifulSoup(page,'lxml')
for tag in soup.find_all('div', {'class':'message'} and {'class':'default'} and {'class':'clearfix'}):
    if (tag.find('div', {'class': "from_name"}) != None):
        user = tag.find('div', {'class': "from_name"}).text.strip()
    if (tag.find('div', {'class': "text"}) != None):
        message = tag.find('div', {'class': "text"}).text

        num = re.findall(r'' + find_num, message )
        prod = regularFind.get_found_word(message.lower())
        buy_sell_ = re.findall(r'' + buy_or_sell, message.lower())
    if (num) and (prod) and (buy_sell_):    
        adv_dict[user] = [buy_sell_, prod, num]

print(adv_dict.items)



for el in adv_dict:
    print(el + '   ' + str(adv_dict.get(el)))
