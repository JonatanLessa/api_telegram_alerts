import os 
from telethon import TelegramClient,sync,events
from time import sleep
import requests
from dotenv import load_dotenv
load_dotenv()
api_hash = os.getenv('API_HASH')
api_id = os.getenv('API_ID')

session = 'Forward messages'
# Function to forward messages
def main():
    print('Monitoring started...')
    client = TelegramClient(session, api_id, api_hash)
    #Method that waits for messages in the group passed by id
    @client.on(events.NewMessage(chats = [4143426144]))
    async def send_message(event):
        await client.send_message(1002159133551, event.raw_text)
    client.start()
    client.run_until_disconnected()

main()

# Function to get IDs of groups, channels and people
# def get_chats():

#     client = TelegramClient(session, api_id, api_hash)
#     client.start()
#     dialogs = client.get_dialogs()
#     for dialog in dialogs:
#         print('---------------------')
#         if dialog.id < 0:
#             print(f'Group: {dialog.title}')
#             print(f'id: {dialog.id}')
#         else:
#             print(f'Name: {dialog.title}')
#             print(f'id: {dialog.id}')
#         print('-------------\n')
#     client.disconnect()

# get_chats()