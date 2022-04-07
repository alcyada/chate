from pyrogram import Client, filters ,idle
from pyrogram.types import *
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
    plugins=dict(root="handlers")
)






bot.run()


