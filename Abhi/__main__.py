from logging import getLogger
import os
from Abhi import bot, LOGGER
import asyncio

LOGS = getLogger(__name__)

os.system("pip install -U telethon")


print(f"""MAFIABOT IS ON!!! MAFIABOT VERSION :- {mafiaversion} YOUR 𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋 IS READY TO USE! FOR CHECK YOUR BOT WORKING OR NOT PLEASE TYPE (.alive/.ping) ENJOY YOUR BOT! JOIN FOR MORE FUTURE UPDATES @MafiaBot_Support .""")
async def humhai():
    await bot.send_file(
        LOGGER,
        
        caption=f"BOT IS START FOR FUCK GROUPS")
    except Exception as e:
        LOGS.info(str(e))

bot.loop.create_task(humhai())
if len(argv) not in (1, 3, 4):
    bot.disconnect()
else:
    bot.run_until_disconnected()
