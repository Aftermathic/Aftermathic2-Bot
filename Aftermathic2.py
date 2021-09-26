#Libraries
import discord
import os
import requests
import random
import json

#24/7 thing
from webserver import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

random_gameideas = [
    "where you fight aliens that are trying to take over earth!",
    
    "where you change gravity to pass really difficult levels!",

    "where you can freely explore, bulid, destroy things, and play with other friends without any punishments!",

    "where you try to get a better job to get money so you have a home and food in a ongoing pandemic! (No, I'm not talking about COVID-19.)",

    "where you must answer hard math questions while avoiding a math teacher!",

    "where you explore a abandoned school to get a cheat sheet for your exam, while avoiding zombies and ghouls.",

    "where you deliver pizzas, get money from it, and then upgrade your restaurant to get more money!",

    "where you try to keep zombie pizzas from getting delivered to people!",

    "where you can fight against custom bosses by uploading your own 3D Object files and adding your own attacks!",

    "where you can explore space, find some aliens, and play fun minigames!",

    "where you create a living being that evolves into many forms after a certain period of time, or when your creation learns something new!",

    "where you must avoid monsters that appear due to a epidemic. (This idea came from the Netflix TV Show 'Sweet Home')",

    "where you can fight against zombies with your friends.",

    "where you have to create potions to cure people, if they don't get cured, they will try to murder you!",

    "where you are deserted on a island, with a shark that's trying to kill you and materials that can help you make a raft to find land."
]

random_genres = [
    "horror",
    "RPG",
    "adventure",
    "difficult",
    "unusual",
    "fighting",
    "violent",
    "epic",
    "block",
    "science"
]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='your commands.'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
        
    if message.content.startswith('$help'):
        await message.channel.send('Prefix: $\n\nCommands:\n$help - Description: I will tell you all of the commands and show you what I can do!\n\n$about - Description: I will tell you all about me!\n\n$ping - Description: When the command is used, I will reply "Pong!" back to you.\n\n$inspire - Description: I will find a inspiring quote to read to you, hopefully inspiring you, hence the command name.\n\n$gameidea - Description: I will tell you a good game idea if you feel like making a game, or trying to learn how to code!\n\nOther Stuff:\n I will greet someone when they type "hello".')

    if message.content.startswith('$ping'):
        await message.channel.send('Pong!')

    if message.content.startswith('hello'):
        await message.channel.send('Hello! I am Aftermathic2! If you want to use me my prefix is $.')

    if message.content.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith('$gameidea'):
        await message.channel.send('A ' + random.choice(random_genres) + ' game ' + random.choice(random_gameideas))

    if message.content.startswith('$about'):
        await message.channel.send("I was created by Aftermathic#8216. He used the programming language: Python.\n\n A while ago, I was created with JavaScript, but since the main coder of the bot, StormyRaptor started to become inactive, Aftermathic attempted to recreate me in Java, C#, and JavaScript, but it didn't work.\n\nSo then he tried using Python, and it worked! So now you know how I'm alive!")

keep_alive() #keep bot alive

#get token from discord developer portal
client.run('put the bot token in here')
