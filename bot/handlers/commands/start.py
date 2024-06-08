from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.utils.markdown import hbold
from aiogram.utils.i18n import gettext as _

from bot.keyboards.default.main import main_menu_keyboard


router = Router()


@router.message(CommandStart())
async def start(message: types.Message) -> None:
    name = message.from_user.full_name
    company_name = hbold("Olive Garden")
    text = _("Assalomu alaykum {name}. Men {company} yetkazib berish xizmati botiman!\nПривет {name}! Я бот службы "
             "доставки {company}!".format(name=name, company=company_name))
    markup = main_menu_keyboard()

    await message.answer(text, reply_markup=markup, parse_mode=ParseMode.MARKDOWN)
