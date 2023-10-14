from requests import get

async def run(message, params):
    ip = get('https://api.ipify.org').content.decode('utf8')
    await message.channel.send(f'IP: {ip}')