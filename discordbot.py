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
    game = discord.game('吹妳老公的大雞巴')
    await client.change_presence(status=discord.Status.dnd, activity=game)

    
   @client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if message.content == '過來幫我吹':
        
    await message.channel.send('https://cdn.discordapp.com/attachments/856925480192311307/883038733765574676/ezgif-2-e44b0f4de4b1.gif') 
    
# Bot起動
client.run(TOKEN)
