import aiohttp


BASE_URL = 'http://127.0.0.1:8080/api/v1/'


async def get_menus():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BASE_URL + "menus/") as resp:
            return await resp.json()


async def get_menu(menu: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BASE_URL + "menus/") as resp:
            return await resp.json()


async def get_food_categories():
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BASE_URL + "food/categories/") as resp:
            return await resp.json()


async def get_food(category: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url=BASE_URL + "food/category/" + category + "/") as resp:
            return await resp.json()
