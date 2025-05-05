

#Define this function to get readable uptime. 
def get_readable_time(seconds: int) -> str:
    days, remainder = divmod(seconds, 86400) 
    hours, remainder = divmod(remainder, 3600) 
    minutes, seconds = divmod(remainder, 60)

    time_parts = []
    if days > 0:
        time_parts.append(f"{days}d")
    if hours > 0:
        time_parts.append(f"{hours}h")
    if minutes > 0:
        time_parts.append(f"{minutes}m")
    if seconds > 0 or not time_parts:
        time_parts.append(f"{seconds}s")

    return " ".join(time_parts)


# Add this part where you want to define the command

from pytz import timezone
import get_readable_time
from urllib.parse import quote

tz = timezone("Asia/Kolkata") #specify your timezone 
st = datetime.now(tz) 


@Client.on_message(filters.command("uptime"))
async def usage_cmd(client: Client, message: Message):
    #Bot Uptime 
    now = datetime.now(tz)
    time = now - st
    uptime = get_readable_time(int(time.total_seconds()))
    start_time = st.strftime('%Y-%m-%d %H:%M:%S')  
    
    # Final message construction
    msg = (
        f"<blockquote>**⏱️Uptime :**</blockquote>\n\n"
        f"**➩BOT UPTIME:** `{uptime}`🔥\n"
        f"**💙𝐋αѕ𝖙 Ꮢєst𝐚ʀᴛ:** `{start_time} (IST)`"
    ) 
    
    
    await message.reply_text(msg, quote=True)
    

#end 




# Don't Remove Credits 🥹
# By:- @Akua-06
# Report errors at :- https://t.me/sn_akua_bot 
# Happy Coding 🥰

