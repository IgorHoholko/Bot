from telethon import TelegramClient, sync
from telethon import functions, types
from telethon import utils
from telethon import events
import asyncio
import os
import telebot


token = os.environ['TOKEN']
MAIN_URL = 'https://api.telegram.org/bot{}/'.format(token)
api_id =  os.environ['API_ID']                  
api_hash = os.environ['API_HASH']              
phone_number =  os.environ['PHONE_NUMBER'] 
# chat = os.environ['CHAT_NAME']
output_channel = os.environ['OUTPUT_CHANNEL']
mirror_channel = os.environ['MIRROR_CHANNEL']

owner = '@ihoholko'


client = TelegramClient('SomeName', api_id, api_hash).start()


@client.on(events.NewMessage(incoming=True, chats=('Оп')))
async def handler(event):
	persone = event.client
	bot = telebot.TeleBot(token)

	dialogs = await persone.get_dialogs()
	message = dialogs[0].message.message
	# # await event.respond()

	# await client.send_message(owner, str(message) )
	# await bot.send_message(output_channel, str(message))
	await bot.send_message(mirror_channel, str(message))

	# result = await client(functions.messages.DeleteHistoryRequest(
	#    	peer=owner,
	#     max_id=0
	# ))

print("I'm working")
client.run_until_disconnected()
