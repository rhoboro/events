
```sh
$ uv sync --frozen
$ uv run process_time.py
INFO:     Started server process [73827]
INFO:     Waiting for application startup.
INFO:     ASGI 'lifespan' protocol appears unsupported.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     127.0.0.1:62890 - "POST / HTTP/1.1" 200 OK
processing time: 0.000311249983496964
```

```sh
$ curl http://127.0.0.1:8000
$ curl http://127.0.0.1:8000/error
$ curl -i http://127.0.0.1:8000 -H 'content-type: application/json' -d '{"hello": "world"}'
$ curl -i http://127.0.0.1:8000/users/123 -H 'content-type: application/json' -d '{"hello": "world"}' -u rhoboro:secret
```

