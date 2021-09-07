
import discord
from discord.ext import commands
import os
import json
import random
import time
from pprint import pprint
# 輸入自己Bot的TOKEN碼
bot = commands.Bot(command_prefix='$')

with open('setting.json', 'r', encoding='utf8') as jfile
   jdata = json.load(jfile)

TOKEN = os.environ['TOKEN']

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')
    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.dnd

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.playing, name=" 弄 你 的 臭 雞 雞", url="https://cn.pornhub.com/view_video.php?viewkey=ph60c597d48e037")
    await client.change_presence(status= status_w, activity=activity_w)
    

      
# Bot起動
client.run(TOKEN)
