import os
import asyncio
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest


load_dotenv('config.env')

API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')

client = TelegramClient('session', API_ID, API_HASH)


def stylize(text):
    normal = "0123456789:"
    fonts = {
        "bold":            "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗:",
        "outlined":        "⓪①②③④⑤⑥⑦⑧⑨:",
        "double_struck":   "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡:",
        "fullwidth":       "０１２３４５６７８９:",
        "sans_serif_bold": "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵:",
        "monospace":       "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿:",
        "normal":          "0123456789:",
    }
    selected = fonts.get(os.getenv('SELECTED', 'normal'), normal)
    table = {ord(n): s for n, s in zip(normal, selected)}
    return text.translate(table)

async def update_last_name():
   # print("Connecting...")
    await client.start()
   # print("Connected! bot started.\n")

    while True:
        # timezone
        TIMEZONE = os.getenv('TIMEZONE')
        if TIMEZONE == "":
            now = datetime.now()
        else: 
            now = datetime.now(ZoneInfo(TIMEZONE))
        # format of clock
        last_name = stylize(f"{now.strftime('%H:%M')}")

        try:
            await client(UpdateProfileRequest(last_name=last_name))
            #print(f"\r updated! ← {last_name}", end="")
        except Exception as e:
            print(f"❌ Error!!! {e}")

       
        seconds_to_wait = 60 - now.second
        await asyncio.sleep(seconds_to_wait)

with client:
    client.loop.run_until_complete(update_last_name())
