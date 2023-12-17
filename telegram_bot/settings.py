from pydantic import BaseSettings, SecretStr

class Settings(BaseSettings):
    TELEGRAM_BOT_API_TOKEN: SecretStr

    class Config:
        env_file = "../.env"
        env_file_encoding = "utf-8"