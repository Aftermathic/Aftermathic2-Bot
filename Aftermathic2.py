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

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

    if message.content.startswith('hello'):
        await message.channel.send('Hello! I am Aftermathic2.')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

client.run('put in your own bot token here')
