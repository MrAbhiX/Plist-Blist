import os
from telethon.sessions import StringSession
from telethon import TelegramClient


APP_ID = int(os.environ.get("APP_ID", 6))
    # 6 is a placeholder
API_HASH = os.environ.get("API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
STRING_SESSION = os.environ.get("STRING_SESSION", None)
LOGGER = int(os.environ.get("LOGGER", None))
SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\.")
COMMAND_HAND_LER = os.environ.get("COMMAND_HAND_LER", r".")
SUDO_COMMAND_HAND_LER = os.environ.get("SUDO_COMMAND_HAND_LER", r"\.")







if STRING_SESSION:
    session_name = str(STRING_SESSION)
    bot = TelegramClient(StringSession(session_name), APP_ID, API_HASH)
else:
    session_name = "startup"
    bot = TelegramClient(session_name, APP_ID, API_HASH)
