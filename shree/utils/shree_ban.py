from pyrogram import filters
from pyrogram.enums import ChatMemberStatus
from shree import app

async def admin_check(_, __, message):
    if message.chat.type == "private":
        return True
    user_id = message.from_user.id
    chat_id = message.chat.id
    member = await app.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.OWNER]

admin_filter = filters.create(admin_check) 