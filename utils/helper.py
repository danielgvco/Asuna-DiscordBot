import discord
import asyncio
import os
import json
import tiktoken

async def channel_history2(data, limit=6):
    message = data["message"]
    client = data["client"]
    channel = message.channel
    formatted_messages = []

    async for msg in channel.history(limit=limit):
        role = "assistant" if msg.author == client.user else "user"
        formatted_messages.append({"role": role, "content": msg.content})

    formatted_messages = formatted_messages[::-1]
    formatted_messages.insert(0, {"role": "system", "content": "You're a friendly Discord Bot called Asuna.\nBe as useful as possible.\ntry to reply in the users own language."})

    return formatted_messages

async def channel_history(data, limit=6):
    client = data["client"]
    history = await get_channel_history(data, limit)
    formatted_history = format_chat_dictionary_list(history, client)
    return formatted_history

async def get_channel_history(data, limit):
    message = data["message"]
    channel = message.channel
    history = []

    async for msg in channel.history(limit=limit):
        history.append(msg)

    return history

def format_chat_plain_text(history, client):
    formatted_messages = []

    for msg in history:
        if msg.author != client.user:
            author_name = msg.author.display_name
            formatted_messages.append(f"{author_name}: {msg.content}")

    formatted_messages = formatted_messages[::-1]
    formatted_string = "\n".join(formatted_messages)

    return formatted_string

def format_chat_dictionary_list(history, client):
    formatted_messages = []

    for msg in history:
        role = "assistant" if msg.author == client.user else "user"
        formatted_messages.append({"role": role, "content": msg.content})

    formatted_messages = formatted_messages[::-1]
    formatted_messages.insert(0, {"role": "system", "content": "You're a friendly Discord Bot called Asuna.\nBe as useful as possible.\ntry to reply in the users own language."})

    return formatted_messages

def format_chat_author(history, client, author):
    formatted_messages = []

    for msg in history:
        if msg.author == author and msg.author != client.user:
            author_name = msg.author.display_name
            formatted_messages.append(f"{author_name}: {msg.content}")

    formatted_messages = formatted_messages[::-1]
    formatted_string = "\n".join(formatted_messages)

    return formatted_string

def num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301"):
  """Returns the number of tokens used by a list of messages."""
  try:
      encoding = tiktoken.encoding_for_model(model)
  except KeyError:
      encoding = tiktoken.get_encoding("cl100k_base")
  if model == "gpt-3.5-turbo-0301":  # note: future models may deviate from this
      num_tokens = 0
      for message in messages:
          num_tokens += 4  # every message follows <im_start>{role/name}\n{content}<im_end>\n
          for key, value in message.items():
              num_tokens += len(encoding.encode(value))
              if key == "name":  # if there's a name, the role is omitted
                  num_tokens += -1  # role is always required and always 1 token
      num_tokens += 2  # every reply is primed with <im_start>assistant
      return num_tokens
  else:
      raise NotImplementedError(f"""num_tokens_from_messages() is not presently implemented for model {model}.
  See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens.""")

def true_or_false(value):
    true_values = ['true', 'yes', 'y', '1']
    false_values = ['false', 'no', 'n', '0']

    clean_value = value.replace(".", "").replace(",", "").lower().strip()

    if clean_value in true_values:
        return True
    elif clean_value in false_values:
        return False
    else:
        return None

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
        
def get_value_from_json(file_path, key, sub_key=None):
    content = read_file(file_path)
    json_content = json.loads(content)
    
    if sub_key is not None:
        return json_content[key][sub_key]
    else:
        return json_content[key]