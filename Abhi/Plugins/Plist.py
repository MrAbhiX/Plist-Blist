import os
import asyncio
from telethon.errors import ChatAdminRequiredError
from Abhi.utils import admin_cmd, sudo_cmd
from Abhi import bot, LOGGER


@bot.on(admin_cmd(pattern=r"plist ?(.*)", outgoing=True))
@bot.on(sudo_cmd(pattern=r"plist ?(.*)", allow_sudo=True))
async def get_users(show):
    await show.delete()
    if not show.text[0].isalpha() and show.text[0] not in ("/"):
        if not show.is_group:
            await show.edit("Are you sure this is a group?")
            return
        info = await show.client.get_entity(show.chat_id)
        title = info.title if info.title else "this chat"
        mentions = "id,reason"
        try:
            if not show.pattern_match.group(1):
                async for user in show.client.iter_participants(show.chat_id):
                    if not user.deleted and user.id != bot.uid:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
                    elif user.id != bot.uid:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
            else:
                searchq = show.pattern_match.group(1)
                async for user in show.client.iter_participants(
                    show.chat_id, search=f"{searchq}"
                ):
                    if not user.deleted and user.id != bot.uid:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
                    elif user.id != bot.uid:
                        mentions += f"\n{user.id},⚠️Porn / Porn Group Member//AntiPornFed #Massban🔞🛑"
        except ChatAdminRequiredError as err:
            mentions += " " + str(err) + "\n"
        file = open("userslist.csv", "w+")
        file.write(mentions)
        file.close()
        await show.client.send_file(
            BOTLOG_CHATID,
            "userslist.csv",
            caption="Group Members in {}".format(title),
            reply_to=show.id,
        )
