from mydjangobot.botcommands.wake import wol


async def run(message, params):
    try:
        if not message.author.id == 154268434090164226:
            await message.reply("quién eres?")
            return

        if not params[0]:
            await message.reply("¿QUÉ?")
            return

        if wol.wake(params[0]):
            await message.reply("enviado")
        else:
            await message.reply("no tengo deso")
    except:
        await message.reply("¿QUÉ?")
