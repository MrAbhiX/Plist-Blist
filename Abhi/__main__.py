from logging import getLogger
import os
from Abhi import bot, LOGGER
import asyncio
from sys import argv
from telethon import TelegramClient
import telethon.utils


LOGS = getLogger(__name__)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
BOT_USERNAME = os.environ.get("BOT_USERNAME", None)



os.system("pip install -U telethon")


async def add_bot(bot_token):
    await bot.start(bot_token)
    bot.me = await bot.get_me() 
    bot.uid = telethon.utils.get_peer_id(bot.me)



if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.tgbot = None
    if BOT_USERNAME is not None:
        print("Initiating Inline Bot")
        # ForTheGreatrerGood of beautification
        bot.tgbot = TelegramClient(
            "TG_BOT_TOKEN",
            api_id=APP_ID,
            api_hash=API_HASH
        ).start(bot_token=BOT_TOKEN)
        print("Initialisation finished with no errors")
        print("Starting MafiaBot")
        bot.loop.run_until_complete(add_bot(BOT_USERNAME))
        print("MafiaBot Startup Completed")
    else:
        bot.start()
        

print(f"I'M STARTED")
async def humhai():
    try:
        if LOGGER != 0:
            await bot.send_file(
                LOGGER,
                
                caption=f"༆ʟɛɢɛռɖaʀʏ FEDBOT༆",
            )
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(humhai())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
