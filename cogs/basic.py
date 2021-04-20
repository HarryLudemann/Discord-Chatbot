# Import Modules
import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

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
  chat     Talk To Chat Bot
       ``` ''')

    # Ping Commands
    @commands.command(name='ping', help='Test Bot Is Active')
    async def ping(self, ctx):
        await ctx.send('Pong')

        
    #Events
    # On Bot Successfully Connected
    @commands.Cog.listener()
    async def on_ready(self):
        print('We have logged in as {0.user}'.format(self.client))

    # On Member Join
    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send( f'Hi {member.name}, welcome to my Discord server!' )


def setup(client):
    client.add_cog(Basic(client))
