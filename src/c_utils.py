# Storage Room




async def _send_embed(self):
    """
    This converts embed dictionary which is designer in the "discohook.org", then transpiled into embed in code.
    """
    embed = discord.Embed()
    embed_dict = {
    "content": None,
    "embeds": [
      {
        "description": "⚙️ Questions regarding Technology, Advices, Non-related or related to Computer Engineering are valid.\n\n⚙️ Suggestions regarding Improvement, Features, Suggestion, Ideas, and more are highly appreciated.\n\n⚙️ Report is available with the <command /icpep report>, so if you see any annoying or rule-breaking actions, let us know.\n\n⚙️ Information Category is for important formal matters such as Questions, Suggestions, Announcements, Resources, and more.\n\n⚙️ Main Category is for general conversation wherein you can talk about anything, informally or formally. Bot commands is for trying commands from discord bot that is available here. Media for pictures/videos for formality if you want.",
        "color": 3567334,
        "author": {
          "name": "▬▬ ◊ GUIDE ◊ ▬▬",
          "icon_url": "https://png.pngtree.com/element_our/20190530/ourmid/pngtree-correct-icon-image_1267804.jpg"
        },
        "footer": {
          "text": "Moderator/Admin",
          "icon_url": "https://cdn3.emoji.gg/emojis/1503-moderator-badge.png"
        },
        "thumbnail": {
          "url": "https://cdn-icons-png.flaticon.com/512/1705/1705351.png"
        }
      },
      {
        "description": "⚙️ Not all of us are Technical, so, if you don't wanna explain the uncertain one's, for certain reasons, then please just be understanding for those users.\n\n⚙️ Be nice, Be gentle aw.\n\n⚙️ Respect one another. Meow\n\n⚙️ Members are dedicated to BS Computer Engineering ONLY. Visitors have to verify in order to be access channels.\n\n⚙️ We highly value your suggestions, if you have one. \n\n⚙️ No inappropriate topics such as politics, racism, pornographic, NSFW.\n\n⚙️ No spam messages",
        "color": 3567334,
        "author": {
          "name": "▬▬ ◊ RULES ◊ ▬▬",
          "icon_url": "https://png.pngtree.com/element_our/20190530/ourmid/pngtree-correct-icon-image_1267804.jpg"
        },
        "footer": {
          "text": "Moderator/Admin",
          "icon_url": "https://cdn3.emoji.gg/emojis/1503-moderator-badge.png"
        },
        "thumbnail": {
          "url": "https://cdn-icons-png.flaticon.com/512/3211/3211448.png"
        }
      }
    ],
    "username": "Welcome",
    "avatar_url": "https://icpepprofessionalgroup.files.wordpress.com/2017/05/icpep-logo.png",
    "attachments": []
  }
    embeds = [embed.from_dict(embed_dict["embeds"][i]) for i in range(len(embed_dict["embeds"]))]
      # await self.interaction.response.send_message(view=LinkButtons())
    await client.get_channel(channel.OUTPUT.value).send(file=discord.File(r"C:\Users\Adrian\Downloads\COMPUTER_ENGINEERING-removebg-preview.png"), embeds=embeds, view=LinkButtons())