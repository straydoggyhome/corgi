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

