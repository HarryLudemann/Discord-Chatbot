# Import Modules
import os # for loading cog files
import discord
from discord.ext import commands
from decouple import config #Get .env Varible
# Custom Modules
import functions

# Bots Description
description = "Hazzahs Discord Bot"
# Initialize client
client = commands.Bot(command_prefix=functions.GetConfigValue('identifier', 'MAIN'), case_insensitive=True, description=description, help_command=None)
# Get Discord Token From .env file
DiscordBotToken = config('DiscordBotToken')
# Load All Categorys in cogs folder
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
# Run Bot
client.run(DiscordBotToken)