import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'OTUyODMxMjk3NTczNzY5MjM2.Yi7vTA.OZnBwjovLtQrzxZOW7EN6wW68nw'

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
	
client.run(TOKEN)
