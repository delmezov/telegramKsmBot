from bs4 import BeautifulSoup
import requests
import regularFind
import re


adv_dict = {}

find_num = '[-+]?[7|8]\s?[-]?[(]?[0-9][0-9][0-9]\s?[-]?[)]?\s?[-]?[0-9]\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9][-]?\s?[0-9]\s?[0-9]'

def get_html(url):
    r = open(url, 'r')
    return r.read()

page = get_html('History/messages41.html')
soup = BeautifulSoup(page,'lxml')
for tag in soup.find_all('div', {'class':'message'} and {'class':'default'} and {'class':'clearfix'}):
    #print("=====================================")
    if (tag.find('div', {'class': "from_name"}) != None):
        user = tag.find('div', {'class': "from_name"}).text.strip()
        #print(user)
    if (tag.find('div', {'class': "text"}) != None):
        
        message = tag.find('div', {'class': "text"}).text
        num = re.findall(r''+find_num, message )
        prod = regularFind.get_found_word(message.lower())

    if (num) and (prod):    
        adv_dict[user] =[prod, num]

print(adv_dict.items)



for el in adv_dict:
    print(el + '   ' + str(adv_dict.get(el)))
