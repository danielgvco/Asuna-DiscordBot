import os
import discord
from dotenv import load_dotenv
from utils import *
from procedures import *

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

ssl_cert_file = os.getenv('SSL_CERT_FILE')
    
if ssl_cert_file:
    os.environ['SSL_CERT_FILE'] = ssl_cert_file

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
    
    print(f"{message.author}: {message.channel}: {message.content}")
    
    data = {
        "message": message,
        "client": client
        }
    
    answer = openai_utils.high_moderation(message.content)
    if answer:
        await moderation.delete_message(message)
        return
    elif answer == None:
        await moderation.disappear_message(message)
        return

    #messages = await chat.chat(data)
    #await message.reply(openai_utils.generate_chat(messages))
    await chat.chat(data)
        

client.run(TOKEN)