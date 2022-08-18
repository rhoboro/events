def simple_app(environ, start_response):
    print(environ)
    status = "200 OK"
    response_headers = [("Content-Type", "text/plain")]
    start_response(status, response_headers)
    return [b"Hello, world!\n"]
