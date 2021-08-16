#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon
# from wsgiref.simple_server import make_server


def app(environ, start_response):
    print(environ)
    print(type(environ))
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

# if __name__ == '__main__':
#     httpd = make_server('', 9999, application)
#     print("Serving HTTP on port 9999...")
#     httpd.serve_forever()