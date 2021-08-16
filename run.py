#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon
from wsgiref.simple_server import make_server


def app(environ, start_response):
    print(environ)
    print(type(environ))
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])

# 创建一个服务器，IP地址为空，端口是8000，传入函数application
httpd = make_server('', 8000, app)

print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()