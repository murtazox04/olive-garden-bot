from fastapi import FastAPI
from aiogram import types
from contextlib import asynccontextmanager

from loader import bot, dp, WEBHOOK_PATH, WEBHOOK_URL
from bot.handlers.commands import router as commands_router
from bot.handlers.callback_queries import router as callback_queries_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    dp.include_router(commands_router)
    dp.include_router(callback_queries_router)
    url = await bot.get_webhook_info()
    if url.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)

    yield  # The application will run here

    # Shutdown
    await bot.delete_webhook()
    await dp.storage.close()
    await bot.session.close()  # Ensure the aiohttp session is closed


app = FastAPI(title="Olive Garden Delivery Bot", lifespan=lifespan)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    await dp.feed_update(bot, telegram_update)
    return {"status": "ok"}
