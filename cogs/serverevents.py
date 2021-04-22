# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client
  
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

    # On Server Join
    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            functions.CreateConfigFile(str(guild.id))
            print(f'Created .ini Infomation For {guild.name}')
        except:
            print(f'{guild.name} Rejoined')



def setup(client):
    client.add_cog(Basic(client))
