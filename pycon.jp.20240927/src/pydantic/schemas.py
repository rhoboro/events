from enum import StrEnum
from pydantic import BaseModel, PositiveInt


class Kind(StrEnum):
    DRINK = "DRINK"
    FOOD = "FOOD"


class Item(BaseModel):
    item_id: int
    name: str
    price: PositiveInt
    kind: Kind = Kind.DRINK
