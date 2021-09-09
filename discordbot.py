
import discord
import googletrans
import os
import random
import json
import time
from pprint import pprint
# 輸入自己Bot的TOKEN碼
TOKEN = os.environ['TOKEN']

client = discord.Client()

sad_words = ["$nsfw"]

jpg_words = ["$jpg"]

mp4_words = ["$mp4"]

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
  "https://cdn.discordapp.com/attachments/883316057283108924/883392501388558346/ezgif.com-gif-maker68.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883531577617960960/image0.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883550684040032357/image0.gif",
  "https://s6.ezgif.com/save/ezgif-6-3aae739194a3.gif",
  "https://s6.ezgif.com/save/ezgif-6-8f7f8fab00b6.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572400124485652/210904_6.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572422060671036/210904_2.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572426670239744/210904_5.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572444818993183/210904_4.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572453014646814/210904_11.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572455808061490/210904_1.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572470123208765/210904_8.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572470865604628/210904_7.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572474896330812/210904_10.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572477970767872/210904_9.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883572907563941908/image0.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883578591898652762/210904_12.gif",
  "https://cdn.discordapp.com/attachments/883316057283108924/883578599272235048/210904_13.gif"
  
]

jpg = [
  
  "https://cdn.discordapp.com/attachments/883582213424291861/883582259863621662/tumblr_ozir9nTp2a1vf91eio9_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582356517158932/tumblr_ozjql1COr01vf91eio5_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582366491217930/tumblr_ozjql1COr01vf91eio10_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582414411169853/tumblr_ozir9nTp2a1vf91eio7_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582487018754078/tumblr_pipf9gH56m1xox4yko1_640.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582494727868436/tumblr_pipf9gH56m1xox4yko3_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582784248086598/tumblr_on5i3chsaQ1w31n5xo1_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582805517410334/tumblr_inline_opqqf9uI6J1uk8ne9_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582918776221736/tumblr_p0dja6Jlka1vf91eio7_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883582920265199646/tumblr_p0dja6Jlka1vf91eio5_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883583177422151700/21.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883583179078905876/24.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883583451289247764/rs9m84w4rrd21.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883583452195225650/9T8wmvi.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883583452572680212/D0uL4O0XQAElq1y.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883583981306675250/tumblr_p9fisfnO4E1xr9y7so1_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584080170606672/strugglingguy_195079089_303919924793024_8529951646469367857_n.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584093261004840/tumblr_opupxkcUQh1w5jn34o8_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584208826691614/plant.lily_218111053_371919814268976_2551655048679593476_n.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584255970639892/photo_2021-06-19_00-24-37.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584265927929856/nr9e934WSD1rwp671o1_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584459151138857/m40925_198823145_793407354644874_4050101979349464463_n.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584462221352971/m40925_191913642_800120523976072_2940247273776926335_n.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584724252114964/EMHGjcPUUAEjHV6.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584725992734791/ELOfhsUUEAIRlPi.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584732498100234/EL-UnZAUcAEkTD_.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584736109404160/EL-UnZCUcAAvkvN.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584737116049438/EMHGjcMUEAATbAI.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584784134189096/EfwxCWdVoAE7dKF.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584785958703114/EfwxCWeU8AAUnKz.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584793382625290/EfGP4NxU0AAK6LB.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584837397676053/EcQDEdVUYAIGded.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584889373458463/E45vpNfVgAUvuRV.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584894201131038/E45zBhUVcAIG2CC.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584960903151626/E4UrFjnVoAUODBT.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584964141125662/E4pt_hzVkAQl_m8.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883584966640930866/E4pt_jBVIAEX2Ho.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585234132688927/Dogge_3.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585237425201172/Dogge_4.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585241430782032/Dogge_5.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585244136087613/Dogge_6.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585248548491324/Dogge_8.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585253443264512/Dogge_2.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585347928342548/D-1aoyPUIAAtMEC.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585370585989150/D_UsbFTUwAAUU1M_2.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585536730726430/80444311_p0_.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585537850622002/71744896_p0_.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585594859597874/62859920_E324_4F8C_B3CB_CC0F94060A3E.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585661343518720/23055366moded_3.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585866025553930/E6lL2oTUUAMQd1D.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883585867652939776/E6lL2oUVkAUkhFj.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883586438770339850/Dtn_UKTV4AA77lQ.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883586627455299614/DuHxEHxW0AA7x_b.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883586631704133632/DuHxEHuX4AASJWz.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883586635688710154/DuHxEHwXQAEamoi.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883586838848208936/D-zUUhWU0AEijPP.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883587058285834240/EgPoxLnUEAEQfB-.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883587122240561162/EHUooPTVUAIqGco.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883587327111348234/D_eQcn3XUAAmjQE.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883587427183255592/tumblr_o9eibrfeqa1v4l2v8o1_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883587428911288340/tumblr_o9eibrfeqa1v4l2v8o6_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883587906743201812/IMG_6762.JPG",
  "https://cdn.discordapp.com/attachments/883582213424291861/883587908630614037/IMG_6763.JPG",
  "https://cdn.discordapp.com/attachments/883582213424291861/883588557728518214/89_FAFSHIM_89.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883588611101036554/77_FAFSHIM_77.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883588666776223794/68_FAFSHIM_68.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589231145009192/15_00_15.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589271062208552/07_00_7.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589451538898984/26_evelynn_kda_nsfw3.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589456748224512/07_kda_akali_neon_nsfw2.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589459218673684/11_k_da_ahri_nsfw.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589461773017108/15_KaiSa_4.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589616559616020/30_boette_bowsett_peach_sandwich.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589616580558858/35_bosette_virginkillersweater_nsfw.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589619059396648/40_bowsette_nsfw3.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589871384539176/007_74119003_p0_On_her_way_to_serve_you.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589870784753674/001_73304699_p0_Doggy_Miku.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589873578168371/003_76038043_p0_Tactical_flesh_doll.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589923062554634/023_70942382_p0_Mikus_special_restraint_chair.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883589943081971722/017_72105978_p1_lovely_vehicle_.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590017031753748/030_70699585_p0_MIKUs_blow_job_task.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590035482497044/036_69759800_p0_Flesh_toy_of_all_sailors.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590104042577921/042_69039743_p0_Voiceroid_discipline_lab.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590210116546590/055_67773166_p1_.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590457840513094/131_72506340_p1_.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590724489191474/002_72285538_p1_Camilla_holiday.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590820937203774/172_69464870_p1_Term_79_JPG_PSD_video_summary.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590920568733696/246_64039863_p0_D.va_Selfie.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883590935114551306/252_63558583_p0_D.vahri_combo.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883591260399620107/001_3.png",
  "https://cdn.discordapp.com/attachments/883582213424291861/883591261871800381/002_3.png",
  "https://cdn.discordapp.com/attachments/883582213424291861/883591700075925584/020_FFA03170.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883591711480221716/034_FFA03310.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883591753427484682/013_FFA03099L.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592196954136616/049_Ea7fE2GVAAEc7Mt.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592199386853387/015_E2JwMMjVEAMj8Vq.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592199537831936/016_E2JwMMjVkAArVy1.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592201022615622/040_E4u61qSUUAsnipi.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592431524794378/129_EeGNMxLVoAAIIRw.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592431524794378/129_EeGNMxLVoAAIIRw.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592433772924939/128_EeGNMxLUYAEbDma.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592447270199326/156_EhokLayU4AAcwQX.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592712786419752/283_EqOTFjxVEAE8puJ.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592717697953823/284_EquX7v_VoAMZ4xt.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592775340290048/405_EzvhCknVkAAZ9KY.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592862183350272/364_Ez0kAJfVkAE_lci.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883592893766434857/357_EZ_u3_oU0AAu8S7.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883593563135422514/43_DSC_42.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594367338708992/089_B042.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594368836055060/118_B071.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594370056618014/120_B073.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594618317459506/IMG_0537.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594623623237652/IMG_0589.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594655571263568/IMG_0455.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594959536676924/tumblr_pdy819Bz0B1swbon6o2_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594968080474142/tumblr_pbqxc4NZ7z1swbon6o2_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883594977911926784/tumblr_pc9m1hIADq1swbon6o1_1280.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883595014385590302/tumblr_pdw8jaFYLd1swbon6o1_540.jpg",
  "https://cdn.discordapp.com/attachments/883582213424291861/883595196707782697/507999.jpg"
  
]

mp4 = [


  "https://cdn.discordapp.com/attachments/884435564693160056/884435743924174888/3HlPAMw1UyWjdoSS.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884475885363802172/3HlPAMw1UyWjdoSR.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829351235964938/tumblr_p96zwarNgo1wwr1ds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829362287956039/tumblr_p9lxamA45S1wwr1ds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829369422467103/tumblr_p8exvb7b681vl3dh5.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829374350778378/tumblr_p7ufjtz5it1wwr1ds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829389869678592/Tumblrbunnybunny-love_-_Pornhubcom.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829390935044187/tumblr_p9wm7gPa1e1wwr1ds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829399487234048/tumblr_p5bxskJ7pQ1wwr1ds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829410686033970/tumblr_p74u0pA2lF1wwr1ds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829422769831946/tumblr_pa3vjb4nef1wwr1ds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829429489094686/tumblr_pco42kYELR1xr9y7s.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829438100000788/tumblr_paf92syWMh1xrkq9n_480.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829443179282472/tumblr_pbnlc7JBV81xrkq9n_480.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829446484410418/tumblr_pajq9vIAvH1xrkq9n_480.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829456328446003/tumblr_pa7tl8uwJc1xrkq9n_480.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829473080504340/tumblr_pj82sm2yRw1xrkq9n.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829506634940436/tumblr_phedtkjop41xjg3z1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829510862794832/ZIyavlxWTuweuwds.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829511399657502/ufkY4fqj7N3kgaJ-.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829512146251796/QKppBS4paRaAkucz.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829522774589441/tumblr_pgol0gbVGg1xrkq9n.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829533965004850/NrKI9cBPf1rUwALd.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829533902082118/tumblr_pb7133vEHY1xrkq9n.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829537614065714/SVmFMe7LZcNDDQXG.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829541279879238/tumblr_pakt1uPyQA1xrkq9n.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829723656589452/2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829741885050881/3_8o4qy2a8cKaF3j.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829742811988039/3c6YzFDorZl1f3HL.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829764081315850/1_2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829846230949939/-.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829849267626095/-_.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829963889565746/5jt7c3ToO2DsTpqe.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829977802047528/8OQbG83Z9vRR10sc.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829978900967464/22pMgoc0g7NtKmKH.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884829992175927346/8-Sf_E5JgZMOiFRQ.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830001294368809/91shipin-1073543733482803201-20181214_194226-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830012870647828/9.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830013738868786/10.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830034844598362/4_ETjd2DjV7XM7Jn.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830095414530109/41642989_1931143666982526_4373653463389700096_n.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830108114911262/AAzj7VV1cB2foDzV.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830109415125022/anazawsea-1070330095825371136-20181205_225235-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830160896008202/badunclept-1070210089695371264-20181205_145543-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830273202712616/badunclept-1070715774761717760-20181207_002508-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830274901377034/badunclept-1070710688933281793-20181207_000455-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830289631789207/badunclept-1070711656269864960-20181207_000846-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830289933766706/badunclept-1070212577794224129-20181205_150536-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830376919453756/Csshn12-1071959951327674368-20181210_104903-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830391331061840/bugu520-1072387432069378050-20181211_150742-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830393944125460/beauty_taotao-1070235828247420928-20181205_163800-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830403473600592/BDSM_1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830408045396018/C_FLLk4OTmwg_ffH.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830409261715546/bE61EZjAOzlUM18p.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830496427757658/dOLbrqbzuvWU1ZEF.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830504011042856/fHv5Uxq0JFSn1ynv.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830546847469568/Dz-Z8AiEXsNn0mHE.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830577243611287/cv9zxnM9MEGyXI0s.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830581530189824/FmVPSF79NUz1JOsL.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830588027170907/hYswr_kHElFGGVTj.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830591273562112/H_u-BMkawVP0f6KA.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830599607631893/Everything_About_Nothing_sun_shadesFollow_me_on_eroshare_Forget.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830605274136706/IbuYvOuGT3espxRG.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830615743119370/H0thQyJ6U0Jtygz5.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830631480147998/Facebook_1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830632801345556/EBCnCyPpIYrEq4M2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830648450314271/GvoQfQyl2u6FCp85.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830673632915477/FR76Svi-8MxHCiyk.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830681417547806/euUOABQlUxgdF5Fw.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830693732016148/KKVTPqE7oM1896-7.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830700514185266/DandSMaster-1074504305493782528-20181217_111924-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830722668523520/JKF_20.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830732546084944/GqYzMFFomQvr4to7.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830732927795270/gohiKhPa3KbE8ne4.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830754771709962/MasterD1234-953855947893592064-20180118_130554-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830765119074304/MasterD1234-927537097631657984-20171106_220411-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830767388176404/GkhtbcHbJjczHD5h.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830768055066655/ddd.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830783515267122/MissReinaT_-_Asian_Student_Seduce_Teacher_-_ManyVids.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830810098790400/nidemugou-1069632126989942787-20181204_003906-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830819422715944/MissReinaT_-_Spy_on_my_private_show_-_ManyVids.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830828000063488/NG_5bFEHYz8li7Ba.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830831162585088/jQQ7mS0Zw7ZC_aQi.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830834245378088/Jr4zUUPFuY9ockTx.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830840897556510/nidexiaomugou-1074681002612543488-20181217_230132-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830845435772978/my4prdGXDNf3a7Co.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830849466527755/nZPO-sBJcLWJTvos.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830849399394314/MissReinaT_-_Dirty_Girl_-_ManyVids.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830854499684382/MissReinaT_-_Horny_In_My_Bathroom_-_ManyVids.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830861940371486/L6ZACLO52uf5WOKW.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830864209502208/J6nP0tAyhbWEaRO2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830874863017984/MissReinaT_-_Profile_-_ManyVids_3.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830886686765146/J9K5FIDq2l5K_cV_.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830898581798932/JReZEIamCtX1cxzP.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830952877076541/Os2BeEsWYc6NY5P-.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830969591365683/P_.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830989124255774/PdJtHjHc2GEwkjrI.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884830991309504552/pCgwmdgSIgHcVg-1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831039829205062/Q3DjqpZ2upIK-NkQ.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831065737416764/pRzYsJBSy6bgqDrt.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831082510450758/qflLjwA_pIab8Ym2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831084515323974/PRavqHPloTiL_afC.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831113846091906/ribenguniang-1072154142892789760-20181210_234041-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831139158696036/Richard_ssss-990410156432338944-20180429_095916-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831142728040569/Richard_ssss-1018767846992560128-20180716_160237-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831144284155904/Richard_ssss-1056375549520539649-20181028_104212-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831164966252554/Richard_ssss-1013419586882973696-20180701_215032-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831164966252554/Richard_ssss-1013419586882973696-20180701_215032-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831173023518730/Richard_ssss-1069108788928503808-20181202_135933-vid1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831209207787572/RkeQhxYhms9fPslb.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831549852385290/The_Most_CUTIES_THING_you_have_ever_seen__Ahegao_rtc.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831551781765120/Tumblr_2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831555485319238/Tumblr_3.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831568789655572/Ts2EtJZek2W1U9l4.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831579246067712/T6APCAmL_dOoiGSX.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831607175917578/Tumblr_4.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831614377537606/tumblr_p2nolpjys21wg2ri1_480.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831624842334228/tDsSMgfRnifLkZ70.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831629900677210/Tumblr.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831646736609281/tumblr_p3vf24QeB11x5obay.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831657394331678/Tumblr_1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831660263227442/tumblr_p0aeutpMk41wg2ri1_720.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831668790231060/tumblr_o3qaqbmofs1v7m0s5.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831701006692422/Tumblr_9.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831735509041152/tumblr_olriglN1El1w0827b.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831746275827762/tumblr_p0nwvuvcL21wktzj2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884831817507668079/tumblr_p4722n38Jm1x5obay.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832008528863232/2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832008277217330/1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832032620949585/ZXyMAfAKakEDgW5O.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832033740828742/2.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832091072790578/V-sRb0xVAVV7IQ-I.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832134198603776/VNphRuE3JtT7VhIG.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832231967838258/Tv0jH_1gAkY2JFqj.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832291296280576/tumblr_pi8gm8dm0z1x62hlb_480.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832349899071488/tumblr_pjt56n8mr11xtjb3m.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832352818331669/tumblr_pjtqnysx121xtjb3m.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832788149305435/eeb38b3f30683403.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884832829442248755/c7c98bcb6e49bd76.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884833227469127821/Zx-5sfkfTIS23A7Y.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884833228916150272/QoHEUZLRxAkTWhTd.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884833229230719008/S_IIp8-XvYG5fCUY.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/884833235706732544/vW4ZvyfKAWtwu8Fd.mp4",
  "https://cdn.discordapp.com/attachments/700217350456213515/882174419651416125/chftEJVUCU3_N0US.mp4",
  "https://cdn.discordapp.com/attachments/700217350456213515/882288900515709008/video0.mp4",
  "https://cdn.discordapp.com/attachments/700217350456213515/882673628745986108/-.mp4",
  "https://cdn.discordapp.com/attachments/700217350456213515/882867589976559646/8ngbC8JPaEyYVfT8.mp4",
  "https://cdn.discordapp.com/attachments/700217350456213515/883223634628476928/VID_20210903_133420_058.mp4",
  "https://cdn.discordapp.com/attachments/700217350456213515/884070017514233876/wo-huan-bu-qu-mai-re-gou.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885103855338139688/online-video-cutter.com_1.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885103823474003998/31796351a.webm",
  "https://cdn.discordapp.com/attachments/884435564693160056/885103823188807710/31796331a.webm",
  "https://cdn.discordapp.com/attachments/884435564693160056/885099534785589298/69395c65c8be92bb.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885099514359328788/xdianying_846.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885099506184646676/7ca070bd0a7a4635.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885099493928865822/xdianying_686.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885099481190764574/1013gangan_.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098939211214908/video_2021-09-03_20-07-55.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098917514072114/video_2021-06-10_00-14-04.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098907858767872/video_2021-06-10_00-15-38.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098907858767872/video_2021-06-10_00-15-38.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098903584796712/video_2021-06-10_00-22-22.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098881317228554/video_2021-06-10_00-14-50.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098855727771658/video_2021-04-18_02-04-53.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098786085560340/video_2021-05-09_11-56-02.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098742938763294/IMG_3826.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098711674413126/IMG_7133.mov",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098707572391966/IMG_6643.MP4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098698458169364/IMG_6644.MP4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098690715455518/IMG_6641.MP4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098685216735254/IMG_6642.MP4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098677264338944/IMG_6640.MP4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098644922060840/IMG_4954.MP4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098589515288617/IMG_2987.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098440713965568/IMG_1636.MP4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098228297637888/F910773AAA5F3C572B550D2A1CEABE35.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885098018737647626/210112163420.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885097757277306890/647bba344396e7c8170902bcf2e15551.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885097693704249354/5fa987a927d7e2bc7e7f0_source.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885097651060744242/LittIe3.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885097628705103882/3.mp4",
  "https://cdn.discordapp.com/attachments/884435564693160056/885097599181398076/6D65C3623926D4EFBCEA947C93762586.mp4"


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
    activity_w = discord.Activity(type=discord.ActivityType.playing, name="🍆👅💦")
    await client.change_presence(status= status_w, activity=activity_w)


      
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
  
  
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)
    
  if any(word in msg for word in sad_words):
    gifmsg = await message.channel.send(random.choice(starter_encouragements))
    await message.delete()
    time.sleep(30)
    await gifmsg.delete()
    aaamsg = await message.channel.send('出來了嗎？❤')
    time.sleep(5)
    await aaamsg.delete()  

  if any(word in msg for word in jpg_words):
    jpgmsg = await message.channel.send(random.choice(jpg))
    await message.delete()
    time.sleep(10)
    await jpgmsg.delete()
    bbbmsg = await message.channel.send('好色唷❤')
    time.sleep(5)
    await bbbmsg.delete()
    
  if any(word in msg for word in mp4_words):
    jpgmsg = await message.channel.send(random.choice(mp4))
    await message.delete()
    cccmsg = await message.channel.send('要不行了啦❤')
    time.sleep(5)
    await cccmsg.delete()

  
# Bot起動
client.run(TOKEN)
