#الامبراطور اليسع
import random
import re
import time
from platform import python_version
from datetime import datetime
from telethon import version
from telethon.errors.rpcerrorlist import (
    MediaEmptyError,
    WebpageCurlFailedError,
    WebpageMediaEmptyError,
)
from telethon.events import CallbackQuery
import requests

from ..Config import Config
from ..core.managers import edit_or_reply
from ..helpers.functions import check_data_base_heal_th, codalive, get_readable_time
from ..helpers.utils import reply_id
from ..sql_helper.globals import gvarstatus
from . import StartTime, codex, codversion, mention
from . import mention

plugin_category = "العروض"


@codex.cod_cmd(
    pattern="بنج$",
    command=("بنج", plugin_category),
    info={
        "header": "❂ :  لفحص بوت الأمبـراطور ",
        "usage": [
            "{tr}بنج",
        ],
    },
)
async def amireallyalive(event):
    "A kind of showing bot details"
    reply_to_id = await reply_id(event)
    uptime = await get_readable_time((time.time() - StartTime))
    _, check_sgnirts = check_data_base_heal_th()
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    ALIVE_TEXT = gvarstatus("ALIVE_TEXT") or "✮ -  بـوت  𝑨𝑴𝑩𝑹𝑶   يعمـل .. جيداً "
    COD_IMG = gvarstatus("ALIVE_PIC") or "https://telegra.ph/file/8822bd4624d64b4ab67cf.jpg" 
    if COD_IMG:
        A_IMG = [x for x in COD_IMG.split()]
        PIC = random.choice(A_IMG)
        cod_caption = f"**{ALIVE_TEXT}**\n\n"
        cod_caption += f"**{EMOJI} المستخدم : {mention}**\n"
        cod_caption += f"**{EMOJI} الوقت :** `{uptime}\n`"
        cod_caption += f"**{EMOJI} إصدار تليثيون :** `{version.__version__}\n`"
        cod_caption += f"**{EMOJI}إصدار 𝑨𝑴𝑩𝑹𝑶 :** `{codversion}`\n"
        cod_caption += f"**{EMOJI}  إصدار باثيون :** `{python_version()}\n`"
        cod_caption += f"**{EMOJI} قاعدة البيانات :** `{check_sgnirts}`\n"
        cod_caption += f"**{EMOJI} قناة السورس :** [𝗦𝗢𝗨𝗥𝗖𝗘𖢏𝗘𝗠𝗣𝗘𝗥𝗢𝗥](t.me/Mlze1bot) \n"
        try:
            await event.client.send_file(
                event.chat_id, PIC, caption=cod_caption, reply_to=reply_to_id
            )
            await event.delete()
        except (WebpageMediaEmptyError, MediaEmptyError, WebpageCurlFailedError):
            return await edit_or_reply(
                event,
                f"**Media Value Error!!**\n__Change the link by __`.setdv`\n\n**__Can't get media from this link :-**__ `{PIC}`",
            )
    else:
        await edit_or_reply(
            event,
            f"**{ALIVE_TEXT}**\n\n"
            f"**{EMOJI} المستخدم : {mention}**\n"
            f"**{EMOJI} الوقت :** `{uptime}\n`"
            f"**{EMOJI} إصدار تليثيون  :** `{version.__version__}\n`"
            f"**{EMOJI} إصدار 𝑨𝑴𝑩𝑹𝑶 :** `{codversion}`\n"
            f"**{EMOJI} إصدار باثيون :** `{python_version()}\n`"
            f"**{EMOJI}  قاعدة البيانات :** `{check_sgnirts}`\n"
            f"**{EMOJI} قناة السورس :** [𝗦𝗢𝗨𝗥𝗖𝗘𖢏𝗘𝗠𝗣𝗘𝗥𝗢𝗥](t.me/Mlze1bot) \n",
        )


@codex.cod_cmd(
    pattern="فحص$",
    command=("فحص", plugin_category),
    info={
        "header": "لـ عمل فحص للبوت أنه يعمل بنجاح ومفعل خاصية الانلاين ~~",
        "options": "To show media in this cmd you need to set ALIVE_PIC with media link, get this by replying the media by .tgm",
        "usage": [
            "{tr}فحص",
        ],
    },
)
async def amireallyalive(event):
    "نوع من عرض تفاصيل الروبوت بواسطة الروبوت المضمن الخاص بك"
    reply_to_id = await reply_id(event)
    EMOJI = gvarstatus("ALIVE_EMOJI") or "✧✧"
    cod_caption = f"**✮بـوت  𝑨𝑴𝑩𝑹𝑶   يعمـل .. جيداً**\n"
    cod_caption += f"**{EMOJI}  إصدار تليثيون :** `{version.__version__}\n`"
    cod_caption += f"**{EMOJI} إصدار 𝑨𝑴𝑩𝑹𝑶 :** `{codversion}`\n"
    cod_caption += f"**{EMOJI} إصدار باثيون :** `{python_version()}\n`"
    cod_caption += f"**{EMOJI} المستخدم:** {mention}\n"
    results = await event.client.inline_query(Config.TG_BOT_USERNAME, cod_caption)
    await results[0].click(event.chat_id, reply_to=reply_to_id, hide_via=True)
    await event.delete()


@codex.tgbot.on(CallbackQuery(data=re.compile(b"stats")))
async def on_plug_in_callback_query_handler(event):
    statstext = await codalive(StartTime)
    await event.answer(statstext, cache_time=0, alert=True)
