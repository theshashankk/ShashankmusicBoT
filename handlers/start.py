from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import command, other_filters, other_filters2


@Client.on_message(command("start") & other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""🙃 Hᴇʏ Nᴜʙ {message.from_user.first_name}!
✨ I ᴀᴍ sᴘᴇᴄɪᴀʟ ᴍᴜsɪᴄ ʙᴏᴛ. 
🥳 I ᴄᴀɴ ᴘʟᴀʏ ᴍᴜsɪᴄ ɪɴ ʏᴏᴜʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ😉
⚜️ Usᴇ ᴛʜᴇsᴇ ʙᴜᴛᴛᴏɴs ʙᴇʟᴏᴡ ᴛᴏ ᴋɴᴏᴡ ᴍᴏʀᴇ. 👇""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚒ sᴏᴜʀᴄᴇ ᴄᴏᴅᴇ", url="https://github.com/theshashankk/ShashankmusicBoT"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💻 Nᴜʙ ᴄʀᴇᴀᴛᴏʀ", url="https://t.me/Theshashank"
                    ),
                    InlineKeyboardButton(
                        "ᴄʀᴇᴀᴛᴏʀ ᴋɪ ᴊᴀɴᴇᴍᴏɴ❤️", url="https://t.me/cutie1145"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Aᴅᴅ ʙᴏᴛ ɪɴ ᴜʀ ɢʀᴏᴜᴘ🎵", url="t.me/Theshashank_musicRobot?startgroup=true"
                    )
                ]
            ]
        )
    )


@Client.on_message(command("start") & other_filters)
async def start2(_, message: Message):
    await message.reply_text(
        "**Nᴜʙ Isʜɪᴋᴀ:** I'M Wᴏʀᴋɪɴɢ!!!\nUsᴇ ᴍᴇ ɪɴ ɪɴʟɪɴᴇ ᴛᴏ sᴇᴀʀᴄʜ ғᴏʀ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ/Mᴜsɪᴄ. \n**Hᴀᴘᴘʏ sᴛʀᴇᴀᴍɪɴɢ**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🎶 Sᴇᴀʀᴄʜ 🎶", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "❌ Cʟᴏsᴇ ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
