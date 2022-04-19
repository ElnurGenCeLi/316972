from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("➕ Məni Qrupa Əlavə Et", url=f"http://t.me/SozTapmacaBot?startgroup=new")
    ],
    [
        InlineKeyboardButton("🖥️ Məni Yaradan", url="t.me/Pyhchistion"),
        InlineKeyboardButton("❓ Əmrlər", url="t.me/SozTapmacaResmi"),
    ]
])



START ="""
 **Salam 👋\n\n**Mən @SozTapmacaBot Məni Qrupunuza Əlavə Edərək Söz Tapmaca Oynaya Bilərsiz\n\nƏminəmki Sizi Qoymayacam Sıxılmağa\n\n\nSizde Belə Bir Bot İstəyirsizsə : @Pyhchistion**
"""

    
    
    
    
    
    
"""
PRIVATE /start MESSAGE
"""
@Client.on_message(filters.command("start") & filters.private)
async def priv_start(c:Client, m:Message):
    await c.send_message(m.chat.id, START, reply_markup=keyboard)
