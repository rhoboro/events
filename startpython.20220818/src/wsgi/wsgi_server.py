import argparse
from importlib import import_module
from wsgiref.simple_server import make_server


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("app", help="module:app_name")
    parser.add_argument("-p", default=8000, help="port")
    args = parser.parse_args()

    app = import_module(args.app.split(":", 1)[0])

    with make_server("", args.p, getattr(app, args.app.split(":", 1)[1])) as httpd:
        print("Serving HTTP on port 8000...")
        httpd.serve_forever()


if __name__ == "__main__":
    main()
