from pyrogram import Client , filters
import asyncio
from pyrogram.types import Message

@Client.on_message(
    filters.command("gbr")
    & ~ filters.edited & filters.outgoing
)
async def gbrd(client: Client, message: Message):
    text = message.text.split(" ", 1)
    queryy = text[1]
    zxz = ["channel", "supergroup"]
    async for dialog in client.iter_dialogs():
            if dialog.chat.type in zxz:
              try:
                x = await client.send_message(dialog.chat.id, queryy )
                asyncio.sleep(3)
              except Exception as e:
                message.reply_text(f"[Broadcast] {dialog.chat.id} {e}")

@Client.on_message(
    filters.command("br")
    & ~ filters.edited & filters.outgoing
)
async def gbrd(client: Client, message: Message):
    text = message.text.split(" ", 1)
    queryy = text[1]
    async for dialog in client.iter_dialogs():
          try:
                x = await client.send_message(dialog.chat.id, queryy )
                asyncio.sleep(3)
          except Exception as e:
            message.reply_text(f"[Broadcast] {dialog.chat.id} {e}")
