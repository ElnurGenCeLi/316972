from pyrogram import Client, filters


message= "**• Merhaba 🎉\n\n• Ben Bir Oyun Botuyum 🎮** \n\n**• Çeşitli oyunlar oynamak ve eğlenceli vakit geçirmek için benimle oynayabilirsin ✍🏻 **\n\n**• Benimle oynamak için beni bir gruba ekleyip yönetici yapman lazim 💭**"


@Client.on_message(filters.private & filters.command("start"))
async def starttgg(c, m):
    await m.reply(message)
