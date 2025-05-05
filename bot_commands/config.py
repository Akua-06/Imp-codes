#Add this to the config.py file of your bot repo. 

import os

AUTO_SET_COMMANDS = str(os.environ.get("AUTO_SET_COMMANDS", "True"))
# Enable auto setting bot commands on startup, (default: True)
