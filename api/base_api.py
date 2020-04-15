# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : base_api.py
@Time    : 2020-04-14  16:25:28
@Author  : indeyo_lin
"""
import json


class BaseApi:
    def format(self, data):
        print(json.dumps(data, indent=2))