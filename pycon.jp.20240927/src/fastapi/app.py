from fastapi import FastAPI
from schemas import CreateItemRequest, Item

app = FastAPI()


@app.post("/items")
async def create_item(
    data: CreateItemRequest,
) -> Item:
    item = {
        "item_id": 0,  # dummy
        "name": data.name,
        "price": data.price,
        "kind": data.kind,
    }
    return Item.model_validate(item)
