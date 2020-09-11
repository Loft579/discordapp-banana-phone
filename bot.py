import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time

client = discord.Client()
bot = commands.Bot(command_prefix = "'")

current_channel = None

@bot.listen()
async def on_ready():
    print("on")

@bot.listen()
async def on_voice_state_update(member, before, after):
    global current_channel
    channel = after.channel
    if channel == None:
        channel = current_channel.guild.get_channel(current_channel.id)
    if channel != None:
        if len(channel.members) == 1:
            if channel.name.endswith("☎"):
                current_channel = channel
                await channel.edit(name=channel.name.replace("☎","📞↗"))
                invite = await channel.create_invite(temporary=True)
                memberlist = None
                for th in channel.overwrites.items():
                    if th[1].pair()[0].connect:
                        memberlist = th[0]
                if type(memberlist) == discord.role.Role:
                    memberlist == memberlist.members
                if type(memberlist) == discord.member.Member:
                    memberlist == [memberlist]
                for mmr in memberlist:
                    try:
                        await mmr.send(channel.name)
                        await mmr.send(invite.url)
                        await asyncio.sleep(1)
                        await mmr.send(channel.members[0].name)
                        await mmr.send(invite.url)
                await asyncio.sleep(20)
                await channel.edit(name=channel.name.replace("📞↗","📞"))
            if channel.name.endswith("📞"):
                await channel.edit(name=channel.name.replace("📞","☎"))
                await channel.clone()
                await channel.delete()

TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)
