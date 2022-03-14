import os

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

@bot.command(name='add', help='Add available times')
async def add_time(ctx, day, time):
    response = 'Added timing'
    await ctx.send(response)

@bot.command(name='delete', help='Delete specific available times')
async def add_time(ctx, day, time):
    response = 'Deleted timing'
    await ctx.send(response)	

@bot.command(name='show', help='Show user\'s available times')
async def add_time(ctx):
    response = 'todo: show available time'
    await ctx.send(response)

@bot.command(name='availi', help='Show available times')
async def add_time(ctx):
    response = 'todo: show available time'
    await ctx.send(response)


bot.run(TOKEN)
