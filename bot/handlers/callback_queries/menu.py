from aiogram.enums import ParseMode
from aiogram import Router, types, F
from aiogram.fsm.context import FSMContext
from aiogram.utils.i18n import gettext as _

from services.api.food import FoodService
from services.api.order import OrderService
from bot.keyboards.default.food import set_keyboard
from bot.keyboards.inline.order import set_order

router = Router()
food_service = FoodService()
order_service = OrderService()


@router.message()
async def menu(message: types.Message, state: FSMContext):
    message_text = message.text
    print(message_text)
    if message_text == _("🍴 Menu"):
        text = _("Please choose one of the options:")
        categories = await food_service.get_categories()
        markup = set_keyboard(categories)

        await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=markup)
        await state.set_state("set_category")
    elif message_text == _("🛍 Orders"):
        text = _("Order text")
        order = await order_service.get_order(...)

        await message.answer(...)
    elif message_text == _("✍️️ Feedback"):
        ...
    elif message_text == _("⚙️ Settings"):
        ...


@router.message(F.state == "set_category")
async def set_category(message: types.Message, state: FSMContext):
    category = message.text
    data = await food_service.get_category(category)
    if await food_service.check_child_category(data):
        text = _("Please choose one of the options:")
        markup = set_keyboard(data)
        await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=markup)
        await state.set_state("set_category")
    else:
        text = _("Please choose one of the foods:")
        data = await food_service.get_foods()
        markup = set_keyboard(data)
        await message.answer(text, parse_mode=ParseMode.MARKDOWN, reply_markup=markup)
        await state.set_state("set_food")


@router.message(F.state == "set_food")
async def set_food(message: types.Message, state: FSMContext):
    food = message.text
    data = await food_service.get_food(food)
    image = data['image']
    text = _(
        "{name}\n{category}\n{price}\n{description}".format(
            name=data['name'], category=data['category'], price=data['price'], description=data['description']
        )
    )
    markup = set_order(data['id'])

    await message.answer_photo(
        photo=image,
        caption=text,
        reply_markup=markup,
        parse_mode=ParseMode.MARKDOWN
    )
