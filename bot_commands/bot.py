# Integration in bot.py file 

from config import AUTO_SET_COMMANDS
from commands import COMMANDS


#Add inside start() method, after 'get_me():' and before 'self.LOGGER(__name__, self.name).info("Bot Started!!")'
if AUTO_SET_COMMANDS:
    try:
        await self.set_bot_commands(COMMANDS)
        self.LOGGER(__name__, self.name).info("Bot Commands📋 set successfully.")
    except Exception as e:
        self.LOGGER(__name__, self.name).warning(f"🛑Failed to set bot commands: {e}")






# Don't Remove Credits 🥹
# By:- @Akua-06
# Report errors at :- https://t.me/sn_akua_bot 
# Happy Coding 🥰
