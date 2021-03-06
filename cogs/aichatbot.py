# Import Modules
import discord
from discord.ext import commands
import json
import random
import asyncio
# Custom Modules
import functions #shows error dont remove / discord.py initializes this file apart of main bot.py, so imports are acting from bot.py

class Ai_Chat_Bot(commands.Cog):
    def __init__(self, client):
        self.client = client

    # Permission Checkers
    # chat command
    def check_chat_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('chatbot-chat', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True
    # ask command
    def check_ask_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('chatbot-train', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True
    # addquestion command
    def check_addquestion_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('chatbot-addquestion', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True
    # listintents command
    def check_listintents_permission(ctx): #Shows Error / Dont Remove
        role = discord.utils.get(ctx.guild.roles, name=str(functions.GetConfigValue('chatbot-listintents', str(ctx.guild.id))))
        if role in ctx.author.roles:
            return True


    #Commands
    # Asks Ai Questions
    @commands.command(name='chat', help='Talk To Chat Bot')
    @commands.check(check_chat_permission)
    async def chat(self, ctx, *message):
        response = functions.chatbot.chatbot_response(' '.join(message))
        await ctx.send(response)

    # Asks every questions and stores responses
    @commands.command(name='train', help='Train Bot By Answering Questions')
    @commands.check(check_ask_permission)
    async def train(self, ctx):
        await ctx.send('Reply to Questions:') 
        # Get Intents
        with open('./functions/chatbot/resources/intents.json') as json_file:
            data = json.load(json_file)
        # Initilzie new json object
        newdata = {}
        newdata['intents'] = []
        for i in data['intents']:
            # Get Current Infomation
            tag = i['tag']
            questions = i['patterns']
            responses = i['responses']
            context_set = i['context_set']
            # Get New Repsonse
            # Ask Questions
            embed = discord.Embed( title=str(random.choice(questions)))
            await ctx.send(embed=embed) 
            #Get response
            try:
                msg = await self.client.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
                if msg: 
                    #Append to responses
                    responses.append(msg.content)
                    # Append New Object
                    newdata['intents'].append({
                        "tag": tag,
                        "patterns": questions,
                        "responses": responses,
                        "context_set": context_set
                    })
                    #await ctx.send(msg.content)
            except asyncio.TimeoutError:
                await ctx.send("Cancelling due to timeout", delete_after=10)
        with open("./functions/chatbot/resources/intents.json",'w') as f:
            json.dump(newdata, f, indent=4)
        print('Added Training Data')
        await ctx.send('Added Training Data') 

    # Add Question
    @commands.command(name='addquestion', help='Add Question To Bot')
    @commands.check(check_addquestion_permission)
    async def addquestion(self, ctx):
        tag = ''
        question = ''
        response = ''
        # Get Tag
        await ctx.send('Tag: ') 
        #Get response
        try:
            msg = await self.client.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
            if msg: tag = msg.content
                #await ctx.send(msg.content)
        except asyncio.TimeoutError:
            await ctx.send("Cancelling due to timeout", delete_after=10)

        # Get Question
        await ctx.send('Question: ') 
        #Get response
        try:
            msg = await self.client.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
            if msg: question = msg.content
                #await ctx.send(msg.content)
        except asyncio.TimeoutError:
            await ctx.send("Cancelling due to timeout", delete_after=10)

        # Get Response
        await ctx.send('Response: ') 
        #Get response
        try:
            msg = await self.client.wait_for("message", timeout=60, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
            if msg: response = msg.content
                #await ctx.send(msg.content)
        except asyncio.TimeoutError:
            await ctx.send("Cancelling due to timeout", delete_after=10)

        # Get Intents
        with open('./functions/chatbot/resources/intents.json') as json_file:
            data = json.load(json_file)

        # Check if tag is duplicate
        duplicate = False
        for i in data['intents']:
            if i['tag'] == tag:
                duplicate = True

        if duplicate:
            await ctx.send('```Failed: Duplicate Tag Retry```') 
        else:
            # Create Object
            data['intents'].append({
                "tag": tag,
                "patterns": question,
                "responses": response,
                "context_set": ''
            })
            with open("./functions/chatbot/resources/intents.json",'w') as f:
                json.dump(data, f, indent=4)
            await ctx.send('Added To Intents') 
            
    # List Current Intents
    @commands.command(name='intents', help='Add Question To Bot')
    @commands.check(check_listintents_permission)
    async def intents(self, ctx):
        # Get Intents
        with open('./functions/chatbot/resources/intents.json') as json_file:
            data = json.load(json_file)

        for i in data['intents']:
            embed = discord.Embed( title=str('Tag: ' + str(i['tag']) + ' Question/s: ' + str(i['patterns']) + ' Response/s: ' + str(i['responses'])))
            await ctx.send(embed=embed) 

def setup(client):
    client.add_cog(Ai_Chat_Bot(client))