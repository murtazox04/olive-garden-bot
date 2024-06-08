from typing import List

from pydantic import BaseModel


class ChildCategory(BaseModel):
    id: int
    name: str


class FoodModel(BaseModel):
    id: int
    name: str
    category: str
    description: str
    price: float
    image: str


class CategoryModel(BaseModel):
    id: int
    name: str
    children: List[ChildCategory]

