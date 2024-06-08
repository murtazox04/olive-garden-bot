from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def set_keyboard(data) -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    for category in data:
        builder.add(KeyboardButton(text=category["name"])).adjust(2)
    builder.row(
        KeyboardButton(text="Back"),
        width=1
    )

    return builder.as_markup(resize_keyboard=True)
