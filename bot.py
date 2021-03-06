# Import Modules
import os # for loading cog files
import discord
from discord.ext import commands
from discord.utils import get
from decouple import config
# Custom Modules
import functions

def get_prefix(client, message):
  return functions.GetConfigValue('identifier', str(message.guild.id))

# Bots Description
description = "Hazzahs Bot"
# Initialize client
client = commands.Bot(command_prefix= get_prefix, case_insensitive=True, description=description, help_command=None)
# Get Discord Token From .env file
# token = str(os.getenv("DiscordBotToken"))

# Load All Categorys in cogs folder
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
#Get Discord Token From .envpip
token = config("DISCORD_BOT_TOKEN")
# Run Bot
client.run(token)