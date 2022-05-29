from logging import getLogger
import os
from Abhi import bot, LOGGER
import asyncio
from sys import argv

LOGS = getLogger(__name__)

os.system("pip install -U telethon")


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
