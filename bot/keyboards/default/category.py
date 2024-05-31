from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

fake_data = [
    {"title": "Category 1"},
    {"title": "Category 2"},
    {"title": "Category 3"},
    {"title": "Category 4"},
    {"title": "Category 5"},
    {"title": "Category 6"},
    {"title": "Category 7"},
    {"title": "Category 8"},
    {"title": "Category 9"},
]


def category_keyboard(data=None) -> ReplyKeyboardMarkup:
    if data is None:
        data = fake_data
    builder = ReplyKeyboardBuilder()
    for category in data:
        builder.add(KeyboardButton(text=category["title"])).adjust(2)
    builder.row(
        KeyboardButton(text="Back"),
        width=1
    )

    return builder.as_markup(resize_keyboard=True)
