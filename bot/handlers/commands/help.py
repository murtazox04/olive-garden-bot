from aiogram import Router, types
from aiogram.filters import Command
from aiogram.utils.i18n import gettext as _

from bot.keyboards.default.main import main_menu_keyboard

router = Router()


@router.message(Command("help"))
async def cmd_help(message: types.Message) -> None:
    text = _(
        "Bot Olive Garden kafesining yetkazib berish hizmatini qulaylashtirish maqsadida "
        "ishlab chiqilgan. Ovqatga buyurtma qilish uchun /start bosing!"
    )
    markup = main_menu_keyboard()

    await message.answer(text, reply_markup=markup)
