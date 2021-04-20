# Import Modules
import discord
from discord.ext import commands
# Custom Modules
import functions #shows error dont remove / discord.py initializes this file apart of main bot.py, so imports are acting from bot.py

class Ai_Chat_Bot(commands.Cog):
    def __init__(self, client):
        self.client = client

    #Commands
    # Asks Ai Questions
    @commands.command(name='chat', help='Talk To Chat Bot')
    async def chat(self, ctx, *message):
        response = functions.chatbot.chatbot_response(' '.join(message))
        await ctx.send(response)

def setup(client):
    client.add_cog(Ai_Chat_Bot(client))