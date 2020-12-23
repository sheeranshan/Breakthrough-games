#!/usr/bin/env python
# -*- coding:utf-8 -*-

# changer.py
# 装饰模式
# 为某些敌人对象添加 reborn() 方法

from abc import ABCMeta, abstractmethod
from enemy import *


# 装饰抽象类，从外类来扩展enemy类的功能
class Decorator(Enemy):
    def __init__(self, enemy):
        self._y = 0
        self._x = 0
        self._enemy = enemy

    def enemy_type(self):
        if self._enemy:
            return self._enemy.enemy_type()

    def set_location(self, x, y):
        self._x = x
        self._y = y

    def get_location(self):
        return [self._x, self._y]

    def dead(self):
        return self.enemy_type() + " is dead"


# 具体装饰对象，对某些敌人对象添加reborn（）函数
class RebornWarrior(Decorator):

    def __init__(self, enemy):
        self.__re = 1
        super(RebornWarrior, self).__init__(enemy)

    def dead(self):
        if self.__re == 0:
            self.__re = 1
            return super(RebornWarrior, self).dead()
        else:
            return super(RebornWarrior, self).dead() + self.reborn()

    # 表示敌人复活
    def reborn(self):
        self.__re = 0
        return " But it seems to be reborn……"


# if __name__ == "__main__":
#     enemy_1 = MageCreator().create()
#     enemy_1.set_location(1,2)
#
#     d1 = RebornWarrior(enemy_1)
#     print(d1.dead())
#     print(d1.dead())
