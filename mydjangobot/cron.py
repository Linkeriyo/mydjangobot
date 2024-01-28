import discord

from mydjangobot import settings

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("discord client ready")
    channel = client.get_channel(settings.MICROSOFT_ACCOUNT_CHANNEL_ID)
    await channel.send('test')

def scheduled_job():
    client.run(settings.token)