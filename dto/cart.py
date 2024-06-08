from typing import List

from pydantic import BaseModel


class CartItemModel(BaseModel):
    ...


class CartModel(BaseModel):
    items: List[CartItemModel]
