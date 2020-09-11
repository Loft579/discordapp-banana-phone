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
        if len(channel.members) <= 1:
            if len(channel.members) == 1:
                if channel.name.endswith("☎"):
                    current_channel = channel
                    await channel.edit(name=channel.name.replace("☎","📞↗"))
                    invite = await channel.create_invite(temporary=True)
                    for rol in member.roles:
                        if "☎" in rol.name:
                            connected = [] 
                            for mmr in channel:
                                connected.append(mmr.id)
                            for mmr in rol.members:
                                if not mmr.id in connected:
                                    try:
                                        await mmr.send(rol.name)
                                        await mmr.send(invite.url)
                                        await asyncio.sleep(1)
                                        await mmr.send(channel.members[0].name)
                                        await mmr.send(invite.url)
                                except:
                                    pass
                    await asyncio.sleep(20)
                    await channel.edit(name=channel.name.replace("📞↗","📞"))
            if channel.name.endswith("📞"):
                await channel.edit(name=channel.name.replace("📞","☎"))
                await channel.clone()
                await channel.delete()

TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)
