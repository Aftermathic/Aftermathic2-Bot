import discord
import os
import requests
import json

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send('Prefix: $\n\nCommands:\n$help - Description: I will tell you all of the commands and show you what I can do!\n\n$ping - Description: When the command is used, I will reply "Pong!" back to you.\n\n$inspire - Description: I will find a inspiring quote to read to you, hopefully inspiring you, hence the command name.\n\nOther Stuff:\n I will greet someone when they type "hello".')

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

    if message.content.startswith('hello'):
        await message.channel.send('Hello! I am Aftermathic2! If you want to use me my prefix is $.')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

client.run('put your own bot token here')
