from pyrogram import Client, filters ,idle
from pyrogram.types import *
from pymongo import MongoClient
import requests
import os
import re


API_ID = os.environ.get("API_ID", None) 
API_HASH = os.environ.get("API_HASH", None) 
STRING_SESSION = os.environ.get("STRING_SESSION", None) 
KUKI_API = os.environ.get("KUKI_API", None) 
bot = Client(
    STRING_SESSION,
    api_id = API_ID,
    api_hash = API_HASH ,
)



@bot.on_message(
    filters.text
    & filters.reply
    & ~filters.private
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"https://kukiapi.xyz/api/message={msg}").json()

  moezilla = f"{Kuki['reply']}"

  self = await bot.get_me()
  bot_id = self.id
  if not message.reply_to_message.from_user.id == bot_id:
         return
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)


@bot.on_message(
    filters.text
    & ~filters.reply
    & filters.private
    & ~filters.bot
    & ~filters.edited,
    group=2,
)
async def kukiai(client: Client, message: Message):
  msg = message.text
  chat_id = message.chat.id

  Kuki =   requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}").json()

  moezilla = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)


@bot.on_message(
    filters.command("chat", prefixes=["/", ".", "?", "-"]))
async def kukiai(client: Client, message: Message):

  msg = message.text.replace(message.text.split(" ")[0], "")
    
  Kuki =   requests.get(f"https://kukiapi.xyz/api/apikey={KUKI_API}/message={msg}").json()

  moezilla = f"{Kuki['reply']}"
      
  await client.send_chat_action(message.chat.id, "typing")
  await message.reply_text(moezilla)






bot.run()

