# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : wework.py
@Time    : 2020-04-14  08:58:25
@Author  : indeyo_lin
"""
import json

import requests

from api.base_api import BaseApi

proxies = {
    "http": "127.0.0.1:8888",
    "https": "127.0.0.1:8888"
}


class WeWork(BaseApi):
    _corpid = "ww84f2624b18176321"
    _token = {}

    @classmethod
    def get_token(cls, secret):
        # done: 需要保存token，不用每次调用都去请求
        if secret not in cls._token.keys():
            cls._token[secret] = cls.get_access_token(secret)
        cls.format("", cls._token)
        return cls._token[secret]

    # 类函数，直接通过类调用，不需要创建对象
    @classmethod
    def get_access_token(cls, corpsecret):
        r = requests.get(
            "https://qyapi.weixin.qq.com/cgi-bin/gettoken",
            params={
                "corpid": cls._corpid,
                "corpsecret": corpsecret
            },
            proxies=proxies,
            verify=False
        )
        # 类方法调用父类实例方法报错，前面随便加个值字可以通过
        # todo:待排查：TypeError: format() missing 1 required positional argument: 'data'
        # 实例方法可以正常调用
        # cls.format(r.json())
        return r.json()["access_token"]

    def request(self, method, url, **kwargs):
        # todo:不太明白封装requests的意义
        r = requests.request(method, url, **kwargs)
        return r.json()