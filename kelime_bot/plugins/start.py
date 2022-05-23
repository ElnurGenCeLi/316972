from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import oyun
from kelime_bot.helpers.kelimeler import *
from kelime_bot.helpers.keyboards import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery


# Komut
@Client.on_message(filters.command("start"))
async def start(bot, message):
  await message.reply_photo("https://i.ibb.co/khRz42f/Turkish-Voice.jpg",caption=START,reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="Repo", url="https://t.me/Botdestekgrubu")]]))



START_TEXT = f"""
🙋‍♂️ Merhaba Ben <b>Kelime bot</b>

<b>I specialize for logo design  Services with Amazing logo 
Creator Platform & more tools</b>
                                
<b>Powered by</b>:
◈ <code>Single Developers Logo Creator API</code>
◈ <code>TroJanzHex Image editor</code>
◈ <code>Pyrogram</code>
"""

START_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("About", callback_data="_about"),
                    InlineKeyboardButton("Help", callback_data="_help")
                ],
                [
                    InlineKeyboardButton("Updates", url="https://t.me/szteambots"),
                    InlineKeyboardButton("Support", url="https://t.me/slbotzone")
                ],
            ]
        )

GROUP_BTN = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("help", callback_data="helpmenu")
                ]
            ]
        )

HELP_TEXT = f"""

**Help Menu** : 

- `/game [logo name ]`
- `/logohq [logo name ]`
- `/rmbg` [reply to photo ]
- `/edit` [reply to photo ] 
- `/text` [reply or send with text]
- `/write - [text]`
- `/carbon` [reply to text]
- `/wall or wallpaper [name]`

**Powered By** ~ @Mahoaga
"""

BACKTOHOME = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("🔙Back", callback_data="startmenu")
                ]
            ]
        )

ABOUT_TEXT = """
**Logo Design Platform in Telegram , 
World First Time With Image Editor tools**

🔥You Can Create Many Type Of **Logo Design**
For your Dp & More Usage , Remove Background  
With full **Advance image Editor Features** Included 
This Bot Based on @MalithRukshan **Logo API**
& **TroJanzHex Image editor** 

ᗚ **Features** : 

[+] Api Based logo Creator.
[+] Rando logo Creator .
[+] Carbon maker.
[+] Background Remover.
[+] Text art Genarator 80+ styles.
[+] Image editor.
`(Bright | Mixed | Black & White | Cartoon 
Circle | Blur | Border | Sticker |
Rotate | Contrast | Sepia | Pencil 
| Invert | Glitch | Remove Background)`
"""

CLOSE_BTN =  InlineKeyboardMarkup(
            [[InlineKeyboardButton("• sᴜᴘᴘᴏʀᴛ •", url="https://t.me/DevilsHeavenMF")]])


FSUB_TEXT = """
**🚫 Access Denied**
You Must Join [• sᴜᴘᴘᴏʀᴛ •](https://t.me/DevilsHeavenMF)To Use Me. So, Please Join it & Try Again.
            """

FSUB_BTN = InlineKeyboardMarkup(
            [[InlineKeyboardButton("• sᴜᴘᴘᴏʀᴛ •", url="https://t.me/DevilsHeavenMF")]])

@Client.on_callback_query(filters.regex("startmenu"))
async def startmenu(_, query: CallbackQuery):
    await query.edit_message_text(START_TEXT,
        reply_markup=START_BTN,
     disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("_help"))
async def helpmenu(_, query: CallbackQuery):
    await query.edit_message_text(HELP_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("_about"))
async def aboutenu(_, query: CallbackQuery):
    await query.edit_message_text(ABOUT_TEXT,
        reply_markup=BACKTOHOME,
     disable_web_page_preview=True
    )

@Client.on_callback_query(filters.regex("closeit"))
async def close(_, query: CallbackQuery):
    await query.message.delete()        




# Mahoaga Ufak çaplı düzenlemeler.
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
        await m.reply("**❗ Oyun Zaten Grubunuzda Devam Ediyor ✍🏻 \n Oyunu durdurmak için yazıp /stop durdurabilirsiniz")
    else:
        await m.reply(f"**{m.from_user.mention}** Tarafından! \nKelime Bulma Oyunu Başladı .\n\nİyi Şanslar !", reply_markup=kanal)
        
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
🎯 Raund : {oyun[m.chat.id]['round']}/60 
📝 Söz :   <code>{kelime_list}</code>
💰 Kazandığınız Puan: 1
🔎 İpucu: 1. {oyun[m.chat.id]["kelime"][0]}
✍🏻 Uzunluk : {int(len(kelime_list)/2)} 

✏️ Karışık harflerden doğru kelimeyi bulun
        """
        await c.send_message(m.chat.id, text)
        
