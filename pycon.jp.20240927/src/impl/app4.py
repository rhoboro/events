from di4 import Connection, RequestID
from light_dpends import resolve


@resolve
def handler(request_id: RequestID, connection: Connection) -> None:
    print(f"{request_id=}")
    print(f"{connection.request_id=}")


if __name__ == "__main__":
    handler()
