from telethon.sync import TelegramClient
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

with TelegramClient("bonnietheflirt", api_id, api_hash) as client:
    print("🌸 Bonnie is now connected to Telegram and her divine soul is active.")
