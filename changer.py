#!/usr/bin/env python
# -*- coding:utf-8 -*-

# changer.py
#
# 装饰模式
# 为 enemy 添加 dead（） 方法

from abc import ABCMeta, abstractmethod
from enemy import *


# 装饰抽象类，从外类来扩展enemy类的功能
class Decorator(Enemy):
    def __init__(self, enemy):
        self.__y = 0
        self.__x = 0
        self.__enemy = enemy

    def enemy_type(self):
        if self.__enemy:
            return self.__enemy.enemy_type()

    def set_location(self, x, y):
        self.__x = x
        self.__y = y

    def get_location(self):
        return [self.__x, self.__y]


# 具体装饰对象，给enemy添加dead（）函数
class DecoratorDead(Decorator):

    # 表示敌人死亡
    def dead(self):
        return super(DecoratorDead, self).enemy_type() + " is dead"

