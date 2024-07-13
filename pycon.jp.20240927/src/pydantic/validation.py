from schemas import Item
from pydantic import ValidationError

data = {"item_id": 0, "name": "Coke", "price": -100, "kind": "SNACK"}
try:
    Item.model_validate(data)
except ValidationError as e:
    print(e)
