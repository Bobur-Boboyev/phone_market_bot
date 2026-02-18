import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    TG_TOKEN = os.getenv("BOt_TOKEN")
    OWNER_ID = os.getenv("OWNER_ID")


settings = Settings()
