from bs4 import BeautifulSoup
import requests
import regularFind
import re

adv_dict = {}
find_num = '[-+]?[7|8]\s?[-]?[(]?[0-9][0-9][0-9]\s?[-]?[)]?\s?[-]?[0-9]\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9]'
#buy_or_sell = '[а-я]{0,2}[к][у][п]\w+'


def get_html(url):
    r = open(url, 'r')
    return r.read()

page = get_html('History/messages41.html')
soup = BeautifulSoup(page,'lxml')
for tag in soup.find_all('div', {'class':'message'} and {'class':'default'} and {'class':'clearfix'}):
    if (tag.find('div', {'class': "from_name"}) != None):
        user = tag.find('div', {'class': "from_name"}).text.strip()
    if (tag.find('div', {'class': "text"}) != None):
        message = tag.find('div', {'class': "text"}).text

        num = re.findall(r'' + find_num, message )
        prod = regularFind.get_found_word(message.lower())
        buy_sell_ = regularFind.get_sell_or_prod(message.lower())
    if (num) and (prod) and (buy_sell_):    
        adv_dict[user] = [buy_sell_, prod, num[0]]



for el in adv_dict:
    print(el + '   ' + str(adv_dict.get(el)))


print(len(adv_dict))
'''
Покупка Куплю Закупаю Закупка Купим Купля Закупаем 
'''