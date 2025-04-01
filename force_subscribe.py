# info.py / config.py / vars.py file..
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

FSUB_CHANNEL = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('FSUB_CHANNEL', '').split()] # give channel id with seperate space. Ex : ('-10073828 -102782829 -1007282828')


# force subscribe main code :- (Can be set in helper_func.py file) 
from config import FSUB_CHANNEL
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import *

async def is_subscribed(bot, query, channel):
    btn = []
    for id in channel:
        chat = await bot.get_chat(int(id))
        try:
            await bot.get_chat_member(id, query.from_user.id)
        except UserNotParticipant:
            btn.append([InlineKeyboardButton(f'Join {chat.title}', url=chat.invite_link)])
        except Exception as e:
            pass
    return btn

#@Client.on_message.....
#async def start(....
    if FSUB_CHANNEL:
        try:
            btn = await is_subscribed(client, message, FSUB_CHANNEL)
            if btn:
                username = (await client.get_me()).username
                if message.command[1]:
                    btn.append([InlineKeyboardButton("♻️ Try Again ♻️", url=f"https://t.me/{username}?start={message.command[1]}")])
                else:
                    btn.append([InlineKeyboardButton("♻️ Try Again ♻️", url=f"https://t.me/{username}?start=true")])
                await message.reply_text(text=f"<b>👋 Hello {message.from_user.mention},\n\nPlease join the channel then click on try again button. 😇</b>", reply_markup=InlineKeyboardMarkup(btn))
                return
        except Exception as e:
            print(e)




# Don't Remove Credits 🥹
# By:- @Akua-06
# Note:-  First See the file in which the code is to be placed. 
# Report errors at :- https://t.me/sn_akua_bot 
# Happy Coding 🥰



