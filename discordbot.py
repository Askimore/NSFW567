
import discord
import googletrans
import os
import random
import json
import time
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']

client = discord.Client()

gif_words = ["$gif"]

jpg_words = ["$jpg"]

mp4_words = ["$mp4"]

gif = [
  
  
  
]

jpg = [
  

  
]

mp4 = [

  
]

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')
    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.dnd

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="🍆👅💦")
    await client.change_presence(status= status_w, activity=activity_w)


      
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in gif_words):
    gifmsg = await message.channel.send(random.choice(gif))
    await message.delete()
    aaamsg = await message.channel.send('出來了嗎？❤')
    time.sleep(10)
    await aaamsg.delete()

  if any(word in msg for word in jpg_words):
    jpgmsg = await message.channel.send(random.choice(jpg))
    await message.delete()
    bbbmsg = await message.channel.send('好色唷❤')
    time.sleep(10)
    await bbbmsg.delete()
    
  if any(word in msg for word in mp4_words):
    jpgmsg = await message.channel.send(random.choice(mp4))
    await message.delete()
    cccmsg = await message.channel.send('要不行了啦❤')
    time.sleep(10)
    await cccmsg.delete()

  
# Bot起動
client.run(TOKEN)
