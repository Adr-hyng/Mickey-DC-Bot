# Main Source (Credentials <-- Ticker)

from discord import app_commands, Client, Intents
from os import getenv as os_environ
from dotenv import load_dotenv
from enum import Enum


load_dotenv()

class Credentials(Enum):
    TOKEN = os_environ("DISCORD_TOKEN")
    GUILD_ID = int(os_environ("GUILD_ID"))

class Channel(Enum):
    BOT_TESTING = int(os_environ("C_BOT_TESTING"))
    STATISTICS = int(os_environ("C_STATISTICS"))
    ONLINE = int(os_environ("C_ONLINE"))
    
class DiscordBot(Enum):
    client = Client(intents=Intents.all())
    tree = app_commands.CommandTree(client)

