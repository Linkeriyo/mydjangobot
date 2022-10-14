import random
import re
from datetime import date

import mydjangobot.discordbot_settings as settings
from asgiref.sync import sync_to_async
from mydjangobot.data_functions import update_and_get_discord_user
from mydjangobot.funny_data import INSULTS
from mydjangobot.models import Debt


async def run(message, params):
    clean_message = message.content[len(settings.prefix):]
    match = re.search(
        r'debt add <@([0-9]+)> x <@([0-9]+)> ([0-9\.,]+) ?([A-z]+)', clean_message)
    indebted_id = match.group(1)
    debtor_id = match.group(2)
    amount = match.group(3)

    if amount.__contains__(','):
        amount.replace(',', '.')

    currency = match.group(4)

    debtor_discord_user = None
    for member in message.mentions:
        if str(member.id) == debtor_id:
            debtor_discord_user = member

    indebted_discord_user = None
    for member in message.mentions:
        if str(member.id) == indebted_id:
            indebted_discord_user = member

    if debtor_discord_user is None or indebted_discord_user is None:
        return

    debtor = await sync_to_async(update_and_get_discord_user, thread_sensitive=True)(debtor_discord_user)
    indebted = await sync_to_async(update_and_get_discord_user, thread_sensitive=True)(indebted_discord_user)

    debt = Debt(
        debtor=debtor,
        indebted=indebted,
        amount=amount,
        currency=currency,
        start_date=date.today()
    )

    await sync_to_async(debt.save, thread_sensitive=True)()
    await message.reply(f'<@{indebted_id}> paga {random.choice(INSULTS).lower()}, id de la deuda: {debt.id}')
