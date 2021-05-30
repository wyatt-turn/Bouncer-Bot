# bot.py
import os

import time

import discord
from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


#prefix = {}
#defaultPrefix = "%"

#roleToRemove = {}
defaultRoleToRemove = "Guest"
defaultDaysToWait = 3

@client.event
async def on_ready():
    print(f'{client.user} has joined')

    """
    while(True):
        for guild in client.guilds:
            print(guild)
        time.sleep(5)
    """
    #time.sleep(5)
    for guild in client.guilds:
            print(guild)
            for member in guild.members:
                if(removeMemberWithRole(member)):
                    print(member.name)  #todo call kick on member


def TimeInDaysSince(date):
    currentDate = datetime.now(timezone.utc).replace(tzinfo=None)
    timeDiff = currentDate - date
    return timeDiff.days


def removeMemberWithRole(member):

    hasRoleFlag = False
    removeFlag = False

    for role in member.roles:
        if(role.name == defaultRoleToRemove):    #TODO: Refactor this in future to use dictionary look up
            hasRoleFlag = True
    
    if(not hasRoleFlag): 
        return False
    
    if(defaultDaysToWait <= TimeInDaysSince(member.joined_at)):
        removeFlag = True
    
    return removeFlag
    

    

#client = CustomClient(discord_client)
client.run(TOKEN)
