#سورس#الامبراطور 
#تعريب#الامبراطور#اليسع
import json

import requests

from ..sql_helper.globals import gvarstatus
from . import codex, edit_delete, edit_or_reply

plugin_category = "extra"


@codex.cod_cmd(
    pattern="اذان(?:\s|$)([\s\S]*)",
    command=("اذان", plugin_category),
    info={
        "header": "يظهر لك أوقات الصلاة الإسلامية لاسم المدينة المحدد.",
        "note": "you can set default city by using {tr}setcity command.",
        "usage": "{tr}اذان <اسم المدينه>",
        "examples": "{tr}اذان عدن",
    },
)
async def get_adzan(adzan):
    "يظهر لك أوقات الصلاة الإسلامية لاسم المدينة المحدد"
    input_str = adzan.pattern_match.group(1)
    LOKASI = gvarstatus("DEFCITY") or "Delhi" if not input_str else input_str
    url = f"http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    request = requests.get(url)
    if request.status_code != 200:
        return await edit_delete(
            adzan, f"`Couldn't fetch any data about the city {LOKASI}`", 5
        )
    result = json.loads(request.text)
    codresult = f"<b>**❒:أوقات الصلوات الإسلامية ** </b>\
            \n\n<b>**❂:مدينة**  : </b><i>{result['query']}</i>\
            \n<b>**❂:لدولة**   : </b><i>{result['country']}</i>\
            \n<b>**❂:التاريخ**  : </b><i>{result['items'][0]['date_for']}</i>\
            \n<b>**❂:الفجر**  : </b><i>{result['items'][0]['fajr']}</i>\
            \n<b>**❂:االصباح*  : </b><i>{result['items'][0]['shurooq']}</i>\
            \n<b>**❂:الضهر**  : </b><i>{result['items'][0]['dhuhr']}</i>\
            \n<b>**❂:العصر**  : </b><i>{result['items'][0]['asr']}</i>\
            \n<b>**❂:المغرب** : </b><i>{result['items'][0]['maghrib']}</i>\
            \n<b>**❂:الفجر**  : </b><i>{result['items'][0]['isha']}</i>\
    "
    await edit_or_reply(adzan, codresult, "html")
