import random
import discord
from mydjangobot.botcommands.wake import command as wakecommand
from mydjangobot.botcommands.ping import command as pingcommand
from mydjangobot.botcommands.fakedelete import command as fakedeletecommand
from mydjangobot.botcommands.debt_add import command as adddebtcommand
from mydjangobot.botcommands.debt_pay import command as paydebtcommand
from mydjangobot.botcommands.debt_list import command as listdebtcommand
import mydjangobot.discordbot_settings as settings
from mydjangobot.funny_data import INSULTS

intents = discord.Intents.default()
intents.message_content = True

activity = discord.Activity(type=discord.ActivityType.listening, name='tests')
client = discord.Client(intents=intents, activity=activity)

@client.event
async def on_ready():
    print("discord client ready")

@client.event
async def on_message(message):
    if message.author.bot:
        return
        
    if not message.content.startswith(settings.prefix):
        return

    content = message.content[len(settings.prefix):]

    words = content.split(" ")

    if len(words) == 0:
        return  

    if words[0] == "wake":
        await wakecommand.run(message, words[1:])
    elif words[0] == "ping":
        await pingcommand.run(message, words[1:])
    elif words[0] == ";DELETE":
        await fakedeletecommand.run(message, words[1:])
    elif words[0] == "debt":
        try:
            if words[1] == "add":
                await adddebtcommand.run(message, words[1:])
            elif words[1] == "pay":
                await paydebtcommand.run(message, words[1:])
            elif words[1] == "list":
                await listdebtcommand.run(message, words[1:])
            else:
                await message.reply("Argumentos posibles: add, pay, list")
        except:
            await message.reply("Argumentos posibles: add, pay, list")
    elif words[0] == "insult":
        await message.reply(random.choice(INSULTS))
    else:
        await message.reply('que dices')

print("discord client initialized")

client.run(settings.token)
