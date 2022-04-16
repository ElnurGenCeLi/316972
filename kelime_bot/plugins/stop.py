from pyrogram import Client
from pyrogram import filters
from random import shuffle
from kelime_bot import USERNAME
from pyrogram.types import Message
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *



@Client.on_message(filters.command("stop") & ~filters.private & ~filters.channel)
async def stop(c:Client, m:Message):
    global oyun
    
    siralama = []
    for i in oyun[m.chat.id]["oyuncular"]:
        siralama.append(f"{oyun[m.chat.id]['oyuncular'][i]}  :  {i}")
    siralama.sort(reverse=True)
    siralama_text = ""
    for i in siralama:
        siralama_text += i + "\n"     
    
    await c.send_message(m.chat.id, f"**Oyun {m.from_user.mention} tarafından bitirildi🤯\n Yeni oyuna başlamak için /game yazabilirsiniz...**\n\n**Puan -  Oyuncu**\n{siralama_text}")
    oyun[m.chat.id] = {}
    