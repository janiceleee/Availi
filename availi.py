import os

import discord
from discord.ext import commands

TOKEN = 'OTUyODMxMjk3NTczNzY5MjM2.Yi7vTA.OZnBwjovLtQrzxZOW7EN6wW68nw'

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@bot.command(name='add', help='Add available time')
async def add_time(ctx, day, time):
    response = 'Added timing'
    await ctx.send(response)

	

bot.run(TOKEN)
