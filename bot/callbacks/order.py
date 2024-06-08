from enum import Enum
from aiogram.filters.callback_data import CallbackData


class OrderingStatus(Enum):
    BUY = "buy"
    CART = "cart"


class SetOrdering(CallbackData, prefix="order"):
    food_id: int
    status: OrderingStatus
