from requests import get
from mydjangobot import strings

async def run(message, params):
    if not message.author.id == 154268434090164226:
            await message.reply(strings.not_allowed)
            return
    
    ip = get('https://api.ipify.org').content.decode('utf8')
    await message.channel.send(f'IP: ||{ip}||')