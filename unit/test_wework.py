# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : test_wework.py
@Time    : 2020-04-14  09:52:23
@Author  : indeyo_lin
"""
from api.wework import WeWork


class TestBaseApi:
    def setup(self):
        self.base = WeWork()

    def test_get_access_token(self):
        secret = "W1a-_z8wERVJRacyrzhuf5W4vHqBTkd2ghvTwAfivwI"
        assert self.base.get_token(secret) != ""