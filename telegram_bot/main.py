import os
import httpx
import uvicorn
from fastapi import FastAPI, Request
from logger import CarrotLogger, watcher
from settings import settings
from pathlib import Path
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage

from routers.start import start_router
from routers.dalle import dalle_router

storage = MemoryStorage()

WEBHOOK_PATH = f"/bot/{settings.TELEGRAM_BOT_TOKEN.get_secret_value()}"
WEBHOOK_URL = "https://90f1-74-48-170-175.ngrok-free.app" + WEBHOOK_PATH


def create_app() -> FastAPI:
    app = FastAPI(debug=True)
    config_path = Path(settings.LOGGING_CONFIG)
    logger = CarrotLogger.make_logger(config_path)
    app.logger = logger
    return app


app = create_app()
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN.get_secret_value(), parse_mode="HTML")
dp = Dispatcher(storage=storage)


@app.on_event("startup")
async def on_startup():
    watcher.info("机器人启动...,开始设置webhook")
    await bot.set_webhook(url=WEBHOOK_URL)
    watcher.info("webhook设置完成！")
    dp.include_router(start_router)
    dp.include_router(dalle_router)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot=bot, update=telegram_update)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.session.close()
    watcher.info("机器人关闭...再见！")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
