from pyrogram.types import BotCommand

# structure for commands list
COMMAND_LIST = [
    {"command": "start", "description": "Start the bot"},
    {"command": "help", "description": "Get help about the bot"},
    {"command": "genlink", "description": "Generate file share link"},
    {"command": "settings", "description": "Open bot settings"},
    {"command": "upload", "description": "Upload a new file"},
    # Add more here as needed
]


COMMANDS = [BotCommand(cmd["command"], cmd["description"]) for cmd in COMMAND_LIST]



# Don't Remove Credits 🥹
# By:- @Akua-06
# Report errors at :- https://t.me/sn_akua_bot 
# Happy Coding 🥰
