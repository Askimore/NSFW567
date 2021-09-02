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

# Bot起動
client.run(TOKEN)
