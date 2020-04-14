# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : base_api.py
@Time    : 2020-04-14  08:58:25
@Author  : indeyo_lin
"""
import json

import requests


class BaseApi:
    _corpid = "ww84f2624b18176321"

    def get_access_token(self, corpsecret):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
                "corpid": self._corpid,
                "corpsecret": corpsecret
            }
        )
        print(json.dumps(r.json(), indent=2))
        return r.json()["access_token"]

    def request(self, method, url, **kwargs):
        # todo:不太明白封装requests的意义
        r = requests.request(method, url, **kwargs)
        return r.json()