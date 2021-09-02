import discord
import googletrans
import os
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']
SRCLanguage=os.environ['SRC']
DSTLanguage=os.environ['DST']

client = discord.Client()

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.dnd

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.custom, name="吹妳老公的大雞巴", url="https://cdn.discordapp.com/attachments/856925480192311307/883038733765574676/ezgif-2-e44b0f4de4b1.gif")

    await client.change_presence(status= status_w, activity=activity_w)

   
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
   
    if message.content == '跳個舞吧':
     
        
        tmpmsg = await message.channel.send('https://cdn.discordapp.com/attachments/856925480192311307/882657302484770876/moiichan43_240835984_365616848349753_4194115607686417839_n.gif')
     
  
    
# Bot起動
client.run(TOKEN)
