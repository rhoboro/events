from fastapi import FastAPI

from di3 import Connection, RequestID
from schemas import CreateItemRequest, Item

app = FastAPI()


@app.post("/items")
async def create_item(
    data: CreateItemRequest,
    request_id: RequestID,
    conn: Connection,
) -> Item:
    print(f"{request_id=}")
    print(f"{conn.request_id=}")
    item = {
        "item_id": 0,  # dummy
        "name": data.name,
        "price": data.price,
        "kind": data.kind,
    }
    return Item.model_validate(item)



