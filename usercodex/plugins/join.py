from telethon import events

from usercodex import Config, codex

from ..core.session import group_call_factory

group_call = group_call_factory.start(xedoc)


@codex.cod_cmd(events.NewMessage(from_user=Config.OWNER_ID, pattern=r"^/join$"))
async def join_handler(event):
    chat = await event.get_chat()
    await group_call.start(xedoc.chat_id, chat.id)
