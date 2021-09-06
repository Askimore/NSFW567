
import discord
import googletrans
import os
import random
import time
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
    ansmsg = await message.channel.send('你出來了嗎？❤')
    time.sleep(5)
    await ansmsg.delete()  

  if any(word in msg for word in jpg_words):
    jpgmsg = await message.channel.send(random.choice(jpg))
    await message.delete()
    time.sleep(10)
    await jpgmsg.delete()
    anmmsg = await message.channel.send('你好:se4:唷❤')
    time.sleep(5)
    await anmmsg.delete()

  
# Bot起動
client.run(TOKEN)
