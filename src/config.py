from os import getenv
from dotenv import load_dotenv

load_dotenv()


"""Telegram config"""
TELEGRAM_BOT_TOKEN = getenv("TELEGRAM_BOT_TOKEN")
BOTHOST = getenv("BOTHOST")  # only required in prod environment, used to set webhook