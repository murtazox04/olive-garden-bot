from pydantic import BaseModel


class RegisterUser(BaseModel):
    first_name: str
    last_name: str
    username: str
    phone_number: str
    telegram_id: int


class UserGeolocation(BaseModel):
    telegram_id: int
    lat: float
    lng: float
    reference_point: str
