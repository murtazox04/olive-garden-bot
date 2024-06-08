import aiohttp
from typing import List
from decouple import config

BASE_URL = config("CART_BASE_URL")


class FoodService:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.base_url = BASE_URL

    async def get_cart(self, user_id: int):
        url = f"{self.base_url}/cart/"
        async with self.session.get(url) as resp:
            if resp.status == 200:
                return await resp.json()

    async def create_cart_item(self, cart_item: dict):
        url = f"{self.base_url}/cart-item/"
        async with self.session.post(url, json=cart_item) as resp:
            if resp.status == 200:
                return await resp.json()

    async def update_cart_item(self, cart_item: dict):
        url = f"{self.base_url}/cart-item/"
        async with self.session.put(url, json=cart_item) as resp:
            if resp.status == 200:
                return await resp.json()

    async def delete_cart_item(self, cart_item: dict):
        url = f"{self.base_url}/cart-item/"
        async with self.session.delete(url, json=cart_item) as resp:
            if resp.status == 200:
                return await resp.json()