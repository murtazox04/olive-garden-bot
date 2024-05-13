from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton


def main_menu_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(
        text="🍴 Menu",
    ).adjust(1, True)
    builder.button(
        text="🛍 Orders"
    ).adjust(1, True)
    builder.row(
        KeyboardButton(text="✍️ Feedback"),
        KeyboardButton(text="⚙️ Settings"),
        width=2
    )
    return builder.as_markup(resize_keyboard=True)
