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

    def test_list(self):
        resp = self.department.list()
        assert resp["errcode"] == 0
        assert len(resp) != 0

    def test_create(self):
        department_name = "dont give up"
        assert self.department.create(department_name, 1)["errcode"] == 0
        assert department_name in self.department.get_departments_by_attribute("name")

    def test_update(self):
        update_content = "更新部门22"
        resp = self.department.update(33, name=update_content)
        assert resp["errcode"] == 0
        assert update_content in self.department.get_departments_by_attribute("name")

    def test_delete(self):
        delete_id = 5
        resp = self.department.delete(delete_id)
        assert resp["errcode"] == 0
        assert delete_id not in self.department.get_departments_by_attribute("id")