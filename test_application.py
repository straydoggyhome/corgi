#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon
from wsgiref.simple_server import make_server

from corgi.application import Corgi


# app = Corgi()
# app.listen()

app = Corgi()
host='127.0.0.1'
port=8888
server = make_server(host, port, app)
print('server started')
server.serve_forever()