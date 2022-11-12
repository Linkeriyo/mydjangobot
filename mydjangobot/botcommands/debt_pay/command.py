import discord
from asgiref.sync import sync_to_async
from django.db.models.query import QuerySet

from mydjangobot import data_functions


class DebtSelectItem(discord.ui.Select):
    async def callback(self, interaction: discord.Interaction):
        debt_paid = await sync_to_async(data_functions.set_paid_debt)(interaction.data['values'][0])
        if debt_paid:
            response = f"Deuda {interaction.data['values'][0]} pagada."
        else:
            response = "Ha ocurrido un problema."

        await interaction.response.edit_message(content=response, view=None)


async def run(interaction: discord.Interaction):
    debts = await sync_to_async(data_functions.get_unpaid_debts_for_user)(interaction.user)
    options = await sync_to_async(get_select_options_from_debts_queryset)(debts)

    if len(options) == 0:
        await interaction.response.send_message("No tienes deudas.")
        return

    select_menu = DebtSelectItem(
        options=options,
        placeholder="Selecciona una deuda.",
        max_values=1,
        min_values=1
    )

    view = discord.ui.View()
    view.add_item(select_menu)

    await interaction.response.send_message(view=view, ephemeral=True)


def get_select_options_from_debts_queryset(debts: QuerySet):
    options = []

    for d in debts:
        options.append(discord.SelectOption(
            label=f'Deuda {d.id}', description=str(d), value=d.id))

    return options
