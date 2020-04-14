# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@Project : WeworkTestEngine
@File    : test_department.py
@Time    : 2020-04-14  10:52:26
@Author  : indeyo_lin
"""
from api.department import Department


class TestDepartment:
    def setup_class(self):
        self.department = Department()
        self.department.get_token()

    def test_list(self):
        assert self.department.list()["errcode"] == 0
