from credentials import Channel, DiscordBot, Credentials  # Ticker --> Credentials
from discord import Status
from discord.ext import tasks

from dota2_command import Dota2

import json
import asyncio
import threading

client = DiscordBot.client.value
tree = DiscordBot.tree.value
channel = Channel
credentials = Credentials


# Get Statistics of the Discord Server
@tasks.loop(seconds=30)
async def guild_tick():
	total_members = len(client.users)
	online_members = len([
	 member for member in client.get_all_members()
	 if member.status == Status.online
	])
	await client.get_channel(channel.STATISTICS.value
	                         ).edit(name=f"📊STATISTICS: {total_members}")
	await client.get_channel(channel.ONLINE.value
	                         ).edit(name=f"Online: {online_members}")

@guild_tick.before_loop
async def before():
	await client.wait_until_ready()
 
 
# Dota 2 Match Run Looper
@tasks.loop(seconds=0.1)
async def dota2_match_finder():
    
    auto_accept_permission = False
    wait_match_permission = False
    with open("../status.json") as f:
        data = dict(json.load(f))
        auto_accept_permission = data.get("auto_accept")
        wait_match_permission = data.get("wait_match")
        curr_match_id = data.get("current_match_id")
    if wait_match_permission:
        handler = Dota2()
        await handler.run()
        if handler.match_found:
            t = threading.Thread(target=handler._speak, args=("A match has been found",), daemon=True)
            t.start()
            await client.get_channel(1046039940540145734).send(f">>> **Dota 2**: Match Found \n**ID**: {curr_match_id}")
            if auto_accept_permission:
                await handler._click_accept()
                handler.engine.endLoop()
            await asyncio.sleep(2)
                

@dota2_match_finder.before_loop
async def before():
	await client.wait_until_ready()

