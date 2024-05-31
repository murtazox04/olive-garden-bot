from aiogram.enums import ParseMode
from aiogram import Router, types, F
from aiogram.utils.markdown import hbold
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from loader import bot
from bot.keyboards.default.category import category_keyboard


router = Router()


@router.message()
async def menu(message: types.Message, state: FSMContext):
    message_text = message.text
    print(message_text)
    if message_text == _("🍴 Menu"):
        text = _("Please choose one of the options:")
        markup = category_keyboard()

        await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=markup)
        await state.set_state("set_category")
    elif message_text == _("🛍 Orders"):
        ...
    elif message_text == _("✍️️ Feedback"):
        ...
    elif message_text == _("⚙️ Settings"):
        ...


@router.message(F.state == "set_category")
async def set_category(message: types.Message, state: FSMContext):
    category = message.text
