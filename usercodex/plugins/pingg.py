# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.

import os
from datetime import datetime
from platform import python_version
#
from . import hmention, reply_id



AMBRA = gvarstatus("C_AMBRA") or "فحص"
PING_PIC = os.environ.get("PING_PIC") or (
    "https://telegra.ph/file/8822bd4624d64b4ab67cf.jpg"
)

JM_TXT = os.environ.get("PING_TEXT") or "...{وَتَوَكَّلْ عَلَى اللَّهِ ۚ وَكَفَىٰ بِاللَّهِ وَكِيلًا}"


@codex.cod_cmd(pattern=f"{AMBRA}$")
async def _(event):
    reply_to_id = await reply_id(event)
    start = datetime.now()
    roz = await edit_or_reply(
        event, "<b><i>روبوت ۞  𝐄𝐌𝐏𝐄𝐑𝐎𝐑 ۞ يعمل جيداً.... </b></i>", "html"
    )
    end = datetime.now()
    await roz.delete()
    ms = (end - start).microseconds / 1000
    if PING_PIC:
        caption = f"<b><i>{JM_TXT}<i><b>\n<code>⊢===>===™𓅓™==<===⊣\n┃ ❂ {ms}\n┃ ❂ <b>{hmention}</b>\n ⊢===>===™𓅓™==<===⊣ "
        await event.client.send_file(
            event.chat_id,
            PING_PIC,
            caption=caption,
            parse_mode="html",
            reply_to=reply_to_id,
            link_preview=False,
            allow_cache=True,
        )
    else:
        await event.edit_or_reply(
            event, "<code>يجـب اضـافة متـغير `PING_PIC`  اولا  f<code>", "html"
        )


# Ayra - UserBot
# Copyright (C) 2021-2022 senpai80
#
# This file is a part of < https://github.com/senpai80/Ayra/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/senpai80/Ayra/blob/main/LICENSE/>.


