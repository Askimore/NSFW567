import discord
import googletrans
import os
from pprint import pprintimport discord
import requests
import json
import random
from replit import db

# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

# 起動時呼叫
@client.event
async def on_ready():
    print('成功登入')
    #這邊設定機器人的狀態
    #discord.Status.<狀態>，可以是online（上線）,offline（下線）,idle（閒置）,dnd（請勿打擾）,invisible（隱身）
    status_w = discord.Status.dnd

    #這邊設定機器當前的狀態文字
    #type可以是playing（遊玩中）、streaming（直撥中）、listening（聆聽中）、watching（觀看中）、custom（自定義）
    activity_w = discord.Activity(type=discord.ActivityType.streaming, name="吹喇叭", url="https://cn.pornhub.com/view_video.php?viewkey=ph60c597d48e037")
    await client.change_presence(status= status_w, activity=activity_w)

sad_words = ["nsfw"]

starter_encouragements = [
  "https://cdn.discordapp.com/attachments/856925480192311307/881587108517666816/ezgif.com-gif-maker.gif",
  "https://cdn.discordapp.com/attachments/869984495015714856/883262887999705118/dance.gif",
  "https://cdn.discordapp.com/attachments/869984495015714856/883267153749504000/ezgif.com-gif-maker.gif"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragment(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
  db["encouragements"] = encouragements

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("$inspire"):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))
    
# Bot起動
client.run(TOKEN)
