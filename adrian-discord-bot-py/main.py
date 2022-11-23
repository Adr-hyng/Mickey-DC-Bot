import discord
from discord.ext import tasks
from datetime import datetime
import time
from os import getenv as os_environ
from dotenv import load_dotenv


load_dotenv()

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "with your mom!"))
    today_time = f"{time.strftime('%I:%M %p')} at {datetime.today().strftime('%B %d, %Y')}"
    await client.get_channel(1044645380408737793).send(f"Just logged in: {today_time}")
    guild_tick.start()
    
@client.event
async def on_message(message):
    if message.author == client.user: return
    
    if message.content == "/a-test":
        await client.get_channel(1044645380408737793).send("Bot Working")
        

@tasks.loop(seconds=5)
async def guild_tick():
    total_members = len(client.users)
    online_members = len([member for member in client.get_all_members() if member.status == discord.Status.online])
    await client.get_channel(1044987292655304764).edit(name = f"📊STATISTICS: {total_members}")
    await client.get_channel(1045066203690971186).edit(name = f"Online: {online_members}")
    
@guild_tick.before_loop
async def before():
    await client.wait_until_ready()

def main():
    client.run(os_environ("DISCORD_TOKEN"))


if __name__ == "__main__":
    main()