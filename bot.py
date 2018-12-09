from telethon import TelegramClient, sync
from telethon import functions, types
from telethon import utils
from telethon import events
import asyncio
import os


api_id =  os.environ['API_ID']                  
api_hash = os.environ['API_HASH']              
phone_number =  os.environ['PHONE_NUMBER']    
username = '@ihoholko'
mak = '@nmakeychik'


client = TelegramClient('SomeName', api_id, api_hash).start()
# client.connect()
# if not client.is_user_authorized():
#     me = client.sign_in(bot_token = os.getenv('TOKEN'))





@client.on(events.NewMessage(incoming=True, chats=('+375 29 594 8978')))
async def handler(event):
	persone = event.client

	dialogs = await persone.get_dialogs()
	message = dialogs[0].message.message
	# # await event.respond()

	await client.send_message(mak, str(message)  )




	# result = await client(functions.messages.DeleteHistoryRequest(
	#    	peer=mak,
	#     max_id=0
	# ))

print("I'm working")
client.run_until_disconnected()
