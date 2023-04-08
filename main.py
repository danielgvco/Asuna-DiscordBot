import os
import discord
from dotenv import load_dotenv
from utils import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Initialize the Discord client
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'\n{client.user} is online!\n')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    data = {
        "message": message,
        "client": client
        }
    
    rules = helper.read_file('resources/rules.md')
    answer = openai_utils.high_moderation(message.content, rules)
    if not answer:
        await moderation.delete_message(message)
    else:
        messages = await helper.channel_history(data)
        await message.channel.send(openai_utils.generate_chat(messages))
        

client.run(TOKEN)