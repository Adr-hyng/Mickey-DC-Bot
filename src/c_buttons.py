from discord.ui import (button, 
                        View as W_View,
                        Button as W_Button)
from discord import (ButtonStyle,
                     Interaction) 

from c_enums import MAIN_PAGE # C Buttons ---> C Enums

class DesignedButtons(W_View):
  @button(label="📑 THE RULES  📑", style=ButtonStyle.primary)
  async def rules(self, interaction: Interaction, button: W_Button):
    await interaction.response.pong()
    
  @button(label="📘 GUIDELINES 📘",style=ButtonStyle.primary)
  async def guide(self, interaction: Interaction, button: W_Button):
    button.url = "https://discord.com/channels/1044527863740768306/1044536390299430942/1046780875062378536"
  
  @button(label="🚀 GETTING STARTED 🚀",style=ButtonStyle.success)
  async def get_started(self, interaction: Interaction, button: W_Button):
    button.url = "https://discord.com/channels/1044527863740768306/1044528861922197536"
  
  
class LinkButtons(W_View):
  def __init__(self):
      super().__init__()
      component_buttons = [
          W_Button(label='🚀 GO BACK 🚀', style=ButtonStyle.success, url=MAIN_PAGE.main_page.value)
      ]
      for c_button in component_buttons:
          self.add_item(c_button)