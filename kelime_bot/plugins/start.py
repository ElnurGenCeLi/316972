from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.errors import FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message


keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni Quruba Əlavə Et ➕", url=f"http://t.me/oke?startgroup=new")
    ],
    [
        InlineKeyboardButton("👨‍💻 Sahibi", url="https://t.me/kdkdmdm"),
        InlineKeyboardButton("📲 Yeniliklər", url="https://t.me/duzled"),
    ]
])


START = """
**• 👋 Salam Ösz Game 🕹 Oyununa Xoş Gəldiz 

• Mən qarışığ həriflərlə sözü tapmağ oyunuyam 🎯 

• Mənimlə oynamaq üçün məni qrupa əlavə edib sadə admin hüquqları verməlisən . 💭**

• • Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin ⛑
"""

HELP = """
⛑ Əmirlər Menyusu ⛑

/start - Botu başladar
/basla - Oyunu başlat 
/skip - Oyunu keç 
/global - Global reytinq 
/cancel - Oyunu dayndırmağ 

Əlaqə - @Vusaliw 👨‍💻
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://telegra.ph/file/69ab03c4a4274aeaca29a.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://telegra.ph/file/69ab03c4a4274aeaca29a.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("basla")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**Oyun Qurupunuzda Dəvam Edir ✍🏻\nOyunu diyandırmaq üçün /cancel yazıb diyandıra bilərsiz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tərəfindən!\nSöz Tapmaq Oyunu Başladı .\n\nYaxşı Olan Qazansın !", reply_markup=kanal)
        
        oyun[m.chat.id] = {"kelime":kelime_sec()}
        oyun[m.chat.id]["aktif"] = True
        oyun[m.chat.id]["round"] = 1
        oyun[m.chat.id]["kec"] = 0
        oyun[m.chat.id]["oyuncular"] = {}
        
        kelime_list = ""
        kelime = list(oyun[m.chat.id]['kelime'])
        shuffle(kelime)
        
        for harf in kelime:
            kelime_list+= harf + " "
        
        text = f"""
🎯 Raund: {oyun[m.chat.id]['round']}/60 
📝 Söz:   <code>{kelime_list}</code>
💰 Qazandığın Xal: 1
🔎 Kömək: {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluq : {int(len(kelime_list)/2)} 

✏️ Qarışık həriflərdən düzgün sözü tapın
        """
        await c.send_message(m.chat.id, text)
