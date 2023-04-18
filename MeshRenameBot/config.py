from typing import Union

try:
    from .tconfig import Config
except ImportError:
    class Config:
        DATABASE_URL = [str, "mongodb+srv://shankswillson33:shankswillson33@cluster0.vshfo6u.mongodb.net/?retryWrites=true&w=majority"]
        API_HASH = [str, "95d2e8a1aa81fc9b7fa8a8aeafe59537"]
        API_ID = [int, 13986700]
        BOT_TOKEN = [str, "5580551341:AAGiwzpBQNqGWJ9HIUKv-otJjVczFY5gMcI"]
        COMPLETED_STR = [str, "▰"]
        REMAINING_STR = [str, "▱"]
        MAX_QUEUE_SIZE = [int, 40]
        SLEEP_SECS = [int, 10]
        IS_MONGO = [bool, True]

        # Access Restriction
        IS_PRIVATE = [bool, False]
        AUTH_USERS = [list,[1880221341]]
        OWNER_ID = [int, 1880221341]

        # Public username url or invite link of private chat
        FORCEJOIN = [str,"Wizard_Bots"]
        FORCEJOIN_ID = [int,-1001721659524]

        TRACE_CHANNEL = [int, -1001553361609]

try:
    from .tconfig import Commands
except ImportError:
    class Commands:
        START = "/start"
        RENAME = "/rename"
        FILTERS = "/filters"
        SET_THUMB = "/setthumb"
        GET_THUMB = "/getthumb"
        CLR_THUMB = "/clrthumb"
        QUEUE = "/queue"
        MODE = "/mode"
        HELP = "/help"
