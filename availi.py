import os
import discord
from discord.ext import commands

TOKEN = 'OTUyODMxMjk3NTczNzY5MjM2.Yi7vTA.OZnBwjovLtQrzxZOW7EN6wW68nw'

# All bot commands starts with the '!' prefix
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready( ):
    print(f'{bot.user.name} has connected to Discord!')

    # Create an embed message with the !start command when bot joins server
    embed=discord.Embed(
    title="Availi Discord Bot",
        color=discord.Color.blue())
    embed.add_field(name="`!start`", value="Sets up a new Availi channel", inline=False)

    # Retrieves the channel ID of 'general' channel
    channel = discord.utils.get(bot.get_all_channels(), name='bot-spam') # Change this to general
    channel_id = channel.id

    # Send message to 'general' channel 
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

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

# Create a new channel when user inputs !start
@bot.command(name='start', help='Sets up a new Availi-channel')
async def create_channel(ctx):
    guild = ctx.message.guild

    # Creates a new channel called 'availi-channel'
    await guild.create_text_channel('availi-channel')

    # Retrieves the channel ID of recently created 'availi-channel' channel
    channel = discord.utils.get(bot.get_all_channels(), name='availi-channel')
    channel_id = channel.id

    # Create an embed message with the list of commands when new 'availi-channel' is created
    embed=discord.Embed(
    title="Availi Discord Bot",
        color=discord.Color.blue())
    embed.add_field(name="`!add`", value="Add available times", inline=False)
    embed.add_field(name="`!delete`", value="Delete specific available times", inline=False)
    embed.add_field(name="`!show`", value="Show user's available times", inline=False)
    embed.add_field(name="`!availi`", value="Show available times", inline=False)
    embed.add_field(name="`!help`", value="Show a list of commands", inline=False)

    # Send message to 'availi-channel' channel
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

# Starts the bot with the Discord token
bot.run(TOKEN)
