from telethon import TelegramClient, sync, events
import time
from messageParsing import message_parsing
import csv

api_id = 1221890

api_hash = 'b030bedaaa6b3465fd6279e9bac47846'

group_name = 'testksm1'

client = TelegramClient('session_name', api_id, api_hash).start()

participants = client.get_participants(group_name)

@client.on(events.ChatAction(chats=(group_name)))
async def normal_handler(event):
    if (event.user_added or event.user_joined):
        global participants 
        participants = await client.get_participants(group_name)

@client.on(events.NewMessage(chats=(group_name)))
async def normal_handler(event):
    
    message = event.message.to_dict()['message']
    adv_info = message_parsing(message)

    date = event.message.to_dict()['date']
    date = str(date.strftime("%d.%m.%Y"))
    
    user_id = event.message.to_dict()['from_id']
    user_all_info = await client.get_entity(user_id)

    if (user_all_info.last_name) and (user_all_info.first_name):
        user_full_name = user_all_info.first_name + " " + user_all_info.last_name
    elif (user_all_info.first_name):
        user_full_name = user_all_info.first_name
    else:
        user_full_name = None

    if (adv_info):
        adv_info = [user_full_name] + adv_info + [date]
        with open ('advs.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer = writer.writerow(adv_info)
            
    
 
    
    











client.run_until_disconnected()

