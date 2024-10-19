from schemas import Item

data = {"item_id": 0, "name": "Coke", "price": 120, "kind": "DRINK"}
item = Item.model_validate(data)
print(item)

json_str = '{"item_id": 1, "name": "Green Tea", "price": 140}'
item = Item.model_validate_json(json_str)
print(item)
