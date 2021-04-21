# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    # Admin Command Stop Bot
    @commands.command(name='q', help='Stop Bot')
    @commands.has_any_role(functions.GetConfigValue('admin-quit', 'PRIVILEGES'))
    async def q(self, ctx):
        await exit()


def setup(client):
    client.add_cog(Basic(client))
