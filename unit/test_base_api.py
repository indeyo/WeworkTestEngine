# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : test_base_api.py
@Time    : 2020-04-14  09:52:23
@Author  : indeyo_lin
"""
from api.wework import WeWork


class TestBaseApi:
    def setup(self):
        self.base = WeWork()

    def test_get_access_token(self):
        secret = "-tzpw8mha37Q7pDSfu22XbLg9EQ38Kx9Dr9aBsX94VU"
        assert self.base.get_access_token(secret) != ""