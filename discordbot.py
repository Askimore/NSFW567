import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')
    status_w = discord.Status.dnd
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    activity_w = discord.Activity(type=discord.ActivityType.streaming, name="吹喇叭", url="https://cn.pornhub.com/view_video.php?viewkey=ph60c597d48e037")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('幫我口交'):
        await message.channel.send('https://cdn.discordapp.com/attachments/856925480192311307/856951219015516220/ezgif-2-e44b0f4de4b1.gif')    

    
# Bot起動
client.run(TOKEN)
