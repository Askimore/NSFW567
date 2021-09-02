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
    game = discord.Game('你的小雞雞')
    #discord.Status.<狀態>，可以是online,offline,idle,dnd,invisible
    await client.change_presence(status=discord.Status.dnd, activity=game)

   
@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
   
    if message.content == '跳個舞吧':
        await message.delete()
        
        await message.channel.send('https://cdn.discordapp.com/attachments/856925480192311307/882657302484770876/moiichan43_240835984_365616848349753_4194115607686417839_n.gif')
    
        await asyncio.sleep(10)
        
        await tmpmsg.delete()
    
    
    
# Bot起動
client.run(TOKEN)
