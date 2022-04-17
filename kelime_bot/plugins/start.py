from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *

@Client.on_message(filters.command("game") & ~filters.private & ~filters.channel & ~filters.edited)
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("• 𝖹𝖺𝗍𝖾𝗇 𝖲𝗎 𝖠𝗇𝖽𝖺 𝖣𝖾𝗏𝖺𝗆 𝖤𝖽𝖾𝗇 𝖡𝗂𝗋 𝖮𝗒𝗎𝗇 𝖵𝖺𝗋 ! ! ! \n• 𝖮𝗒𝗎𝗇𝗎 𝖽𝗎𝗋𝖽𝗎𝗋𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 » /stop 𝗄𝗈𝗆𝗎𝗍𝗎𝗇𝗎 𝗄𝗎𝗅𝗅𝖺𝗇𝗂𝗇 !")
    else:
        await m.reply(f"𝖪𝖾𝗅𝗂𝗆𝖾 𝖳𝗎𝗋𝖾𝗍𝗆𝖾 𝖮𝗒𝗎𝗇𝗎 \n**{m.from_user.mention}** \n𝖳𝖺𝗋𝖺𝖿𝗂𝗇𝖽𝖺𝗇 𝖡𝖺𝗌𝗅𝖺𝗍𝗂𝗅𝖽𝗂 !\n**İyi Eğlenceler 🥳 🥳 🥳**", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["pass"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 𝖱𝗈𝗎𝗇𝖽 : {oyun[m.chat.id]['round']}/60 
📝 𝖪𝖾𝗅𝗂𝗆𝖾 :   <code>{kelime_list}</code>
🔎 İ𝗉𝗎𝖼𝗎 : 1.𝖧𝖺𝗋𝖿 > {oyun[m.chat.id]["kelime"][0]}
✨ 𝖴𝗓𝗎𝗇𝗅𝗎𝗄 : {int(len(kelime_list)/2)} 
• 𝖪𝖺𝗋𝗂𝗌𝗂𝗄 𝖧𝖺𝗋𝖿𝗅𝖾𝗋𝖽𝖾𝗇 𝖣𝗈𝗀𝗋𝗎 𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖡𝗎𝗅𝗎𝗇 🥳 🥳 🥳
        """
        await c.send_message(m.chat.id, text)
        
