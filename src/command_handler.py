from discord import Interaction as D_Interaction
from discord import Object as D_Object
from discord import app_commands
from ticker import client, channel, credentials, tree, guild_tick # Command Handler --> Ticker


@tree.command(name = "add", description = "Add two numbers", guild = D_Object(id = credentials.GUILD_ID.value))
@app_commands.describe(num1 = "First Number", num2 = "Second Number")
async def add(interaction: D_Interaction, num1: int, num2: int):
    await interaction.response.send_message(f"{num1} + {num2} = {num1 + num2}")
    interaction.response