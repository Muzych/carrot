import asyncio
from aiogram import Bot, types, Dispatcher
# from telegram_bot.settings import settings


token = "6761375042:AAFl9RliReL7mB4_7cGJU_qOMu0zcd_UhaU"
bot = Bot(token)
dp = Dispatcher()

@dp.message()
async def cmd_start(msg: types.Message):
    await msg.answer('Hello World!')



if __name__ == "__main__":
    asyncio.run(dp.start_polling(bot))
    