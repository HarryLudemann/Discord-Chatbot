# Import Modules
import discord
from discord.ext import commands
import os
from decouple import config #Get .env Varible
# Custom Modules
import functions

bot = commands.Bot(command_prefix='$', case_insensitive=True)
DiscordBotToken = config('DiscordBotToken')

# Returns Inspirational Qoute
@bot.command(name='inspire', help='Returns Inspirational Quote')
async def inspire(ctx):
    quote = functions.get_quote()
    await ctx.send(quote)

# Asks Ai Questions
@bot.command(name='chat', help='Talk To Chat Bot')
async def chat(ctx, *message):
    response = functions.chatbot.chatbot_response(' '.join(message))
    await ctx.send(response)

# After Bot is successfully connected, prints this message to console
@bot.event
async def on_ready():
  print('We have logged in as {0.user}'.format(bot))

# When a new member joins, private messages them this
@bot.event
async def on_member_join(member):
  await member.create_dm()
  await member.dm_channel.send( f'Hi {member.name}, welcome to my Discord server!' )


bot.run(DiscordBotToken)