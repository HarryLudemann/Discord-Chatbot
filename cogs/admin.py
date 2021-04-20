# Import Modules
import discord
from discord.ext import commands

class Basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    #Commands
    # Admin Command Stop Bot
    @commands.command(name='q', help='Stop Bot')
    @commands.has_any_role("Admin", "Mod")
    async def q(self, ctx):
        await exit()


def setup(client):
    client.add_cog(Basic(client))
