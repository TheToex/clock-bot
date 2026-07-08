import os
from telethon import TelegramClient
from dotenv import load_dotenv


GREEN = "\033[32m"
RESET = "\033[0m"
if not os.path.exists('config.env'):
    print("from https://my.telegram.org")
    api_id   = input("API_ID: ")
    api_hash = input("API_HASH: ")
    print(f"{GREEN}FONTS: bold , outlined , double_struck , fullwidth , sans_serif_bold , monospace{RESET}")
    font = input("Select Font: (leave empty to use normal font) ")
    timezone = input("TimeZone: set timezone like: Europe/Rome or etc... (leave empty to use your system time) ")
    with open('config.env', 'w') as f:
        f.write(f"API_ID={api_id}\nAPI_HASH={api_hash}\nSELECTED={font}\nTIMEZONE={timezone}\n")
    load_dotenv('config.env')

load_dotenv('config.env')


API_ID = int(os.getenv('API_ID'))
API_HASH = os.getenv('API_HASH')

client = TelegramClient('session', API_ID, API_HASH)
client.start()