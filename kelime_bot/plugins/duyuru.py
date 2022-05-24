from kelime_bot.plugins.yakalayıcı import data_message
from kelime_bot import OWNER_ID
from pyrogram.types.messages_and_media import Message

from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantsAdmins

ozel_list = [5234611328]
grup_sayi = []
  


@client.on(events.NewMessage(pattern='^/reklam ?(.*)'))
async def reklam(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Toplam {len(grup_sayi)} Gruba'a reklam gönderiliyor...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**📣 @deepkral **\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi reklamınız.")
