from datetime import date

from annoying.functions import get_object_or_None
from discord import User
from django.db.models import Q

from mydjangobot.models import Debt, DiscordUser


def insert_new_user(discord_user: User):

    db_user = DiscordUser(
        discord_id=discord_user.id,
        username=discord_user.name,
        discriminator=discord_user.discriminator
    )
    db_user.save()

    return db_user


def update_and_get_discord_user(discord_user: User):

    db_user = get_object_or_None(DiscordUser, discord_id=discord_user.id)

    if db_user is None:
        db_user = insert_new_user(discord_user)

    else:
        db_user.username = discord_user.name
        db_user.discriminator = discord_user.discriminator
        db_user.save()

    return db_user


def get_unpaid_debts_for_user(discord_user: User):

    db_user = get_object_or_None(DiscordUser, discord_id=discord_user.id)

    if db_user is None:
        return None

    return Debt.objects.filter(Q(paid_date=None) & Q(debtor__discord_id=discord_user.id) | Q(indebted__discord_id=discord_user.id))


def set_paid_debt(debt_id):

    debt: Debt = get_object_or_None(Debt, id=debt_id)

    if debt is None:
        return False

    debt.paid_date = date.today()
    debt.save()
    return True
