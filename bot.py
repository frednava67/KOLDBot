# bot.py
import os
import discord
import requests
import json
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
my_bot_id = os.getenv('BOTid')

client = discord.Client()

def get_luke():
  response = requests.get("https://swapi.dev/api/people/1/")
  json_data = json.loads(response.text)
  rname = json_data['name']
  return(rname)

@client.event
async def on_ready():
  print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):

  print(message)
  print(message.content)

  if message.author == client.user:
    return

  if message.content.startswith(my_bot_id + ' help'):
    await message.channel.send('How can I help you?')

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('/luke'):
    cname = get_luke()
    await message.channel.send(cname)

client.run(TOKEN)
