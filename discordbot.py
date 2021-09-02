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
     game = discord.Game('吹你的大雞巴')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.dnd,activity=game)


# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    #如果包含 ping，機器人回傳 pong
    if message.content == ('跳舞')
    await message.channel.send('https://cdn.discordapp.com/attachments/856925480192311307/882657302484770876/moiichan43_240835984_365616848349753_4194115607686417839_n.gif')

# Bot起動
client.run(TOKEN)
