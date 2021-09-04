  import discord
import googletrans
import os
import random
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']

client = discord.Client()

sad_words = ["$nsfw"]

jpg_words = ["$jpg"]

starter_encouragements = [
  
  "https://cdn.discordapp.com/attachments/856925480192311307/881587108517666816/ezgif.com-gif-maker.gif",
  "https://cdn.discordapp.com/attachments/869984495015714856/883262887999705118/dance.gif",
  "https://cdn.discordapp.com/attachments/869984495015714856/883267153749504000/ezgif.com-gif-maker.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883321268080898088/tumblr_pimzxziPII1s5y4eao1_540.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326607182397440/O2uwYdh.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326643597344768/6ec8dbfa455c264bae6e6befa6f0a4f7.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326657136586792/unnamed.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326660366204958/EVaI6co.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326666162729000/i015483469263.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326666678632478/2qblLg8.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326673804738571/15774792791983.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326678120669194/932e415bdd57f45aab9d64f28a158ff0.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326681388052550/img.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326683078336542/3516f6d3a6db9914e54c40b10c96297b.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326688753221632/ze23kA1.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326689193656352/1.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326700354699294/i15221404105.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326707182993408/eWKcP6q.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326714049101875/BwSzfXo.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326729169535056/8fef5380dd25d6a76c0f252028ab2f34_1605864535_4979.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326734638931979/b397a99b60df692fb1870e96949b1542.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326738539626506/KL8M4i7.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883326739332333598/i15538808604.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390197503508581/ezgif.com-gif-maker66.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390208912011294/ezgif.com-gif-maker_6.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390239975014490/ezgif.com-gif-maker_20.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390245494738984/ezgif.com-gif-maker_18.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390252683767818/ezgif.com-gif-maker_21.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390262099984404/ezgif.com-gif-maker_22.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390265845497856/ezgif.com-gif-maker_29.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390278864601158/ezgif.com-gif-maker64.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390296753332234/ezgif.com-gif-maker_42.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390308895826040/ezgif.com-gif-maker_24.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390359529480212/ezgif.com-gif-maker_25.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390385936810054/ezgif.com-gif-maker_23.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390393654341692/ezgif.com-gif-maker_41.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390399434096650/ezgif.com-gif-maker65.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390402856632360/ezgif.com-gif-maker_1.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390434712375306/ezgif.com-gif-maker_19.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390456292081684/ezgif.com-gif-maker_28.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390484926578708/ezgif.com-gif-maker_30.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390558310113360/ezgif.com-gif-maker_14.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390660630167582/ezgif.com-gif-maker_8.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390709846147172/ezgif.com-gif-maker_48.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390729077014619/ezgif.com-gif-maker63.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390732247892009/ezgif.com-gif-maker_5.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390745250250752/ezgif.com-gif-maker_33.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390752565104650/ezgif.com-gif-maker_38.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390758193868840/ezgif.com-gif-maker_9.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390778511065169/ezgif.com-gif-maker_45.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390804821942282/ezgif.com-gif-maker_52.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390860660715541/ezgif.com-gif-maker_61.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390886619279360/ezgif.com-gif-maker_62.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390892361273344/ezgif.com-gif-maker_53.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883390919557152838/ezgif.com-gif-maker_49.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391142698303489/ezgif.com-gif-maker62.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391152336805988/ezgif.com-gif-maker_36.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391177322278932/ezgif.com-gif-maker_3.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391186117738516/ezgif.com-gif-maker_54.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391198948106330/ezgif.com-gif-maker_50.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391207672254524/ezgif.com-gif-maker_7.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391228534718474/ezgif.com-gif-maker_56.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391230657048587/ezgif.com-gif-maker_15.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391237233737758/ezgif.com-gif-maker_10.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391254421991484/ezgif.com-gif-maker_39.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391270318407700/ezgif.com-gif-maker_27.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391304049000478/ezgif.com-gif-maker_34.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391303675691078/ezgif.com-gif-maker_35.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391326249447504/ezgif.com-gif-maker_26.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391337653751808/ezgif.com-gif-maker_17.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391345799098368/ezgif.com-gif-maker_58.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391362182041640/ezgif.com-gif-maker_47.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391382813823076/ezgif.com-gif-maker_60.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391441404039209/ezgif.com-gif-maker_13.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391445967462470/ezgif.com-gif-maker_59.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391462224576603/ezgif.com-gif-maker_31.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391463067623474/ezgif.com-gif-maker_40.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391482428522496/ezgif.com-gif-maker_57.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391483229646909/ezgif.com-gif-maker_55.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391486291480586/ezgif.com-gif-maker_44.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391493610569778/ezgif.com-gif-maker_51.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391530239410246/ezgif.com-gif-maker_37.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391550162358352/ezgif.com-gif-maker_46.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391575504322650/ezgif.com-gif-maker_16.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391580524933260/ezgif.com-gif-maker_4.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391613429252126/ezgif.com-gif-maker_11.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391688444379166/ezgif.com-gif-maker_43.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391689648140349/ezgif.com-gif-maker_2.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391693272014889/ezgif.com-gif-maker_32.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883391702172327967/ezgif.com-gif-maker_12.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883392529943392306/ezgif.com-gif-maker67.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883392501388558346/ezgif.com-gif-maker68.gif"
  
]

jpg = [
  
  "https://cdn.discordapp.com/attachments/883582213424291861/883582259863621662/tumblr_ozir9nTp2a1vf91eio9_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582356517158932/tumblr_ozjql1COr01vf91eio5_1280.jpg"
  
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
    activity_w = discord.Activity(type=discord.ActivityType.streaming, name="吹喇叭", url="https://cn.pornhub.com/view_video.php?viewkey=ph60c597d48e037")
    await client.change_presence(status= status_w, activity=activity_w)

    
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(starter_encouragements))

  if any(word in msg for word in jpg_words):
    await message.channel.send(random.choice(jpg))
    
    
# Bot起動
client.run(TOKEN)
