#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon


class Corgi:

    def wsgi_server(self, environ: dict, start_response):
        data = b'this is a test'
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])


