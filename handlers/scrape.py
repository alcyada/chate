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
    chat = await client.get_chat(queryy)
    tgchat = message.chat
    await message.edit_text(f"inviting users from {chat.username}")
    async for member in client.iter_chat_members(chat.id):
        user= member.user
        zxb= ["online", "offline" , "recently", "within_week"]
        if user.status in zxb:
           try:
            await client.add_chat_members(tgchat.id, user.id)
           except Exception as e:
            mg= await client.send_message("me", f"error-   {e}")
            await asyncio.sleep(0.3)
            mg.delete()
