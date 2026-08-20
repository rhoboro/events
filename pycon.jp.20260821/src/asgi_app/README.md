```sh
$ uv sync --frozen
$ uv run uvicorn health:app --log-level trace
INFO:     Started server process [27922]
INFO:     Waiting for application startup.
TRACE:    ASGI [1] Started scope={'type': 'lifespan', 'asgi': {'version': '3.0', 'spec_version': '2.0'}, 'state': {}}
TRACE:    ASGI [1] Raised exception
INFO:     ASGI 'lifespan' protocol appears unsupported.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
TRACE:    127.0.0.1:62305 - HTTP connection made
TRACE:    127.0.0.1:62305 - ASGI [2] Started scope={'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('127.0.0.1', 8000), 'client': ('127.0.0.1', 62305), 'scheme': 'http', 'method': 'GET', 'root_path': '', 'path': '/health', 'raw_path': b'/health', 'query_string': b'', 'headers': '<...>', 'state': {}}
TRACE:    127.0.0.1:62305 - ASGI [2] Send {'type': 'http.response.start', 'status': 200, 'headers': '<...>'}
INFO:     127.0.0.1:62305 - "GET /health HTTP/1.1" 200 OK
TRACE:    127.0.0.1:62305 - ASGI [2] Send {'type': 'http.response.body', 'body': '<17 bytes>'}
TRACE:    127.0.0.1:62305 - ASGI [2] Completed
TRACE:    127.0.0.1:62305 - HTTP connection lost
TRACE:    127.0.0.1:62306 - HTTP connection made
TRACE:    127.0.0.1:62306 - ASGI [3] Started scope={'type': 'http', 'asgi': {'version': '3.0', 'spec_version': '2.3'}, 'http_version': '1.1', 'server': ('127.0.0.1', 8000), 'client': ('127.0.0.1', 62306), 'scheme': 'http', 'method': 'POST', 'root_path': '', 'path': '/', 'raw_path': b'/', 'query_string': b'', 'headers': '<...>', 'state': {}}
TRACE:    127.0.0.1:62306 - ASGI [3] Receive {'type': 'http.request', 'body': '<8 bytes>', 'more_body': False}
TRACE:    127.0.0.1:62306 - ASGI [3] Send {'type': 'http.response.start', 'status': 200, 'headers': '<...>'}
INFO:     127.0.0.1:62306 - "POST / HTTP/1.1" 200 OK
TRACE:    127.0.0.1:62306 - ASGI [3] Send {'type': 'http.response.body', 'body': '<8 bytes>'}
TRACE:    127.0.0.1:62306 - ASGI [3] Completed
TRACE:    127.0.0.1:62306 - HTTP connection lost
```

```sh
curl http://127.0.0.1:8000/health
curl -i http://127.0.0.1:8000 -d 'spam=ham'
```

