from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message

@Client.on_message(
    filters.command("inviteall", prefixes=["/", ".", "?", "-"])
    & ~ filters.edited & filters.outgoing
)
async def inv(client: Client, message: Message):
    text = message.text.split(" ", 1)
    queryy = text[1]
    chat = await client.get_chat("queryy")
    tgchat = message.chat
    await message.edit_text("inviting users")
    async for member in chat.iter_members():
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            await message.reply_text(f"error-   {e}")
