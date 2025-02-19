import os


class Config:
    TELEGRAM_TOKEN = os.getenv("")
    PORT = os.getenv("TELEGRAM_BOT_PORT", 5000)
    TELEGRAM_API = "https://api.telegram.org"
    OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")
    TELEGRAM_CORE_API_HASH = os.getenv("TELEGRAM_CORE_API_HASH")
    TELEGRAM_CORE_API_ID = os.getenv("TELEGRAM_CORE_API_ID")

