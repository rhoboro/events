import json
from schemas import Item

json_schema = Item.model_json_schema()
print(json.dumps(json_schema, indent=2))
