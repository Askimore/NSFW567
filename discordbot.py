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

# 收到訊息時呼叫
@client.event
async def on_message(message):
    # 送信者為Bot時無視
    if message.author.bot:
        return
    
    if message.content.includes("來段舞吧")
        var rnd = random(3,1) ;
        switch(rnd){
        case 1:message.channel.replay("https://cdn.discordapp.com/attachments/856925480192311307/882657302484770876/moiichan43_240835984_365616848349753_4194115607686417839_n.gif") ;break ;
        case 2:message.channel.replay("https://cdn.discordapp.com/attachments/856925480192311307/864755898785857586/eWKcP6q.gif") ;break ;
        case 3:message.channel.replay("https://cdn.discordapp.com/attachments/856925480192311307/864755845946146816/2qblLg8.gif") ;break ;
        
      

   if function random(max,min) 
var rnd = math.floor(math.random()*max)+min ;
        return rnd ;
    
    
    
# Bot起動
client.run(TOKEN)
