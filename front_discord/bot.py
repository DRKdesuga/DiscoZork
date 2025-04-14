# front_discord/bot.py

from discord.ext import commands
from discord import Intents
from front_discord.config import BOT_TOKEN, COMMAND_PREFIX
from front_discord.utils.utilities import utils
from front_discord.src.zork import zork

intents = Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix=COMMAND_PREFIX, intents=intents, help_command=None)

@bot.event
async def on_ready():
    print(f"{bot.user} est en ligne et prêt !")

utils(bot) 
zork(bot)

bot.run(BOT_TOKEN)
