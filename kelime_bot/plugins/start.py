from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel & ~filters.edited)
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**Zaten şu anda devam eden bir oyun var !!**")
    else:
        await m.reply(f"**Kelime Bulma Oyunu {m.from_user.mention} Tarafından Başladı ✨\nİyi eğlenceler ❗️**", reply_markup=kanal)
        
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
🎯 Raund {oyun[m.chat.id]['round']}/60 
✍🏻 Kelime:   <code>{kelime_list}</code>
🔍 İpucu: 1.{oyun[m.chat.id]["kelime"][0]}
📏 Uzunluk: {int(len(kelime_list)/2)} 
Karışık harflerden doğru kelimeyi bulun 🤓
        """
        await c.send_message(m.chat.id, text)
        
