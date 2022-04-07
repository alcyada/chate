from pyrogram import Client, filters
from main import KUKI_API
from pyrogram.types import Message
import requests
import re

@Client.on_message(
    filters.text & filters.incoming
    & filters.reply
    & filters.group
    & ~filters.private
    & ~filters.bot
    & ~filters.edited,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}")
  print(Kuki)
  Kuki= Kuki.json
  print(Kuki)
  moezilla = f"{Kuki['reply']}"

  self = await Client.get_me()
  bot_id = self.id
  if not message.reply_to_message.from_user.id == bot_id:
         return
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)


@Client.on_message(
    filters.text & filters.incoming
    & ~filters.reply
    & filters.private
    & ~filters.bot
    & ~filters.edited,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}").json()
  print(Kuki)
  Kuki= Kuki.json
  print(Kuki)
  moezilla = f"{Kuki['reply']}"
     
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)

@Client.on_message(
    filters.command("chat", prefixes=["/", ".", "?", "-"]))
async def kukiai(client: Client, message: Message):

  msg = message.text.replace(message.text.split(" ")[0], "")
    
  Kuki =   requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}").json()
  print(Kuki)
  Kuki= Kuki.json
  print(Kuki)
  moezilla = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)
