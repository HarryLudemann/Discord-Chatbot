# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
    # Permission Checkers
    # chat command
    def check_ping_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('basic-ping', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True

    #Commands
    # Help Command
    @commands.command()
    async def help(self, ctx):
        await ctx.send(''' ```
Hazzahs Discord Bot

Basic:
  help                Shows this message
  ping                Ping Bot

Fun:
  cat                 Returns Random Cat
  dog                 Returns Random Dog
  comeback {Target}   Returns Random Comeback
  inspire             Returns Inspirational Quote

Ai_Chat_Bot:
  chat                Talk To Chat Bot
  train               Add Responses To AI Model
  addquestion         Add Question To Intents
  intents             List All Intents
       ``` ''')

    # Ping Commands
    @commands.command(name='ping', help='Test Bot Is Active')
    @commands.check(check_ping_permission)
    async def ping(self, ctx):
        await ctx.send('Pong')

    # Get Current Server Info
    @commands.command(name='info', help='Server Info', pass_context = True)
    async def info(self, gui):
      await ctx.send(f'{ctx.author.name}, you are currently in {ctx.guild.name} ({ctx.guild.id}).')


def setup(client):
    client.add_cog(Basic(client))
