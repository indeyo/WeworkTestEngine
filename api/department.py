# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : department.py
@Time    : 2020-04-14  09:11:52
@Author  : indeyo_lin
"""
import json
from pprint import pprint

import requests

from api.base_api import BaseApi
from api.wework import WeWork

proxies = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888"
}


class Department(BaseApi):
    _secret = "-tzpw8mha37Q7pDSfu22XbLg9EQ38Kx9Dr9aBsX94VU"

    def list(self):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/department/list",
            params={"access_token": WeWork.get_token(self._secret)},
            # headers={"content-type": "application/json; charset=UTF-8"},
            headers={"content-type": "charset=utf-8"},
            proxies=proxies,
            verify=False
        )
        # 只对r.text起作用，对r.json()没用
        r.encoding = "utf-8"
        # print(r.text)
        # print(type(json.loads(r.text)))
        # text是字符串类型，无法使用json格式化的方法
        # print(type(r.text))
        self.format(r.json())
        return r.json()

    def create(self, name, parentid, **kwargs):
        data = {
            "name": name,
            "parentid": parentid
        }
        data.update(kwargs)
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/department/create",
            params={"access_token": WeWork.get_token(self._secret)},
            # 这里用data会报错：60001，Warning: wrong json format. department invalid length
            # done: data和json有何区别？
            # 可抓包看数据
            # 用json表示，请求体body用json格式发送，{"name": "dont give up", "parentid": 1}
            # 用data表示，请求体body用赋值的格式传递，name=dont+give+up&parentid=1
            json=data,
            # data=data,
            headers={"content-type": "application/json; charset=utf-8"},
            # headers={"Accept-Encoding": "charset=utf8"},
            proxies=proxies,
            verify=False
        )
        self.format(r.json())
        return r.json()

    def update(self, id, **kwargs):
        data = {"id": id}
        data.update(kwargs)
        r = requests.post(
            "https://qyapi.weixin.qq.com/cgi-bin/department/update",
            params={"access_token": WeWork.get_token(self._secret)},
            json=data,
            headers={"content-type": "application/json; charset=UTF-8"},
            proxies=proxies,
            verify=False
        )
        r.encoding = "utf-8"
        self.format(r.json())
        return r.json()

    def delete(self, id):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/department/delete",
            params={
                "access_token": WeWork.get_token(self._secret),
                "id": id
            },
            headers={"content-type": "application/json; charset=UTF-8"},
            proxies=proxies,
            verify=False
        )
        self.format(r.json())
        return r.json()

    def get_departments_by_attribute(self, attribute):
        """获取部门的id或者name数组格式，用于断言"""
        list = []
        for item in self.list()["department"]:
            list.append(item[attribute])
        return list