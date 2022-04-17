from pyrogram import Clfrom, filters


message= "Ben bir botum"


@Client.on_message(filters.private & filters.command("start"))
async def starttgg(c, m):
    await m.reply(message)
