#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon


class Corgi:
    def __init__(self, name='App') -> None:
        self.name = name
        self.html = \
            b"""
                <html>
                    <head>
                        <title>123</title>
                    </head>
                    <body>
                        <h1>444 is working!</h1>
                    </body>
                </html>
            """

    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-type", "text/html"),
                                  ('Content-Length', str(len(self.html)))])

        return [self.html]


