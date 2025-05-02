import time 


@Client.on_message(filters.private & filters.command(["ping", "p"]))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("<code>Pinging....</code>", quote=True)
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"<b>Pong 🏓!</b>\n{time_taken_s:.3f} ms")
    return time_taken_s



# Don't Remove Credits 🥹
# By:- @Akua-06
# Report errors at :- https://t.me/sn_akua_bot 
# Happy Coding 🥰
