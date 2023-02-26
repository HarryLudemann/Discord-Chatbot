# Discord-Chatbot
Bot allows muiltple servers with customizable permissions using python 3.9.4 and is heroku ready. The dependencies are 80mb to large to fit slug size of free heroku tier as TensorFlow, Keras and nltk for a the chat bot is to large.

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

## Setup:
###### **Pip**:
```
python3 -m venv env
source env/bin/activate
pip install -r piprequirements.txt
```

##### Create .env File:
Create a .env file in the main directory, add your discord bots token. eg.
```
DISCORD_BOT_TOKEN="YFak34Y8Ya9GhML8jbtf4RsQ4Gifs.BeebX7Y5RJlv3cV6jasSzParbZiiL0x9Qj"
```

## Customization:
Currently to change permissions you use the config .ini, each section is titled with the server id. Each command has what the command does and the current role that has permissions to use it, by default most commands are set to @everyone except admin commands which are set to @Admin
