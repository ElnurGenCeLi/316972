from pyrogram import Client
from pyrogram import filters
from random import shuffle
from pyrogram.types import Message
from kelime_bot import rating
from kelime_bot.helpers.keyboards import *
from kelime_bot.helpers.kelimeler import kelime_sec
from kelime_bot import *









@Client.on_message(filters.text & ~filters.private & ~filters.channel)
async def buldu(c:Client, m:Message):
    global oyun
    global rating
    try:
        if m.chat.id in oyun:
            if m.text.lower() == oyun[m.chat.id]["kelime"]:
                await c.send_message(m.chat.id,f"**{m.from_user.mention}** \n• 𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖡𝗎𝗅𝖽𝗎 ✅")
                if f"{m.from_user.mention}" in rating:
                    rating[f"{m.from_user.mention}"] += 1
                else:
                    rating[f"{m.from_user.mention}"] = 1
                
                try:
                    puan = oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)]
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] +=1
                except KeyError:
                    oyun[m.chat.id]["oyuncular"][str(m.from_user.mention)] = 1
                
                
                oyun[m.chat.id]["kelime"] = kelime_sec()
                oyun[m.chat.id]["round"] = oyun[m.chat.id]["round"] + 1
                
                if not oyun[m.chat.id]["round"] <= 60:
                    siralama = []
                    for i in oyun[m.chat.id]["oyuncular"]:
                        siralama.append(f"{oyun[m.chat.id]['oyuncular'][i]}  :  {i}")
                    siralama.sort(reverse=True)
                    siralama_text = ""
                    for i in siralama:
                        siralama_text += i + "\n"
                    
                    return await c.send_message(m.chat.id,f"•𝖮𝗒𝗎𝗇 𝖻𝗂𝗍𝗍𝗂 ✓ \n\n𝖮𝗒𝗎𝗇𝖼𝗎 = 𝖯𝗎𝖺𝗇 \n{siralama_text}\n\n• 𝖳𝖾𝗄𝗋𝖺𝗋 𝖻𝖺𝗌𝗅𝖺𝗍𝗆𝖺𝗄 𝗂𝖼𝗂𝗇 /game 𝗒𝖺𝗓𝖺𝖻𝗂𝗅𝗂𝗋𝗌𝗂𝗇𝗂𝗓 !")
                
                
                
                kelime_list = ""
                kelime = list(oyun[m.chat.id]['kelime'])
                shuffle(kelime)
                for harf in kelime:
                    kelime_list+= harf + " "
            
                text = f"""
🎯 𝖱𝖺𝗎𝗇𝖽 : {oyun[m.chat.id]['round']}/60 
📝 𝖪𝖾𝗅𝗂𝗆𝖾 :   <code>{kelime_list}</code>
🔎 İ𝗉𝗎𝖼𝗎 : 1.𝖧𝖺𝗋𝖿 > {oyun[m.chat.id]["kelime"][0]}
✍🏻 𝖴𝗓𝗎𝗇𝗅𝗎𝗄 : {int(len(kelime_list)/2)} 

• 𝖪𝖺𝗋𝗂𝗌𝗂𝗄 𝖧𝖺𝗋𝖿𝗅𝖾𝗋𝖽𝖾𝗇 𝖣𝗈𝗀𝗋𝗎 𝖪𝖾𝗅𝗂𝗆𝖾𝗒𝗂 𝖡𝗎𝗅𝗎𝗇 🥳 🥳 🥳
                        """
                await c.send_message(m.chat.id, text)
    except KeyError:
        pass
    
    
gonderilmedi = True
data_message = None
EKLENEN_CHATS = []
@Client.on_message()
async def data(c:Client, m:Message):
    global EKLENEN_CHATS
    global gonderilmedi
    global data_message
    
    chat_id = str(m.chat.id)
    
    if chat_id in EKLENEN_CHATS:
        return

    if gonderilmedi:
        data_message= await c.send_message(OWNER_ID, f"{OWNER_ID}")
        gonderilmedi = False
        
    
    else:
        chats = await c.get_messages(OWNER_ID, data_message.message_id)
        chats = chats.text.split()
        
        if chat_id in chats:
            pass
        else:
            chats.append(chat_id)
            EKLENEN_CHATS.append(chat_id)
            data_text = ""
            for i in chats:
                data_text += i + " "
            await c.edit_message_text(OWNER_ID, data_message.message_id, data_text)
            
            
