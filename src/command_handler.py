# Command Handler --> Ticker

from discord import Interaction as D_Interaction
from discord import Object as D_Object
from discord import app_commands

import discord

from ticker import (client, channel, credentials, tree, guild_tick, dota2_match_finder)
from typing import (Union, Literal, Optional)

import json

# /icpep shoutout text: str
@tree.command(name="icpep-shoutout", description="Gives you a shoutout.", guild=D_Object(id=credentials.GUILD_ID.value), auto_locale_strings=True)
@app_commands.describe(text="What text to say?")
async def shoutout(interaction: D_Interaction, text: str = ""):
    return await interaction.response.send_message(f"{interaction.user.name} says {text}")
  
# /icpep test
@tree.command(name=f"icpep-test", description="testing the Discord Bot.", guild=D_Object(id=credentials.GUILD_ID.value))
async def test(interaction: D_Interaction):
    return await interaction.response.send_message(f"I am working, master!")

# /icpep dota2 accept:boolean
@tree.command(name=f"icpep-dota2", description="Fun Dota 2 Commands", guild=D_Object(id=credentials.GUILD_ID.value))
@app_commands.describe(accept="Accept the match or not?", status="Show Dota 2 Database")
async def dota2_accept(interaction: D_Interaction, accept: Optional[bool] = None, status: Optional[Literal["show"]] = None):
    await interaction.response.defer()
    
    if accept is not None:
        # Read Data in Json File
        with open("../status.json") as fr:
            data = dict(json.load(fr))
    
        # Overwrite Auto Accept depending on what user wants
        before_accept = data.get("auto_accept")
        data["auto_accept"] = accept
            
        # Save it
        with open("../status.json", 'w') as fw:
            json.dump(data, fw, indent = 2)
        
        # Feedback
        await interaction.followup.send(f"Update: Auto Accept from {before_accept} to {accept}")
        
    if status is not None:
        # Read Data in Json File
        with open("../status.json") as fr:
            data = dict(json.load(fr))
        
        text = str(data).replace("'", "\"").replace(",", ",\n\t").replace("}", "\n}").replace("{", "{\n\t ").replace("True", "true").replace("False", "false").replace("None", "null")
        
        print(f'Status: \n```json\n{text}\n```')
        
        # Feedback
        await interaction.followup.send(f'Status: \n```json\n{text}\n```')
