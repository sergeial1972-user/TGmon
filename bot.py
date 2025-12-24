#imports
import os
import asyncio
from dotenv import load_dotenv
import logging
import  hostmanager












#aiogram imports
from aiogram import types, Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, message
from bot_ext.handlers import router as handlers_router
from bot_ext.host_managment import router as host_managment_router

#dotenv
load_dotenv()




#bot
bot_token = os.getenv("BOT_TOKEN")
bot = Bot(token=bot_token)
dp = Dispatcher()

async def main():
    dp.include_router(handlers_router)
    dp.include_router(host_managment_router)

    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())










































