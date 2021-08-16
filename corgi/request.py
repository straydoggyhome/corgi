#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ibegyourpardon

class Request:

    def __init__(
            self,
            environ
    ):
        print('request init')

    def get_ua(self, environ):
        return environ['HTTP_USER_AGENT']