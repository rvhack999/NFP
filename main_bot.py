import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

token = '7061711131:AAEP23Laa8is4ymvsABVmM0X20N198Xu4KM'

bot = Bot(token=token)

dp = Dispatcher()


@dp.message(CommandStart())
async def get_message(message: types.Message):
    chat_id = message.chat.id
    text = f'Привет {message.from_user.full_name}'
    await bot.send_message(chat_id, text)


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(token, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())