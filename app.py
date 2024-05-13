from aiogram import Dispatcher,  types

from loader import app, bot, dp, WEBHOOK_PATH, WEBHOOK_URL
from bot.handlers.commands import router as commands_router


@app.on_event("startup")
async def on_startup() -> None:
    print("1111111111")
    dp.include_router(commands_router)
    url = await bot.get_webhook_info()
    print(url)

    if url != WEBHOOK_URL:
        print("3333333")
        await bot.set_webhook(
            url=WEBHOOK_URL
        )


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict) -> None:
    telegram_update = types.Update(**update)
    await Dispatcher._feed_webhook_update(
        self=dp,
        bot=bot,
        update=telegram_update
    )


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await bot.delete_webhook()
    await dp.storage.close()
