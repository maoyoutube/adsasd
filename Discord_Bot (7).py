import discord
import asyncio
import datetime
import os
from discord.ext import commands
import random
import tasks
import pytz
from itertools import cycle
client = discord.Client()
guild_list = client.guilds
now = datetime.datetime.now()
time = f"{str(now.year)}년 {str(now.month)}월 {str(now.day)}일 {str(now.hour)}시 {str(now.minute)}분 {str(now.second)}초"

@client.event
async def on_message(message):
    
    

    if message.content == "미니 호스팅":
       await message.channel.send("DM 으로 보냄")
       await message.author.create_dm()
       await message.author.send("미니 님은 호스팅. `지인용 마오 디스코드 봇 호스팅`")
token = os.environ["BOT_TOKEN"]
client.run(token)
