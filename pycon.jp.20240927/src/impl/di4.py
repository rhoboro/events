from typing import Annotated
from uuid import UUID, uuid4

from light_dpends import Depends


def gen_request_id() -> UUID:
    return uuid4()


RequestID = Annotated[UUID, Depends(gen_request_id)]


class SomeConnection:
    def __init__(self, request_id: RequestID) -> None:
        self.request_id = request_id

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}(request_id={self.request_id!r})>"


Connection = Annotated[SomeConnection, Depends(SomeConnection)]
