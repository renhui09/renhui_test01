#!/usr/bin/env python
# -*- coding: utf-8 -*-
from python_paratice.python_oop.game_oop import Game


# 继承game类
class HouYi(Game):
    '''
    后裔，后裔继承了Game的hp和power,并多了护甲属性
    重新定义另外一个defense属性：
    final_hp = hp + defense - enemy_power
    enemy_final_hp = enemy_hp - power
    两个hp进行对比，血量先为零的人输掉比赛
    '''

    # 构造方法
    def __init__(self):
        self.defense = 100

        # 继承父类的构造方法
        super().__init__(1000, 1100)

    # 重新 如果用到父类的方法，需要用到super().否则不需要
    def fight(self):
        # 改造一下 my_hp 的计算方式
        while True:
            # 我的剩余血量
            self.my_hp = self.my_hp + self.defense - self.enemy_power

            # 敌人的剩余血量
            self.enemy_hp -= self.my_power

            print(f"我的血量：{self.my_hp} VS 敌人血量：{self.enemy_hp}")

            super().rest(3)
            # 胜负判断
            if self.my_hp <= 0:
                print("我输了")
                break
            elif self.enemy_hp <= 0:
                print("我赢了")
                break


if __name__ == "__main__":
    houyi = HouYi()

    # 子类对象可以直接调用父类的属性和方法
    print(houyi.my_power)
    houyi.fight()
    houyi.rest(3)
