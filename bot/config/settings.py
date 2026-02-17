import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
    TG_TOKEN = os.getenv("BOt_TOKEN")
    BOT_OWNER_ID = os.getenv("BOT_OWNER")

settings = Settings()
