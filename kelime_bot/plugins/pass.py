from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("pass") & ~filters.private & ~filters.channel)
async def passs(c:Client, m:Message):
    global oyun
    
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        if oyun[m.chat.id]["pass"] < 3:
            oyun[m.chat.id]["pass"] += 1 
            await c.send_message(m.chat.id,f"📖 𝖳𝗈𝗉𝗅𝖺𝗆 3 𝗉𝖺𝗌𝗌 𝗁𝖺𝗄𝗄𝗂𝗇𝗂𝗓 𝗏𝖺𝗋𝖽𝗂𝗋 !\n🥳 𝖪𝖾𝗅𝗂𝗆𝖾 𝖯𝖺𝗌 𝖦𝖾𝖼𝗂𝗅𝖽𝗂 !\n✏️ 𝖤𝗌𝗄𝗂 𝖪𝖾𝗅𝗂𝗆𝖾 : **<code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
            kelime_list = ""
            kelime = list(oyun[m.chat.id]['kelime'])
            shuffle(kelime)
            
            for harf in kelime:
                kelime_list+= harf + " "
            
            text = f"""
🎯 𝖱𝖺𝗎𝗇𝖽 : {oyun[m.chat.id]['round']}/60 
📝 𝖪𝖾𝗅𝗂𝗆𝖾 :   <code>{kelime_list}</code>
🔎 İ𝗉𝗎𝖼𝗎 : 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 𝖴𝗓𝗎𝗇𝗅𝗎𝗄 : {int(len(kelime_list)/2)} 

✏️ 𝖪𝖺𝗋𝗂𝗌𝗂𝗄 𝖧𝖺𝗋𝖿𝗅𝖾𝗋𝖽𝖾𝗇 𝖣𝗈𝗀𝗋𝗎 𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖡𝗎𝗅𝗎𝗇 🥳 🥳 🥳
            """
            await c.send_message(m.chat.id, text)
            
        else:
            await c.send_message(m.chat.id, f"<code>💭 𝖴𝗓𝗀𝗎𝗇𝗎𝗆 𝖯𝖺𝗌𝗌 𝖧𝖺𝗄𝗄𝗂𝗇 𝖡𝗂𝗍𝗆𝗂𝗌 ! </code>\n• 𝖮𝗒𝗎𝗇𝗎 𝖻𝗂𝗍𝗂𝗋𝗆𝖾𝗄 𝗂𝖼𝗂𝗇 /stop 𝗒𝖺𝗓𝖺𝖻𝗂𝗅𝗂𝗋𝗌𝗂𝗇 ✍🏻")
    else:
        await m.reply(f"💭 𝖦𝗋𝗎𝖻𝗍𝖺 𝗌𝗎 𝖺𝗇𝖽𝖺 𝖺𝗄𝗍𝗂𝖿 𝖻𝗂𝗋 𝗈𝗒𝗎𝗇 𝗒𝗈𝗄 !\n• 𝖸𝖾𝗇𝗂 𝗈𝗒𝗎𝗇 𝖻𝖺𝗌𝗅𝖺𝗍𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 /game 𝗒𝖺𝗓𝖺𝖻𝗂𝗅𝗂𝗋𝗌𝗂𝗇𝗂𝗓 ✍🏻")
