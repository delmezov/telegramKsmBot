from bs4 import BeautifulSoup
import requests
import regularFind
import re
from database import Database

adv_dict = {}
db = Database()

def get_html(url):
    r = open(url, 'r')
    return r.read()
for i in range(2,42):
    page = get_html('History/messages' + str(i) + '.html')
    soup = BeautifulSoup(page,'lxml')
    for tag in soup.find_all('div', {'class':'message'} and {'class':'default'} and {'class':'clearfix'}):
        if (tag.find('div', {'class': "from_name"}) != None):
            user = tag.find('div', {'class': "from_name"}).text.strip()
        if (tag.find('div', {'class': "text"}) != None):
            message = tag.find('div', {'class': "text"}).text
        if (tag.find('div', {'class': "date"}) != None):
            data = tag.find('div', {'class': "date"})['title']
            data = data[0:data.find(' ')]

            num = re.findall(r'' + regularFind.find_num, message )
            prod = regularFind.get_found_word(message.lower())
            buy_sell_ = regularFind.get_sell_or_prod(message.lower())

        if (num) and (prod) and (buy_sell_):    
            adv_dict[user] = [user, buy_sell_, prod, num[0], data]
            db.insert_data(adv_dict.get(user))


'''
for el in adv_dict:
    print(el + '   ' + str(adv_dict.get(el)))


print(len(adv_dict))
'''