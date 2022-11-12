import random
from datetime import date

from asgiref.sync import sync_to_async
from discord import Interaction, User

from mydjangobot.data_functions import update_and_get_discord_user
from mydjangobot.funny_data import INSULTS
from mydjangobot.models import Debt


async def run(interaction: Interaction, indebted: User, debtor: User, amount: float, currency: str):

    debtor_django = await sync_to_async(update_and_get_discord_user)(debtor)
    indebted_django = await sync_to_async(update_and_get_discord_user)(indebted)

    debt = Debt(
        debtor=debtor_django,
        indebted=indebted_django,
        amount=amount,
        currency=currency,
        start_date=date.today()
    )

    await sync_to_async(debt.save, thread_sensitive=True)()
    await interaction.response.send_message(f'<@{indebted.id}> paga {random.choice(INSULTS).lower()}, id de la deuda: {debt.id}')
