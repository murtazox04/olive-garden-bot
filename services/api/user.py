import aiohttp
from typing import Dict
from decouple import config

BASE_URL = config('USER_BASE_URL')


class UserService:
    endpoint = BASE_URL

    @staticmethod
    async def get(path: str, **kwargs: Dict[str, str]) -> dict:
        headers: Dict[str, str] = kwargs.get('headers', {})
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.get(UserService.endpoint + path) as resp:
                return await resp.json()

    @staticmethod
    async def post(path, **kwargs):
        headers: Dict[str, str] = kwargs.get('headers', {})
        data = kwargs.get('data', [])
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.post(UserService.endpoint + path, data=data) as resp:
                return await resp.json()

    @staticmethod
    async def put(path, **kwargs):
        headers: Dict[str, str] = kwargs.get('headers', {})
        data = kwargs.get('data', [])
        async with aiohttp.ClientSession(headers=headers) as session:
            async with session.put(UserService.endpoint + path, data=data) as resp:
                return await resp.json()
