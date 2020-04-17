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
        self.secret = "W1a-_z8wERVJRacyrzhuf5W4vHqBTkd2ghvTwAfivwI"

    def test_get_access_token(self):
        assert WeWork.get_access_token(self.secret) != ""

    def test_get_token(self):
        assert WeWork.get_token(self.secret) != ""