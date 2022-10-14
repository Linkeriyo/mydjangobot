import datetime


async def run(message, params):
    ping = datetime.datetime.utcnow() - message.created_at.replace(tzinfo=None)
    await message.reply(f'{int(ping.microseconds / 1000)}ms')