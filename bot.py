import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os
import time

client = discord.Client()
bot = commands.Bot(command_prefix = ":banana:")

calls = {}

@bot.listen()
async def on_ready():
    print("on")
    print(bot.user.name + "#" + str(bot.user.discriminator))

@bot.listen()
async def on_message(message):
        if message.channel.name.endswith("📠🐒"):
            global calls
            guild_id = message.channel.guild.id
            channel = None
            if not guild_id in calls:
                for ch in message.guild.text_channels:
                    if ch.topic.endswith(bot.user.mention):
                        channel = ch
                for ch in message.guild.voice_channels:
                    if ch.name.endswith("📞"):
                        calls[guild_id] = ch.id
                contents = ["- "," -"]
                delete = await channel.send("call in «" + message.channel.guild.name.replace("«","�").replace("»","�") + "»")
                await delete.delete()
                await channel.send(contents[-1])
                current_time = time.time()
                next_time = current_time+5
                while current_time < next_time:
                    current_time = time.time()
                    if not current_time < next_time:
                        for content in contents:
                            delete = await channel.send(content)
                            await delete.delete()
                current_time = time.time()
                next_time = current_time+30
                while guild.id in calls:
                    current_time = time.time()
                    if current.time > next_time:
                        next_time = current_time+30
                        call_state = message.channel.guild.get_channel(calls[guild_id])
                        if call_state == None:
                           calls.pop(guild_id)
                        else:
                            if call_state.members == 0:
                                calls.pop(guild_id)

TOKEN = os.environ['BOT_TOKEN']
bot.run(TOKEN)
