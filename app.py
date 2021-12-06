import asyncio

from aiogram import executor

from config import admin_id
from loader import bot


async def on_shutdown(dp):
    await bot.close()


async def on_startup(dp):
    await bot.send_message(admin_id, "Bot ishga tushdi!")


if __name__ == '__main__':
    from handlers import dp

    executor.start_polling(dp, on_shutdown=on_shutdown, on_startup=on_startup)