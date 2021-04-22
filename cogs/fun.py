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

    # Permission Checkers
    # chat command
    def check_inspire_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('fun-inspire', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True
    # ask command
    def check_cat_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('fun-cat', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True
    # addquestion command
    def check_dog_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('fun-dog', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True
    # listintents command
    def check_comeback_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('fun-comeback', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True


    # Commands
    # Returns Inspirational Qoute
    @commands.command(name='inspire', help='Returns Inspirational Quote')
    @commands.check(check_inspire_permission)
    async def inspire(self, ctx):
        response = requests.get("https://zenquotes.io/api/random")
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        await ctx.send(quote)

    # Returns Foaas comeback
    @commands.command(name='comeback', help='Returns Foass Comeback')
    @commands.check(check_comeback_permission)
    async def comeback(self, ctx, target):
        response = fuck.random(name=target, from_= str(ctx.message.author)).text
        await ctx.send(response)

    @commands.command(pass_context=True)
    @commands.check(check_cat_permission)
    async def cat(self, ctx):
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
    @commands.check(check_dog_permission)
    async def dog(self, ctx):
        """(d) random dog picture"""
        print('dog')
        isVideo = True
        while isVideo:
            async with aiohttp.ClientSession() as cs:
                async with cs.get('https://dog.ceo/api/breeds/image/random') as r:
                    res = await r.json()
                    res = res['message']
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
