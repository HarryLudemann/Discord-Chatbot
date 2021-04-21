# Import Discord
import discord
from discord.ext import commands
# Modules For Calling Apis
import requests
import json
import aiohttp
import asyncio
# Official Api Packages
from foaas import fuck
# Custom Modules
import functions

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Commands
    # Returns Inspirational Qoute
    @commands.command(name='inspire', help='Returns Inspirational Quote')
    @commands.has_any_role(functions.GetConfigValue('fun-inspire', 'PRIVILEGES'))
    async def inspire(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(quote)

    # Returns Foaas comeback
    @commands.command(name='comeback', help='Returns Foass Comeback')
    @commands.has_any_role(functions.GetConfigValue('fun-comeback', 'PRIVILEGES'))
    async def comeback(self, ctx, target):
        response = fuck.random(name=target, from_= str(ctx.message.author)).text
        await ctx.send(response)

    @commands.command(pass_context=True)
    @commands.has_any_role(functions.GetConfigValue('fun-cat', 'PRIVILEGES'))
    async def cat(self, ctx):
        """(c) random cat picture"""
        print('cat')
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://aws.random.cat/meow') as r:
                res = await r.json()
                await cs.close()
        embed = discord.Embed(
            title = 'Kitty Cat 🐈',
            description = 'Cats :star_struck:',
            colour = discord.Colour.purple()
            )
        embed.set_image(url=res['file'])     
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_any_role(functions.GetConfigValue('fun-dog', 'PRIVILEGES'))
    async def dog(self, ctx):
        """(d) random dog picture"""
        print('dog')
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://random.dog/woof.json') as r:
                    res = await r.json()
                    res = res['url']
                    await cs.close()
            if res.endswith('.mp4'):
                pass
            else:
                isVideo = False
        embed = discord.Embed(
            title = 'Dogga 🐶',
            description = 'Dogs :star_struck:',
            colour = discord.Colour.purple()
            )
        embed.set_image(url=res)  
        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Fun(client))
