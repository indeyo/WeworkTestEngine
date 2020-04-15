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
from api.wework import WeWork

proxies = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888"
}


class Department(BaseApi):
    _secret = "-tzpw8mha37Q7pDSfu22XbLg9EQ38Kx9Dr9aBsX94VU"
    _access_token = None

    def get_token(self):
        if self._access_token is None:
            self._access_token = WeWork.get_access_token(self._secret)
        # self._access_token = self.get_access_token(self._secret)

    def list(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            params={"access_token": self._access_token},
            headers={"content-type": "application/json; charset=utf-8"},
            proxies=proxies,
            verify=False
        )
        self.format(r.json())
        return r.json()

    def create(self, name, parentid, name_en="", order="", id=""):
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            params={"access_token": self._access_token},
            json={
                "name": name,
                "parentid": parentid
                # "name_en": name_en,
                # "order": order,
                # "id": id
            },
            headers={"content-type": "application/json; charset=utf-8"},
            # headers={"Accept-Encoding": "charset=utf8"},
            proxies=proxies,
            verify=False
        )
        self.format(r.json())
        return r.json()

    def update(self):
        pass

    def delete(self):
        pass
