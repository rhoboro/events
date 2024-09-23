from uuid import UUID, uuid4

from fastapi import Depends, FastAPI
from schemas import CreateItemRequest, Item


async def gen_request_id() -> UUID:
    return uuid4()


app = FastAPI()


@app.post("/items")
async def create_item(
    data: CreateItemRequest,
    request_id: UUID = Depends(gen_request_id),
) -> Item:
    print(f"{request_id=}")
    item = {
        "item_id": 0,  # dummy
        "name": data.name,
        "price": data.price,
        "kind": data.kind,
    }
    return Item.model_validate(item)
