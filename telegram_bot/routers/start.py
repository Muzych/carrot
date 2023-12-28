from aiogram import types, Router
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from filters.is_private import IsPrivateFilter

start_router = Router()
start_router.message.filter(IsPrivateFilter())


@start_router.message(CommandStart())
async def start_handler(message: types.Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")