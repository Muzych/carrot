from pydantic import SecretStr
from pydantic_settings import BaseSettings
from urllib.parse import urlparse
from typing import Optional
from aiogram.fsm.storage.redis import RedisStorage
from dataclasses import dataclass


class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: SecretStr
    REDIS_URL: Optional[str] = ""

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"


settings = Settings()
dispatcher_storage = RedisStorage.from_url(url=settings.REDIS_URL)
