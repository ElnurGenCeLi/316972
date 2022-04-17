from kelime_bot import rating
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message


@Client.on_message(filters.command("rating"))
async def ratingsa(c:Client, m:Message):
    global rating
    metin = """𝖦𝗅𝗈𝖻𝖺𝗅 𝖳𝗈𝗉 20 𝖮𝗒𝗎𝗇𝖼𝗎 :
     
    """
    eklenen = 0
    puanlar = []
    for kisi in rating:
        puanlar.append(rating[kisi])
    puanlar.sort(reverse = True)
    for puan in puanlar:
        for kisi in rating:
            if puan == rating[kisi]:
                metin += f"✓ **{kisi}** - 𝖯𝗎𝖺𝗇: **{puan}**\n"
                eklenen += 1
                if eklenen == 20:
                    break
                
    await c.send_message(m.chat.id, metin)
    
    
