import discord
from datetime import datetime
from discord.ext import commands
from config import TOKEN

# All bot commands starts with the '!' prefix
bot = commands.Bot(command_prefix='!')

# List to store all users
userList = []

# AvailiUser class to store the details of each individual user
class AvailiUser:
    def __init__(self, userID, username, available):
        self.userID = userID
        self.username = username
        self.availableList = [available]

    def addAvailability(self, available):
        # Append new available time into list
        self.availableList.append(available)

# Gets the current index of the current user from the userList
def getUserIndex(userID):
    # Loop through userList to find the index of the current user
    for index in range(len(userList)):
        # If userID matches current user, break out of loop
        if(userList[index].userID == userID):
            return index

# Deletes an available time from an individual user
def deleteAvailableTime(deleteTime, index):
    # Loop through to list to delete time
    for time in userList[index].availableList:
        # If time to delete has been found
        if(deleteTime == time):
            # Remove available timing
            userList[index].availableList.remove(deleteTime)

# Updates available times that has passed for all users
def deletePassedTime():
    now = datetime.now()
    for user in userList:
        for time in user.availableList:
            if time < now:
                user.availableList.remove(time)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    
    # Create an embed message with the !start command when bot joins server
    embed=discord.Embed(
    title="Availi Discord Bot",
        color=discord.Color.red())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="`!start`", value="Sets up a new Availi channel", inline=False)

    # Retrieves the channel ID of 'general' channel
    channel = discord.utils.get(bot.get_all_channels(), name='bot-spam') # Change this to general
    channel_id = channel.id

    # Send message to 'general' channel 
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

# !add Command - Add available time for an individual user
@bot.command(name='add', help='Add available times using the format: \'dd/mm/yyyy hh:mm with only 30 mins intervals\'')
async def add_time(ctx, *, time):
    # Get current user's ID
    userID = ctx.author.id
    success = False
    # Updates all user's avaialable times
    deletePassedTime()

    try: 
        # Format date object from the following format
        formatData = "%d/%m/%Y %H:%M"
        # Create datetime object
        availableTime = datetime.strptime(time, formatData)

        # Check time is in 30 minute intervals
        if not (availableTime.minute == 30 or availableTime.minute == 0):
            response = "Please enter in 30 minute intervals"
            await ctx.send(response)
        else:
            # Find existing user
            if any(user.userID == userID for user in userList):

                # Get the index of current user in userList
                index = getUserIndex(userID)

                # Check if not a duplicate time
                if availableTime not in userList[index].availableList:
                    # Add available time to the user's object
                    userList[index].addAvailability(availableTime)
                    # Added successfully
                    success = True
                else:
                    response = ctx.author.name + ' has added this time before'

            # Else if user does not exist            
            else:
                # Create new user and add to the userList
                user = AvailiUser(userID, ctx.author.name, availableTime)
                userList.append(user)
                # Added successfully
                success = True

            # Print respinse to user when added time is successfull   
            if success:
                # Print to user that their timing has been added
                response = 'Added timing: ' + availableTime.strftime("%d %B %Y  %H:%M")
            
            # Send the response message to the channel
            await ctx.send(response)
    except ValueError:
        # Check time is in valid format
        response = "Please enter a valid time"
        await ctx.send(response)

	

# !delete Command - Delete a specific time from an individual user
@bot.command(name='delete', help='Delete specific available times using the format: \'dd/mm/yyyy hh:mm with only 30 mins intervals\'')
async def delete_time(ctx, *, time):
    # Get current user's ID
    userID = ctx.author.id
    # Updates all user's avaialable times
    deletePassedTime()
    
    try: 
        # Format date object from the following format
        formatData = "%d/%m/%Y %H:%M"
        # Create datetime object
        deleteTime = datetime.strptime(time, formatData)

        # Check time is in 30 minute intervals
        if not (deleteTime.minute == 30 or deleteTime.minute == 0):
            response = "Please enter in 30 minute intervals"
            await ctx.send(response)

        # If userList is not empty
        if not(len(userList) == 0):
            # Find existing user
            if any(user.userID == userID for user in userList):

                # Get the index of current user in userList
                index = getUserIndex(userID)

                # Check if timing exists to delete
                if any(time == deleteTime for time in userList[index].availableList):
                    
                    # Delete the time from the user's availableList
                    deleteAvailableTime(deleteTime, index)

                    # Print out a message to the user that the deletion was successful 
                    response = 'Deleted timing: ' + deleteTime.strftime("%d %B %Y  %H:%M")
                # Else, timing specfied was not found in the available times
                else:
                    # Print out a message to the user that they have not enter that time previously
                    response = ctx.author.name + ' has not input specificed time before'

        # Either userList is empty or user does not exist            
        else:
            # User does not exist in system, no time to delete
            response = ctx.author.name + ' does not have any available timing stored in Availi'

        # Send the response message to the channel
        await ctx.send(response)
    except ValueError:
        response = "Please enter a valid time"
        await ctx.send(response)	

# !show Command - Show all available times for an individual user
@bot.command(name='show', help='Show user\'s available times')
async def show_time(ctx):
    # Get current user's ID
    userID = ctx.author.id
    # Updates all user's avaialable times
    deletePassedTime()

    # If userList is not empty
    if not(len(userList) == 0):
        # Find existing user
        if any(user.userID == userID for user in userList):

            # Get the index of current user in userList
            index = getUserIndex(userID)

            # Check if user has existing available times 
            if not(len(userList[index].availableList) == 0):
                
                # Sort the available timings in the user's available times
                userTimes = sorted(userList[index].availableList)

                # Create a response string to store user's available timings to print 
                response = ctx.author.name +"\'s available timings are:\n"

                # Loop through all available timings from user
                for time in userTimes:
                    response = response + time.strftime("%d %B %Y  %I:%M%p") + '\n'

            # Else, no available times was found for specific user
            else:
                # Print out a message to the user that they have not enter any available times
                response = ctx.author.name + ' does not have any available timings stored in Availi'

    # Either userList is empty or user does not exist            
    else:
        # User does not exist in system, no timings to show
        response = ctx.author.name + ' has not added any available timings in Availi' 

    # Send the response message to the channel
    await ctx.send(response)

# !availi Command - Shows the combined available times for all users
@bot.command(name='availi', help='Show everyone\'s available times')
async def availi(ctx):
    # Updates all user's avaialable times
    deletePassedTime()
	if not(len(userList) == 0):
		# Get a list of all available times list
		times = []
		for user in userList:
			times.append(user.availableList)
		
		# Get a list of all times that intersect
		available = sorted(list(set.intersection(*map(set, times))))

		# Generate response
		response = "Everyone's available time:\n"
		for time in available:
			response = response + time.strftime("%d %B %Y  %I:%M%p") + '\n'
		response = response + "for | "

		for user in userList:
			response = response + user.username + " | "

		await ctx.send(response)



# !start Command - Create a new 'Availi-Channel'
@bot.command(name='start', help='Sets up a new Availi-Channel')
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
        color=discord.Color.red())
    embed.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed.add_field(name="`!add`", value="Add available times", inline=False)
    embed.add_field(name="`!delete`", value="Delete specific available times", inline=False)
    embed.add_field(name="`!show`", value="Show user's available times", inline=False)
    embed.add_field(name="`!availi`", value="Show available times", inline=False)
    embed.add_field(name="`!help`", value="Show a list of commands", inline=False)

    # Send message to 'availi-channel' channel
    channel = bot.get_channel(channel_id)
    await channel.send(embed=embed)

# Error handling when user fails to input a time 
@bot.event
async def on_command_error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.channel.send("Please enter a time")

# Starts the bot with the Discord token
bot.run(TOKEN)
