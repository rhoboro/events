# 注意事項
# - ASGIサーバーとASGIアプリケーションがどちらもLifespan Event, Lifespan Stateをサポートしている前提
# - 簡単のため、クエリパラメータや認証情報、JSON以外のレスポンスなどは考慮しない
# - gunicornの場合はCtrl+CのSIGINTで即時終了するため、 SIGTERMで終了させること(`kill -TERM PID`など)
#
# uv run traffic_mirror.py
# curl http://127.0.0.1:8000/users/123 -H 'content-type: application/json' -d '{"hello": "world"}'
import asyncio
import httpx


class TrafficMirrorMiddleware:
    def __init__(self, app, base_url):
        self.app = app
        self.lifespan_app = LifespanApp(app, self.on_startup, self.on_shutdown)
        self.base_url = base_url

    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            await self.lifespan_app(scope, receive, send)
            return
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return
        app = MirrorApp(self.app)
        await app(scope, receive, send)

    async def on_startup(self, state):
        print("on_startup")
        state["client"] = httpx.AsyncClient(base_url=self.base_url, timeout=5.0)
        tg = asyncio.TaskGroup()
        await tg.__aenter__()
        state["tg"] = tg

    async def on_shutdown(self, state):
        tg = state.pop("tg", None)
        if tg:
            # 実行中タスクの完了を待つ
            await tg.__aexit__(None, None, None)

        client = state.pop("client", None)
        if client:
            await client.aclose()
        print("on_shutdown")


class MirrorApp:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        events = await self.drain(receive)
        request_body = b"".join(
            m.get("body", b"") for m in events if m["type"] == "http.request"
        )
        self.create_task(scope, self.mirror(scope, request_body))

        async def replay():
            if events:
                return events.pop(0)
            return await receive()

        await self.app(scope, replay, send)

    async def drain(self, receive):
        events = []
        while True:
            event = await receive()
            events.append(event)
            if event["type"] != "http.request" or not event.get("more_body", False):
                break
        return events

    async def mirror(self, scope, body):
        client = scope["state"]["client"]
        headers = [(k, v) for k, v in scope["headers"] if k != b"host"]
        response = await client.request(
            scope["method"], scope["path"], headers=headers, content=body
        )
        print(response.json())

    def create_task(self, scope, coro):
        # tg.create_task()はエラーになるとそれ以降利用できなくなるのでガードする
        async def wrap():
            try:
                await coro
            except Exception as e:
                print(f"{e!r}")

        tg = scope["state"]["tg"]
        tg.create_task(wrap())


class LifespanApp:
    def __init__(self, app, on_startup, on_shutdown):
        self.app = app
        self.on_startup = on_startup
        self.on_shutdown = on_shutdown

    async def __call__(self, scope, receive, send):
        assert scope["type"] == "lifespan"
        self.scope = scope
        self.receive = receive
        self.send = send

        await self.app(scope, self.my_receive, self.my_send)

    async def my_receive(self):
        event = await self.receive()
        if event["type"] == "lifespan.startup":
            await self.on_startup(self.scope["state"])
        return event

    async def my_send(self, event):
        if event["type"] in (
            "lifespan.shutdown.complete",
            "lifespan.shutdown.failed",
        ):
            await self.on_shutdown(self.scope["state"])
        await self.send(event)
