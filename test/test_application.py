#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon
import sys
sys.path.append("..")

from corgi.application import Corgi
from wsgiref.simple_server import make_server


app = Corgi()

# app.wsgi_server()


# 创建一个服务器，IP地址为空，端口是8000，传入函数application
httpd = make_server('', 8000, app)
print('Serving HTTP on port 8000...')
# 开始监听HTTP请求:
httpd.serve_forever()