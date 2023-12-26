import os
import httpx
import uvicorn
from fastapi import FastAPI, Request
from routers import webhook
from dotenv import load_dotenv
from loguru import logger


load_dotenv()

app = FastAPI()
app.include_router(webhook.router)


@app.on_event("startup")
async def on_startup():
    logger.info("机器人启动...,开始设置webhook")
    # # await bot.set_webhook(url=WEBHOOK_URL)

    # # Register middlewares
    # dp.update.outer_middleware(ConfigMiddleware(config))

    # # Register routes
    # dp.include_router(start_router)
    pass


# @app.post(WEBHOOK_PATH)
# async def bot_webhook(update: dict):
#     # telegram_update = types.Update(**update)
#     # await dp.feed_update(bot=bot, update=telegram_update)
#     pass


@app.on_event("shutdown")
async def on_shutdown():
    # await bot.session.close()
    logger.info("机器人关闭...再见！")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
