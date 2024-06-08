from decouple import config

from dto.user import RegisterUser
from services.api.user import UserService

BASE_URL = config('USER_BASE_URL')


class AuthService:
    user_service = UserService

    @staticmethod
    async def login(request: RegisterUser) -> dict:
        data = request.dict()
        return await AuthService.user_service.post("/login", data=data)

    @staticmethod
    async def refresh_token(refresh_token: str) -> dict:
        return await AuthService.user_service.post("/refresh", data={"refresh_token": refresh_token})


