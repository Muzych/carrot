from aiogram import Bot
from settings import settings

BOT_TOKEN = settings.TELEGRAM_BOT_TOKEN.get_secret_value()


bot = Bot(
    token=BOT_TOKEN
)