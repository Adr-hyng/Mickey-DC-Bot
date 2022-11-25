 # Command Handler --> Ticker

from discord import Interaction as D_Interaction
from discord import Object as D_Object
from discord import app_commands

from c_enums import SLASHCOMMANDS
from ticker import (
                    client, 
                    channel, 
                    credentials, 
                    tree, 
                    guild_tick
                    )
from typing import Union

# Nothing to see here, just an good ol add() for testing.
@tree.command(name = "add", description = "Add two numbers", guild = D_Object(id = credentials.GUILD_ID.value))
@app_commands.describe(num1 = "First Number", num2 = "Second Number")
async def add(interaction: D_Interaction, num1: int, num2: int):
    await interaction.response.send_message(f"{num1} + {num2} = {num1 + num2}")
    


class SlashCommandListener:
    def __init__(self, interaction: D_Interaction, **kwargs):
        self.interaction = interaction
        self._command = kwargs.get("execute")
        self._arg = kwargs.get("arg")
        
    async def run(self):
        if self._command == "shoutout":
            await self._shoutout(self._arg)
        if self._command == "test":
            await self._test()
        return


    #! ADD COMMAND METHODS HERE
    async def _shoutout(self, arg: str = ""):
        return await self.interaction.response.send_message(f"{self.interaction.user.name} says {arg}")
        
    async def _test(self):
        return await self.interaction.response.send_message(f"Test Working")        
        


# /icpep command shoutout argument 
@tree.command(name = "icpep", description = "ICPEP Command List", guild = D_Object(id = credentials.GUILD_ID.value))
@app_commands.describe(execute = "What kind of command to execute?", arg = "Additional Argument")
async def commands(interaction: D_Interaction, execute: SLASHCOMMANDS, arg: str = None):
    slash_command = SlashCommandListener(interaction=interaction, execute=execute.name, arg=arg)
    await slash_command.run()