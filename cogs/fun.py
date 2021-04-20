# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions #shows error dont remove / discord.py initializes this file apart of main bot.py, so imports are acting from bot.py

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Commands
    # Returns Inspirational Qoute
    @commands.command(name='inspire', help='Returns Inspirational Quote')
    async def inspire(self, ctx):
        quote = functions.get_inspire_quote()
        await ctx.send(quote)

    # Returns Foaas comeback
    @commands.command(name='comeback', help='Returns Foass Comeback')
    async def comeback(self, ctx):
        quote = functions.get_foass(str(ctx.author.name))
        await ctx.send(quote)

def setup(client):
    client.add_cog(Fun(client))