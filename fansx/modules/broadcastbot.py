
import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message
from fansx.core.helpers.msg_type import ReplyCheck
from fansx.core.database import get_list_from_vars
from fansx import *

@ubot.on_message(filters.command("unprem") & filters.me)
async def jwbsalamlngkp(client: Client, message: Message):
    await asyncio.gather(
        message.delete(),
        client.send_message(
            message.chat.id,
            "ᴍᴀsᴜᴋᴀɴ ɪᴅ / ᴜsᴇʀɴᴀᴍᴇ ᴘᴇɴɢɢᴜɴᴀ",
            reply_to_message_id=ReplyCheck(message),
        ),
    )

__MODULE__ = "ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ"
__HELP__ = f"""
<b>⦪ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʀᴏᴀᴅᴄᴀsᴛ ʙᴏᴛ ⦫</b>

<blockquote><b>⎆ perintah : <code>/ʙᴄ</code>
ᚗ  ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇɴɢɪʀɪᴍ ᴘᴇsᴀɴ ᴋᴇ sᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ ᴜsᴇʀʙᴏᴛ ʟᴇᴡᴀᴛ ʙᴏᴛ
"""

@PY.BOT("bc")
@PY.OWNER
async def broadcast_bot(client, message):
    msg = await message.reply(
        "<b>⌭ SEDANG DIPROSES TUNGGU SEBENTAR</b>",
        quote=True
    )

    if not message.reply_to_message:
        return await msg.edit("<b>⌭ MOHON BALAS PESAN</b>")

    done = 0
    failed = 0

    users = await get_list_from_vars(client.me.id, "SAVED_USERS")

    for user_id in users:
        try:
            await message.reply_to_message.forward(user_id)
            done += 1
        except Exception:
            failed += 1

    return await msg.edit(
        f"""
        <blockquote><b>✓ BROADCAST SELESAI</b>
        <b>✓ TERKIRIM :</b> <code>{done}</code><br>
        <b>✗ GAGAL :</b> <code>{failed}</code></blockquote>
        """,
        
            parse_mode=ParseMode.HTML
    )
