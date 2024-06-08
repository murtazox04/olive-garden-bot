from aiogram.enums import ParseMode
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from services.api.food import FoodService
from services.api.order import OrderService
from bot.keyboards.default.food import set_keyboard
from bot.callbacks.order import SetOrdering, OrderingStatus

router = Router()
order_service = OrderService()


@router.callback_query(SetOrdering)
async def set_order(call: SetOrdering):
    status = call.status
    if status == OrderingStatus.CART:
        ...
    elif status == OrderingStatus.BUY:
        ...
