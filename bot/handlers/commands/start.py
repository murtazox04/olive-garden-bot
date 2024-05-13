from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.utils.i18n import gettext as _

from bot.keyboards.default.main import main_menu_keyboard


router = Router()


@router.message(CommandStart())
async def start(message: types.Message) -> None:
    text = _("Assalomu alaykum!\nPastdagi menulardan birini tanlang.")
    markup = main_menu_keyboard()

    await message.answer(text, reply_markup=markup)
