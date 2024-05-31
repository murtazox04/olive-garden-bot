from fastapi import FastAPI
from aiogram import Dispatcher, types
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
    print(url)
    if url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)

    yield

    # Shutdown
    await bot.delete_webhook()
    await dp.storage.close()


app = FastAPI(title="Olive Garden Delivery Bot", lifespan=lifespan)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict) -> None:
    telegram_update = types.Update(**update)
    await Dispatcher._feed_webhook_update(
        self=dp,
        bot=bot,
        update=telegram_update
    )
