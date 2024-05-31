from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

fake_menus = [
    {"title": "🍴 Menu"},
    {"title": "🛍 Orders"},
    {"title": "✍️ Feedback"},
    {"title": "⚙️ Settings"},
]


def main_menu_keyboard(menus=None) -> ReplyKeyboardMarkup:
    """
    Creates a main menu keyboard with the specified menu options.
    :param menus: List of menu options (default: fake_menus)
    :return: ReplyKeyboardMarkup
    """
    if menus is None:
        menus = fake_menus
    builder = ReplyKeyboardBuilder()
    for menu in menus:
        builder.add(KeyboardButton(text=menu["title"])).adjust(2)

    return builder.as_markup(resize_keyboard=True)
