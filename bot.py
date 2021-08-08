# bot.py
import os

import time

import discord
from dotenv import load_dotenv
from datetime import datetime, timezone

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


#prefix = {}
#defaultPrefix = "%"

#roleToRemove = {}
defaultRoleToRemove = "Wait List"
defaultDaysToWait = 3

@client.event
async def on_ready():
    print(f'{client.user} has joined')

    #TODO make this properly async for each guild
    for guild in client.guilds:
        print(guild)
        print(guild.id)
        await remove_members_from_guild(guild)
        


async def remove_members_from_guild(guild):
    for member in guild.members:
        if(remove_member_with_role(member)):
            print(f'{member.name} was kicked')
            try:
                await member.kick(reason="Was on wait list for more than 3 days.")
            except:
                print(f'Error kicking {member.name}')


def days_since(date):
    currentDate = datetime.now(timezone.utc)
    timeDiff = currentDate - date
    return timeDiff.days

def remove_member_with_role(member):

    hasRoleFlag = False
    removeFlag = False

    for role in member.roles:
        if(role.name == defaultRoleToRemove):    #TODO: Refactor this in future to use dictionary look up
            hasRoleFlag = True
    
    if(not hasRoleFlag): 
        return False
    
    if(defaultDaysToWait <= days_since(member.joined_at)):
        removeFlag = True
    
    return removeFlag
    

client.run(TOKEN)
