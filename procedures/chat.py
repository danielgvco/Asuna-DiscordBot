import os
import discord
from utils import *

async def chat(data, limit=6):
    active = helper.get_value_from_json("config.json", "chat", "active")
    if helper.true_or_false(active) == False:
        return
    
    message = data["message"]

    client = data["client"]
    history = await helper.get_channel_history(data, limit)
    formatted_history = helper.format_chat_dictionary_list(history, client)
    
    await message.reply(openai_utils.generate_chat(formatted_history))