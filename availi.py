import os
import discord
from datetime import datetime
from discord.ext import commands
from private.config import TOKEN

# All bot commands starts with the '!' prefix
bot = commands.Bot(command_prefix='!')

# List of all users
userList = []

# AvailiUser class to store the details of each individual user
class AvailiUser:
    def __init__(self, userID, available):
        self.userID = userID
        self.availableList = [available]

    def addAvailability(self, available):
        # Append new available time into list
        self.availableList.append(available)

# Gets the current index of the current user from the userList
def getUserIndex(userID):
    # Loop through userList to find the index of the current user
    for user in userList:
        index = 0
        # If userID matches current user, break out of loop
        if(user.userID == userID):
            break
        # Increment index if userID has not been found yet
        index += 1

    return index

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

# !add Command
@bot.command(name='add', help='Add available times using the format: \'dd mm yyyy hh min\'')
async def add_time(ctx, day: int, month: int, year: int, hour: int, minute: int):
    # Get current user's ID
    userID = ctx.author.id

    # Create datetime object
    availableTime = datetime(year, month, day, hour, minute)

    # If userList is not empty
    if not(len(userList) == 0):
        # Find existing user
        #If userID in userList.userID:
        if any(user.userID == userID for user in userList):

            # Get the index of current user in userList
            index = getUserIndex(userID)

            # Add available time to the user's object
            userList[index].addAvailability(availableTime)

    # Either userList is empty or user does not exist            
    else:
        # Create new user and add to the userList
        user = AvailiUser(userID, availableTime)
        userList.append(user)

    # Print to user that their timing has been added
    response = 'Added timing: ' + availableTime.strftime("%d %B %Y  %H:%M") + ' UserID: ' + str(userID)
    await ctx.send(response)

# !delete Command
@bot.command(name='delete', help='Delete specific available times')
async def add_time(ctx, day, time):
    response = 'Deleted timing'
    await ctx.send(response)	

# !show Command
@bot.command(name='show', help='Show user\'s available times')
async def add_time(ctx):
    response = 'todo: show available time'
    await ctx.send(response)

# !availi Command
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
