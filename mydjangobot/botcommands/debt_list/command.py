import random

from asgiref.sync import sync_to_async
from discord import Embed, Interaction
from django.db.models.query import QuerySet

from mydjangobot.data_functions import (get_unpaid_debts_for_user,
                                        update_and_get_discord_user)
from mydjangobot.funny_data import INSULTS, get_plural


async def run(interaction: Interaction):
    await sync_to_async(update_and_get_discord_user)(interaction.user)
    debts = await sync_to_async(get_unpaid_debts_for_user)(interaction.user)
    embed = await sync_to_async(generate_embed)(interaction, debts)
    await interaction.response.send_message(embed=embed)


def generate_embed(interaction: Interaction, debts: QuerySet):
    embed = Embed(type='rich')

    you_owe_string = ""
    you_are_owed_string = ""
    owe_or_owed = False

    for d in debts.order_by('debtor'):
        if d.debtor.discord_id == interaction.user.id:
            you_are_owed_string += f"Debt {d.id}: {d}\n"
        else:
            you_owe_string += f"Debt {d.id}: {d}\n"

    if you_are_owed_string != "":
        embed.add_field(name="Te deben:",
                        value=you_are_owed_string, inline=False)
        owe_or_owed = True

    if you_owe_string != "":
        embed.add_field(name="Debes:", value=you_owe_string, inline=False)
        owe_or_owed = True

    if owe_or_owed:
        embed.set_footer(
            text=f"Pagad {get_plural(random.choice(INSULTS)).lower()}",
            icon_url="https://cdn.discordapp.com/emojis/815528166721585163.webp?size=60")
    else:
        embed.description = "No tienes deudas máquina."

    return embed
