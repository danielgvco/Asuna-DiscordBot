import discord
import asyncio

async def disappear_message(message):
    await message.delete()

async def delete_message(message):
    author = message.author.mention
    channel = message.channel
    await message.delete()
    await channel.send(f"A message from {author} was deleted.")

async def ban_author(message):
    guild = message.guild
    author = message.author
    await guild.ban(author, reason="Banned by bot.")

async def kick_author(message):
    guild = message.guild
    author = message.author
    await guild.kick(author, reason="Kicked by bot.")