import discord
from datetime import datetime
import time

from command_handler import client, channel, credentials, tree, guild_tick  # Main --> Command Handler


@client.event
async def on_ready():
  await tree.sync(guild=discord.Object(id=credentials.GUILD_ID.value))
  await client.change_presence(activity=discord.Game(name="with your mom!"))
  today_time = f"{time.strftime('%I:%M %p')} at {datetime.today().strftime('%B %d, %Y')}"
  await client.get_channel(channel.BOT_TESTING.value
                           ).send(f"Just logged in: {today_time}")
  guild_tick.start()


@client.event
async def on_message(message):
  if message.author == client.user: return

  if message.content == "-test_bot":
    await client.get_channel(channel.BOT_TESTING.value).send("Bot Working")


#python discord bot code above ^^
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return "Bot up and running"


if __name__ == "__main__":
  client.run(credentials.TOKEN.value)
  app.run(host="0.0.0.0", debug=True, port=8080)
