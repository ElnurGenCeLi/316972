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
            await c.send_message(m.chat.id,f"**Kelime pass geçildi !!\nEski kelime: <code>{oyun[m.chat.id]['kelime']}</code>**")
            
            oyun[m.chat.id]["kelime"] = kelime_sec()
            oyun[m.chat.id]["aktif"] = True
            
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
            
        else:
            await c.send_message(m.chat.id, f"<code>Üzgünüm pass hakkın bitmiş😐</code>\nOyunu bitirmek için /stop yazabilirsin...")
    else:
        await m.reply(f"**Grupta şu anda aktif bir oyun yok ❗️**")