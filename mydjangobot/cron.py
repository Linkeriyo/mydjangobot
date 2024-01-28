import discord

from mydjangobot import settings
from mydjangobot import discordbot_settings
from datetime import datetime, timedelta

client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_ready():
    print("discord client ready")
    channel = client.get_channel(settings.MICROSOFT_ACCOUNT_CHANNEL_ID)
    await channel.send('@here pagad el gamepass 1.70€, gracias')
    await client.close()


def scheduled_job():
    if date_check():
        client.run(discordbot_settings.token)


def date_check():
    today = datetime.now()
    tomorrow = today + timedelta(days=1)
    return today.month == 2 and today.month != tomorrow.month or today.day == 30
