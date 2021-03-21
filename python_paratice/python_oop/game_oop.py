#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
1、一个回合制游戏，每个角色都有hp和power,hp代表血量，power代表攻击力
hp的初始值为1000，power的初始值为200
2、定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
两个hp进行对比，血量剩余多的人获胜
'''
from python_paratice.python_oop.log_decorator import log_decorator


class Game:

    # #构造方法
    # def __init__(self):
    #     #初始化属性
    #     self.my_hp = 1000
    #     self.my_power = 200
    #     self.enemy_hp = 1000
    #     self.enemy_power =199

    # 构造方法
    def __init__(self, my_hp, enemy_hp):
        # 初始化属性
        self.my_hp = my_hp
        self.my_power = 200
        self.enemy_hp = enemy_hp
        self.enemy_power = 199

        # 定义私有属性,私有变量不能通过对象去调用
        self.__secret = "secret"

    # 对打方法
    # @log_decorator装饰器的调用
    @log_decorator
    def fight(self):

        # 循环
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp - self.enemy_power

            # 敌人的剩余血量
            self.enemy_hp -= self.my_power

            print(f"我的血量：{self.my_hp} VS 敌人血量：{self.enemy_hp}")

            # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break

    # 定义休息方法
    def rest(self, time_num):
        # 私有方法和变量不可以通过对象去调用，但是可以通过类中的公共方法去调用
        self.__private_method()
        print(f"太累了，休息{time_num}分钟")

    # 定义私有方法
    def __private_method(self):
        print(self.__secret)
        print("这是一个私有方法")


if __name__ == '__main__':
    game = Game(1000, 1100)
    game.fight()
    game.rest(3)
