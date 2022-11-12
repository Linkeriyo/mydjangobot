from discord import Client, Interaction, User, app_commands

from mydjangobot.botcommands.debt_add import command as debt_add_command
from mydjangobot.botcommands.debt_list import command as debt_list_command
from mydjangobot.botcommands.debt_pay import command as debt_pay_command


async def initialize_commands(client: Client):
    debt_group = app_commands.Group(
        name="debt", description="pay your debts", guild_only=True, guild_ids=[580421667336224769, 668539151037235202])

    await define_commands(debt_group)

    command_tree = app_commands.CommandTree(client)
    command_tree.add_command(debt_group)

    await command_tree.sync()


async def define_commands(debt_group):
    await define_debt_add_command(debt_group)
    await define_debt_list_command(debt_group)
    await define_debt_pay_command(debt_group)


async def define_debt_list_command(debt_group: app_commands.Group):
    @debt_group.command(name="list", description="list your debts")
    async def debt_list(interaction: Interaction):
        await debt_list_command.run(interaction)


async def define_debt_add_command(debt_group: app_commands.Group):
    @debt_group.command(name="add", description="add a debt")
    @app_commands.describe(indebted="the indebted user", debtor="the debtor user", amount="the debted amount", currency="the currency of the debt")
    async def debt_add(interaction: Interaction, indebted: User, debtor: User, amount: float, currency: str):
        await debt_add_command.run(interaction, indebted, debtor, amount, currency)


async def define_debt_pay_command(debt_group: app_commands.Group):
    @debt_group.command(name="pay", description="set one debt as paid")
    async def debt_pay(interaction: Interaction):
        await debt_pay_command.run(interaction)
