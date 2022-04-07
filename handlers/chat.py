from pyrogram import Client, filters
from main import KUKI_API
from pyrogram.types import Message
import requests
import re
import json

@Client.on_message(
    filters.reply
    & ~filters.edited & filters.group
)
async def kukiii(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"http://3.15.240.35:82/chatbot/{msg}")
  print(Kuki.text)
  Kuki= json.loads(Kuki.text)
  print(Kuki)
  moezilla = f"{Kuki['query']}"

  self = await client.get_me()
  bot_id = self.id
  if not message.reply_to_message.from_user.id == bot_id:
         return
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)


@Client.on_message(filters.private )
async def kukiaii(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"http://3.15.240.35:82/chatbot/{msg}")
  print(Kuki.text)
  Kuki= json.loads(Kuki.text)
  print(Kuki)
  moezilla = f"{Kuki['query']}"
     
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)

@Client.on_message(
    filters.command("chat", prefixes=["/", ".", "?", "-"]))
async def kukiai(client: Client, message: Message):

  msg = message.text.split(" ", 1)
  msg = msg[1]
  print(msg)
  Kuki =   requests.get(f"http://3.15.240.35:82/chatbot/{msg}")
  print(Kuki.text)
  Kuki= json.loads(Kuki.text)
  print(Kuki)
  moezilla = f"{Kuki['query']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)
