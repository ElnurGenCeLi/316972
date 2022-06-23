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
        InlineKeyboardButton("Məni Qruba Əlavə Et ↗️", url=f"http://t.me/SozGameRobot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🧔🏻 Sahibim", url="https://t.me/o2o_GenCeLi"),
        InlineKeyboardButton("📣 Kanal", url="https://t.me/SecretMMC"),
    ]
])


START = """
**👋  Salam

Mən Qrub Üçün Yaradılmış Əyləncəli Oyun Botuyam Məni Qruba Əlavə Edərək Oyuna İndi Başla!**

Botun istifadə qaydasını öyrənmək üçün /help əmrindən istifadə edin
"""

HELP = """
**✌️ Əmirlər Menyusuna Xoş Gəldiniz.**
/game - Oyunu başlatmak üçün
/kec - Üç dəfə işlədə bilərsiz, oyunu geçmek üçün
/global - Global reytinq
/cancel - Oyunda çıxmaq üçün lazım olan əmr
"""

# Komutlar. 
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://te.legra.ph//file/f36232fb0762e88f9ec56.jpg",caption=START,reply_markup=keyboard)

@Client.on_message(filters.command("help"))
async def help(bot, message):
  await message.reply_photo("https://te.legra.ph//file/f36232fb0762e88f9ec56.jpg",caption=HELP) 

# Oyunu başlat. 
@Client.on_message(filters.command("game")) 
async def kelimeoyun(c:Client, m:Message):
    global oyun
    aktif = False
    try:
        aktif = oyun[m.chat.id]["aktif"]
        aktif = True
    except:
        aktif = False

    if aktif:
        await m.reply("**Oyun Qrubunuzda Dəvam Edir ✍🏻\nOyunu durdurmaq üçün yazıp /cancel durdura bilərsiz")
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
        
