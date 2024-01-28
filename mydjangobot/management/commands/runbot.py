import random

import discord
from mydjangobot import discordbot_settings
from mydjangobot import slash_commands
from mydjangobot.botcommands.ping import command as pingcommand
from mydjangobot.botcommands.wake import command as wakecommand
from mydjangobot.botcommands.whereareyou import command as whereareyoucommand
from mydjangobot.funny_data import INSULTS

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name='linkeriyo')
client = discord.Client(intents=intents, activity=activity)


@client.event
async def on_ready():
    print("discord client ready")
    await slash_commands.initialize_commands(client)


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if not message.content.startswith(discordbot_settings.prefix):
        return

    content = message.content[len(discordbot_settings.prefix):]

    words = content.split(" ")

    if len(words) == 0:
        return

    if words[0] == "wake":
        await wakecommand.run(message, words[1:])
    elif words[0] == "whereareyou":
        await whereareyoucommand.run(message, words[1:])
    elif words[0] == "ping":
        await pingcommand.run(message, words[1:])
    elif words[0] == "sync" and message.author.id == 154268434090164226:
        await slash_commands.initialize_commands(client)
    else:
        await message.reply('que dices')

print("discord client initialized")

client.run(discordbot_settings.token)
