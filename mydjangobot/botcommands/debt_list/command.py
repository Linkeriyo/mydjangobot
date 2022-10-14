import random
import mydjangobot.discordbot_settings as settings
from asgiref.sync import sync_to_async
from discord import Embed, Message
from django.db.models.query import QuerySet
from mydjangobot.data_functions import get_unpaid_debts_for_user
from mydjangobot.funny_data import INSULTS, plural


async def run(message, params):
    clean_message = message.content[len(settings.prefix):]

    debts = await sync_to_async(get_unpaid_debts_for_user)(message.author)
    embed = await sync_to_async(generate_embed)(message, debts)
    await message.reply(embed=embed)


def generate_embed(message: Message, debts: QuerySet):
    embed = Embed(type='rich')
    
    you_owe_string = ""
    you_are_owed_string = ""

    for d in debts.order_by('debtor'):
        if d.debtor.discord_id == message.author.id:
            you_are_owed_string += f"Debt {d.id}: {d}\n"
        else:
            you_owe_string += f"Debt {d.id}: {d}\n"

    embed.add_field(name="Te deben:", value=you_are_owed_string, inline=False)
    embed.add_field(name="Debes:", value=you_owe_string, inline=False)
    embed.set_footer(text=f"Pagad {plural(random.choice(INSULTS)).lower()}", icon_url="https://cdn.discordapp.com/emojis/815528166721585163.webp?size=60")
    return embed
