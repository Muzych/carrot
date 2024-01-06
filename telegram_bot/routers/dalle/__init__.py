import google.generativeai as genai
from BingImageCreator import ImageGen

from aiogram import types, Router
from aiogram.filters import Command
from filters.is_private import IsPrivateFilter
from logger import watcher

dalle_router = Router()
dalle_router.message.filter(IsPrivateFilter())

@dalle_router.message(Command("dalle"))
async def dalle_handler(message: types.Message) -> None:
    watcher.info("参数加载完成，开始调用dalle服务")
    await message.answer(f"This is dalle. Welcome to drawing world.")