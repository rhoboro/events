from schemas import Item

data = {"item_id": 0, "name": "Coke", "price": 120}
item = Item.model_validate(data)
print(item.model_dump())
print(item.model_dump_json())
