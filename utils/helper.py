import discord
import asyncio
import os
import json

async def channel_history(data, limit=10):
    message = data["message"]
    client = data["client"]
    channel = message.channel
    formatted_messages = []

    async for message in channel.history(limit=limit):
        role = "assistant" if message.author == client.user else "user"
        formatted_messages.append({"role": role, "content": message.content})

    formatted_messages = formatted_messages[::-1]
    formatted_messages.insert(0, {"role": "system", "content": "You're a friendly Discord Bot called Asuna.\nBe as useful as possible.\ntry to reply in the users own language."})

    return formatted_messages

def read_file(file_path):
    _, ext = os.path.splitext(file_path)

    with open(file_path, 'r') as file:
        content = file.read()

        if ext == '.json':
            try:
                json_content = json.loads(content)
                return json.dumps(json_content, indent=2)
            except json.JSONDecodeError as e:
                return f"Error decoding JSON file: {e}"
        else:
            return content
        
def get_value_from_json(file_path, key):
    content = read_file(file_path)
    json_content = json.loads(content)
    return json_content[key]