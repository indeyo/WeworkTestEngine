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
        assert len(resp) != 0

    def test_create(self):
        department_name = "test"
        assert self.department.create(department_name, 1)["errcode"] == 0
        assert department_name in self.department.get_departments_by_attribute("name")

    def test_update(self):
        resp = self.department.update(33, name="更新部门11")
        assert resp["errcode"] == 0
        names = []
        for item in self.department.list()["department"]:
            names.append(item["name"])
        assert "更新部门" in "|".join(names)

    def test_delete(self):
        delete_id = 15
        resp = self.department.delete(delete_id)
        assert resp["errcode"] == 0
        ids = []
        for item in self.department.list()["department"]:
            ids.append(item["id"])
        assert delete_id not in ids