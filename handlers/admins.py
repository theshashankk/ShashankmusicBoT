import queue

from pyrogram import Client
from pyrogram.types import Message

import callsmusic

import queues
import cache.admins

from config import BOT_NAME as BN
from helpers.filters import command
from helpers.wrappers import errors, admins_only


@Client.on_message(command(["pause", "p"]))
@errors
@admins_only
async def pause(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text(f"**{BN} :**❕ Nᴏᴛʜɪɴɢ Is Pʟᴀʏɪɴɢ.")
    else:
        callsmusic.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text(f"**{BN} :** ⏸ Pᴀᴜsᴇᴅ.")


@Client.on_message(command(["resume", "r"]))
@errors
@admins_only
async def resume(_, message: Message):
    if (
            message.chat.id not in callsmusic.pytgcalls.active_calls
    ) or (
            callsmusic.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text(f"**{BN} :**❕ Nᴏᴛʜɪɴɢ Is Pʟᴀʏɪɴɢ.")
    else:
        callsmusic.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text(f"**{BN} :** ▶️ Rᴇsᴜᴍᴇᴅ.")


@Client.on_message(command(["end", "s"]))
@errors
@admins_only
async def stop(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :**❕ Nᴏᴛʜɪɴɢ ɪs Sᴛʀᴇᴀᴍɪɴɢ.")
    else:
        try:
            queues.clear(message.chat.id)
        except queue.Empty:
            pass

        callsmusic.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text(f"**{BN} :** ⏹ Sᴛᴏᴘᴘᴇᴅ Sᴛʀᴇᴀᴍɪɴɢ.")


@Client.on_message(command(["skip", "next"]))
@errors
@admins_only
async def skip(_, message: Message):
    if message.chat.id not in callsmusic.pytgcalls.active_calls:
        await message.reply_text(f"**{BN} :**❕ Nᴏᴛʜɪɴɢ Is Pʟᴀʏɪɴɢ Tᴏ Sᴋɪᴘ.")
    else:
        queues.task_done(message.chat.id)

        if queues.is_empty(message.chat.id):
            callsmusic.pytgcalls.leave_group_call(message.chat.id)
        else:
            callsmusic.pytgcalls.change_stream(message.chat.id, queues.get(message.chat.id)["file_path"])

        await message.reply_text(f"**{BN} :** ⏩ Sᴋɪᴘᴘᴇᴅ Tʜᴇ Cᴜʀʀᴇɴᴛ Sᴏɴɢ.")


@Client.on_message(command("admincache"))
@errors
@admins_only
async def admincache(_, message: Message):
    cache.admins.set(
        message.chat.id,
        [member.user for member in await message.chat.get_members(filter="administrators")]
    )
    await message.reply_text(f"**{BN} :** ❇ Aᴅᴍɪɴ ᴄᴀᴄʜᴇ Rᴇғʀᴇsʜ!")
