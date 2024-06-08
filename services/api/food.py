import aiohttp
from typing import List
from decouple import config

from dto.food import CategoryModel, FoodModel

BASE_URL = config("FOOD_BASE_URL")


class FoodService:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.base_url = BASE_URL

    async def get_categories(self) -> List[CategoryModel]:
        async with self.session as session:
            response = await session.get(f"{self.base_url}/")
            return await response.json()

    async def get_category(self, category_name: str) -> CategoryModel:
        async with self.session as session:
            response = await session.get(f"{self.base_url}?name={category_name}")
            return await response.json()

    async def get_foods(self) -> List[FoodModel]:
        async with self.session as session:
            response = await session.get(f"{self.base_url}/")
            return await response.json()

    async def get_food(self, food_name: str) -> FoodModel:
        async with self.session as session:
            response = await session.get(f"{self.base_url}?name={food_name}")
            return await response.json()

    async def check_child_category(self, data) -> bool:
        if data["children"] is not None:
            return True
        return False

