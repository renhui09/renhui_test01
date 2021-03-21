#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Work.Animal_work.Animal import Animal


class Cat(Animal):
    hair = "短毛"

    # 重新父类方法
    def __init__(self, name, color, age, sex, hair=None):
        super().__init__(name, color, age, sex)
        if hair is not None:
            self.hair = hair

    # 添加子类方法
    def specialty(self):
        print("会捉老鼠")

    # 重新方法
    def call(self):
        print("喵喵叫")


if __name__ == '__main__':
    cat = Cat(name="阿毛", color="蓝色", age="1", sex="母")
    print(f"名字叫{cat.name},颜色为{cat.color},年龄{cat.age},性别{cat.sex}，毛发{cat.hair}")
    cat.call()
    cat.specialty()
