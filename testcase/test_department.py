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
        resp = self.department.list()
        assert resp["errcode"] == 0

    def test_create(self):
        department_name = "333"
        assert self.department.create(department_name, 1)["errcode"] == 0
        names = []
        for item in self.department.list()["department"]:
            names.append(item["name"])
        assert department_name in "|".join(names)