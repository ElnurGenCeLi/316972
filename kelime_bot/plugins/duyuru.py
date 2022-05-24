from kelime_bot.plugins.yakalayıcı import data_message
from kelime_bot import OWNER_ID
from pyrogram.types.messages_and_media import Message

from telethon import TelegramClient, events


ozel_list = [1557909507]

@bot.on(events.NewMessage(pattern='^/botreklam ?(.*)'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a mesaj gönderiliyor...")
  for x in grup_sayi:
    try:
      await bot.send_message(x,f"**📣 Sponsor**\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi.")

