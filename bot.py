from dotenv import load_dotenv
import discord
import os

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
TEST_GUILD_ID = os.getenv('TEST_GUILD_ID')

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
            await message.reply('Invalid ASIN received. Message should be in this format: -asin <ASIN_ID>', mention_author=True)
            return
        # print('Message received: ' + message.content)
        asin_id = message.content.strip().split(' ')[1]
        print('ASIN received: ' + asin_id)
        await message.reply('**Showing graph with ASIN:** `' + asin_id + '`', mention_author=True)

client.run(DISCORD_TOKEN)
