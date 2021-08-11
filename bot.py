from discord.ext import commands, tasks
from dotenv import load_dotenv
from keepa import fetch_graph
import asyncio
import discord
import io
import os
import sys
from signal import SIGINT, SIGTERM

load_dotenv()
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
error_string = 'Invalid ASIN received. Message should be in this format: -asin <ASIN_ID>'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )
    
        
@client.event
async def on_message(message):
    if (message.content.startswith('-asin')):
        words = message.content.strip().split(' ')
        if len(words) != 2:
            # print('Invalid ASIN received. Message: ' + message.content.strip())
            await message.reply(error_string, mention_author=True)
            return
        # print('Message received: ' + message.content)
        asin_id = message.content.strip().split(' ')[1]
        print('ASIN received: ' + asin_id)
        
        response = fetch_graph(asin_id)
        if response.status_code >= 400:
            await message.reply('**ERROR: Encountered issue with Keepa API token. Please check your Keepa token value!**')
        elif not validate_asin(asin_id):
            await message.reply(error_string, mention_author=True)
        else:
            # for 200, it will always return an PNG image, even if the ASIN is incorrect
            # pass the image blob to the discord file
            image = io.BytesIO(response.content)
            await message.reply('**Showing graph with ASIN:** `' + asin_id + '`\n' + 'https://www.amazon.com/dp/' + asin_id, file=discord.File(image, 'graph.png'), mention_author=True)
            

def validate_asin(asin_id):
    return len(asin_id) == 10 and (asin_id.startswith('BT') or asin_id.startswith('B0'))

client.run(DISCORD_TOKEN)


if __name__ == '__main__':
	if not DISCORD_TOKEN:
		print('Error: DISCORD_TOKEN not found')
		sys.exit(1)

	loop = asyncio.get_event_loop()

	def interrupt():
		raise KeyboardInterrupt

	loop.add_signal_handler(SIGINT, interrupt)
	loop.add_signal_handler(SIGTERM, interrupt)

	try:
		loop.run_until_complete(client.run(DISCORD_TOKEN))
	except KeyboardInterrupt:
		pass
	finally:
		loop.run_until_complete(client.close())