# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : department.py
@Time    : 2020-04-14  09:11:52
@Author  : indeyo_lin
"""
import json

import requests

from api.base_api import BaseApi

proxies = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888"
}


class Department(BaseApi):
    _secret = "-tzpw8mha37Q7pDSfu22XbLg9EQ38Kx9Dr9aBsX94VU"
    _access_token = None

    def get_token(self):
        if self._access_token is None:
            self._access_token = self.get_access_token(self._secret)
        # self._access_token = self.get_access_token(self._secret)

    def list(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            params={"access_token": self._access_token},
            proxies=proxies,
            verify=False
        )
        print(json.dumps(r.json(), indent=2))
        return r.json()

    def create(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
