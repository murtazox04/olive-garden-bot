from aiogram.utils.i18n import gettext as _
from aiogram.utils.keyboard import InlineKeyboardBuilder

from bot.callbacks.order import SetOrdering, OrderingStatus


def set_order(food_id: int):
    builder = InlineKeyboardBuilder()

    builder.button(
        text=_("Add to Cart"),
        callback_data=SetOrdering(
            status=OrderingStatus.CART,
            food_id=food_id
        ).pack()
    ).adjust(2)
    builder.button(
        text=_("Order now"),
        callback_data=SetOrdering(
            status=OrderingStatus.BUY,
            food_id=food_id
        ).pack()
    ).adjust(2)
    builder.button(
        text=_("Main menu"),
        callback_data="main_menu"
    ).adjust(1)

    return builder.as_markup()


def buy_order(buying_url: str, price: float):
    builder = InlineKeyboardBuilder()
    builder.button(
        text=_("Pay: {price} sum".format(price=price)),
    )

    return builder.as_markup()



