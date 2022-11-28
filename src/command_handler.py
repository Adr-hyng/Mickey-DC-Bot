# Command Handler --> Ticker

from discord import Interaction as D_Interaction
from discord import Object as D_Object
from discord import app_commands

import discord

from ticker import (client, channel, credentials, tree, guild_tick)
from typing import (Union)

# /icpep shoutout text: str
@tree.command(name="icpep-shoutout", description="Gives you a shoutout.", guild=D_Object(id=credentials.GUILD_ID.value), auto_locale_strings=True)
@app_commands.describe(text="What text to say?")
async def shoutout(interaction: D_Interaction, text: str = ""):
    return await interaction.response.send_message(f"{interaction.user.name} says {text}")
  
# /icpep test
@tree.command(name=f"icpep-test", description="testing the Discord Bot.", guild=D_Object(id=credentials.GUILD_ID.value))
async def shoutout(interaction: D_Interaction):
    return await interaction.response.send_message(f"I am working, master!")
