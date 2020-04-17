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
    # @classmethod
    def format(self, data):
        # 默认是ASCII编码，设置成False可以打印中文
        print(json.dumps(data, indent=2, ensure_ascii=False))