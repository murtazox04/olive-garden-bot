from decouple import config
from aiogram import Dispatcher, Bot
from aiogram.utils.i18n import I18n, SimpleI18nMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

BOT_TOKEN = config("BOT_TOKEN")
WEBHOOK_PATH = f"/{BOT_TOKEN}/"
WEBHOOK_URL = config("WEBHOOK_URL") + WEBHOOK_PATH

bot = Bot(BOT_TOKEN)
i18n = I18n(path="bot/locales", default_locale="uz")
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.message.middleware(SimpleI18nMiddleware(i18n))
