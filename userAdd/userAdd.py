from telethon import TelegramClient, sync, events, errors
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.channels import InviteToChannelRequest
import csv
from telethon import functions, types
import time
import random

api_id = 1256419

try_count = 0

api_hash = 'efa69c84e1f7eb38e19836ee3b279f7c'

group_name = "agro_zerno"

client = TelegramClient('session_name', api_id, api_hash).start()

#client(InviteToChannelRequest(users=[1186127399], channel=group_name))
print("EndStart")

participants = client.get_participants("info_zerno")
print("usersDownloaded")


test_users = []
with open ('usersToAdd.csv') as file:
    csv_reader = csv.reader(file, delimiter=',')
    for row in csv_reader:
        if row[0] == 'id':
            continue
        test_users.append(int(row[1]))



for user in test_users:
    try_count+=1
    if try_count == 50:
        time.sleep(600)
        try_count = 0
    try:
        if (user != 846395100) and (user != 50115079) and (user != 312511508) and (user != 988125925):
            client(InviteToChannelRequest(users=[user], channel=group_name))
            print(user, "User added")
    except errors.UserPrivacyRestrictedError:
        print("Низя {USER}".format(USER = user))
    except errors.UserAlreadyParticipantError:
        print("User already in group")
    except errors.UserNotMutualContactError:
        print("None mutual")
    except errors.PeerFloodError:
        print("wait 10 min")
        time.sleep(600)
        continue
    except ValueError:
        print("None value")
    time.sleep(random.randrange(60,120))
print("Finish")


'''
@client.on(events.ChatAction(chats=(group_name)))
async def normal_handler(event):
    if (event.user_added or event.user_joined):
        global participants 
        participants = await client.get_participants(group_name)

@client.on(events.NewMessage(chats=(group_name)))
async def normal_handler(event):
    
    message = event.message.to_dict()['message']
    user_id = event.message.to_dict()['from_id']

    print(user_id)
'''
'''
with open ('users.csv','a+', newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['id','UserID'])
    i = 1
    for user in participants:
        writer.writerow([i,user.id])
        i+=1
    print("I download all users ids")
'''

client.run_until_disconnected()



