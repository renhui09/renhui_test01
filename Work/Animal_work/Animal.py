#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Animal:
    name = "阿花"
    color = "黄色"
    age = "2月"
    sex = "公"

    def __init__(self, name, color, age, sex):
        """

        :param name: 名称
        :param color: 颜色
        :param age: 年龄
        :param sex: 性别
        """

        self.name = name
        self.color = color
        self.age = age
        self.sex = sex

    # 方法：叫
    def call(self):
        print("会叫")

    # 方法：跑
    def run(self):
        print("会跑")
