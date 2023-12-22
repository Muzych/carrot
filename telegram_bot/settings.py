from pydantic import SecretStr
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_BOT_TOKEN: SecretStr

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"

settings = Settings()