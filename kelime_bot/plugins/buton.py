from pyrogram import Client, filters
from pyrogram.types import Message
from main import USERNAME, USERS_LIST, CHATS_LIST
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton

keyboard = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🎉 Gruba Ekle  🎉", url=f"http://t.me/Shark_Game_Bot?startgroup=new") 
    ],
    [
        InlineKeyboardButton("support 👨🏻‍💻", url="t.me/StarBotDestek"),
        InlineKeyboardButton("Kanal 📚", url="t.me/StarBotKanal")
    ],
    [
        InlineKeyboardButton("gelistiri 📚", url="t.me/ByWolk")
    ]
])



START = """
• Merhaba 🎉\n\n• Ben Bir Oyun Botuyum 🎮 \n\n• Çeşitli oyunlar oynamak ve eğlenceli vakit geçirmek için benimle oynayabilirsin ✍🏻 \n\n• Benimle oynamak için beni bir gruba ekleyip yönetici yapman lazim 💭
"""

    
    
    
    
    
    
"""
PRIVATE /start MESSAGE
"""
@Client.on_message(filters.command("start") & filters.private)
async def priv_start(c:Client, m:Message):
    await c.send_message(m.chat.id, START, reply_markup=keyboard)
