from credentials import Channel, DiscordBot, Credentials # Ticker --> Credentials
from discord import Status
from discord.ext import tasks

client = DiscordBot.client.value
tree = DiscordBot.tree.value
channel = Channel
credentials = Credentials

@tasks.loop(seconds=5)
async def guild_tick():
    total_members = len(client.users)
    online_members = len([member for member in client.get_all_members() if member.status == Status.online])
    await client.get_channel(channel.STATISTICS.value).edit(name = f"📊STATISTICS: {total_members}")
    await client.get_channel(channel.ONLINE.value).edit(name = f"Online: {online_members}")
    
@guild_tick.before_loop
async def before():
    await client.wait_until_ready()