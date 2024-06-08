import aiohttp
from decouple import config


BASE_URL = config('ORDER_BASE_URL')


class OrderService:
    def __init__(self):
        self.session = aiohttp.ClientSession()
        self.base_url = BASE_URL

    async def get_order(self, header):
        url = f"{self.base_url}/orders"
        header = header
        async with self.session.get(url, header=header) as resp:
            if resp.status == 200:
                return await resp.json()
            raise "Not Found!"

    async def create_order(self, order, header):
        url = f"{self.base_url}/orders"
        header = header
        async with self.session.post(url, json=order, header=header) as resp:
            if resp.status == 200:
                return await resp.json()
            raise "The order was not created!"

    async def update_order(self, order, header):
        url = f"{self.base_url}/orders/{order['id']}"
        header = header
        async with self.session.put(url, json=order, header=header) as resp:
            if resp.status == 200:
                return await resp.json()

    async def delete_order(self, order, header):
        url = f"{self.base_url}/orders/{order['id']}"
        header = header
        async with self.session.delete(url, json=order, header=header) as resp:
            if resp.status == 200:
                return await resp.json()
