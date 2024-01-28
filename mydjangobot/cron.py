import discord

from mydjangobot import settings

client = discord.Client(intents=discord.Intents.default())

async def scheduled_job():
    client.run(settings.token)
    
    channel = client.get_channel(settings.MICROSOFT_ACCOUNT_CHANNEL_ID)
    await channel.send('test')