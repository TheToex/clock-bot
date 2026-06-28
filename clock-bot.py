import asyncio
from datetime import datetime
from telethon import TelegramClient
from telethon.tl.functions.account import UpdateProfileRequest

# ===========================================================
# enter your informations here (from https://my.telegram.org)
# ===========================================================
API_ID   =      #from https://my.telegram.org
API_HASH = '' #from https://my.telegram.org
# ===========================================================

client = TelegramClient('session', API_ID, API_HASH)

async def update_last_name():
    print("Connecting...")
    await client.start()
    print("Connected! bot started.\n")

    while True:
        now = datetime.now()

        #format of clock
        last_name = f"{now.strftime('%H:%M')}"

        try:
            await client(UpdateProfileRequest(last_name=last_name))
            print(f"updated! ← {last_name}")
        except Exception as e:
            print(f"❌ Error!!! {e}")

       
        seconds_to_wait = 60 - datetime.now().second
        await asyncio.sleep(seconds_to_wait)

with client:
    client.loop.run_until_complete(update_last_name())