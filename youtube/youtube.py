from os import path

from youtube_dl import YoutubeDL

from config import DURATION_LIMIT, BOT_NAME as BN
from helpers.errors import DurationLimitError

ydl_opts = {
    "format": "bestaudio/best",
    "geo-bypass": True,
    "nocheckcertificate": True,
    "outtmpl": "downloads/%(id)s.%(ext)s",
}
ydl = YoutubeDL(ydl_opts)


def download(url: str) -> str:
    info = ydl.extract_info(url, False)
    duration = round(info["duration"] / 60)

    if duration > DURATION_LIMIT:
        raise DurationLimitError(
            f"**{BN} :** Vɪᴅᴇᴏ ɪsLᴏɴɢᴇʀ Tʜᴀɴ {DURATION_LIMIT} ᴍɪɴᴜᴛᴇ(s) ᴀʀᴇɴ'ᴛ ᴀʟʟᴏᴡᴇᴅ, ᴛʜᴇ ᴘʀᴏᴠɪᴅᴇʀ ᴠɪᴅᴇᴏ ɪs {duration} ᴍɪɴᴜᴛᴇ(s)"
        )

    ydl.download([url])
    return path.join("downloads", f"{info['id']}.{info['ext']}")
