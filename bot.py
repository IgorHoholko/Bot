from telethon import TelegramClient, sync
from telethon import functions, types
from telethon import utils
from telethon import events
import asyncio
import os


api_id =  os.environ['API_ID']                  # API ID (получается при регистрации приложения на my.telegram.org)
api_hash = os.environ['API_HASH']              # API Hash (оттуда же)
phone_number =  os.environ['PHONE_NUMBER']    # Номер телефона аккаунта, с которого будет выполняться код

client = TelegramClient('SomeName', api_id, api_hash).start()


username = '@ihoholko'
mak = '@nmakeychik'

me = client.get_me()
from telethon import utils
from telethon import events


# 
@client.on(events.NewMessage(incoming=True, chats=('+375 29 594 8978', 'Приватный канал')))
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
client.run(os.getenv('TOKEN'))