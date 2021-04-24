# Simple Discord-Bot
This bot uses TensorFlow, Keras and nltk for the ai chat bot and is accessable in discord through a set off commands, although to train to bot you must run the train.py script in functions/chatbot/train.py. This bot allows muiltple servers to be connected, customizable permissions for all commands and is in python 3.8.2 to support most hosting website like repl.it.

## **Features:**
1.  **Basic**
  	* Ping - Ping Bot
2.  **Fun**
  	* Cat - Return Random Cat Picture
  	* Dog - Return Random Dog Picture
  	* Comeback {TargetUser} - Return Random Comeback
  	* Inspire - Return Inspirational Qoute
3.  **Ai ChatBot**
    * Chat {Message} - Send Ai Message
	* Train - Add Responses To All Excisting Questions
	* Addquestion - Add To Intents
	* Intents - List All Intents
4.  **Uncategorised**
  	* New Member Welcome Message
5.  **Admin**
  	* Q - Stop Bot

## Install Dependencies:
###### **Pip**:
```
python3 -m venv env
source env/bin/activate
pip install -r piprequirements.txt
```
###### **Conda**:
```
conda create --name <env> --file condarequirements.txt
```

## Create .env:
Create a .env file in the main directory, add your discord bots token. eg.
```
DiscordBotToken="Y4Y8Ya9GhML8jbtf4RsQ4Gifs.BeebX7Y5RJlv3cV6jasSzParbZiiL0x9Qj"
```

## Initial Setup
Have bot.py running while you invite the bot to your server/s the first time you connect