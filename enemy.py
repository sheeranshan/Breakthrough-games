#!/usr/bin/env python
# -*- coding:utf-8 -*-

# enemy.py
# 定义两种敌人，法师和战士

from abc import ABCMeta, abstractmethod


# 定义工厂方法所创建的敌人接口
class Enemy(metaclass=ABCMeta):

    # 抽象方法，返回敌人种族（类型）
    @abstractmethod
    def enemy_type(self):
        pass

    # 抽象方法，设置敌人位置
    @abstractmethod
    def set_location(self, x, y):
        pass

    # 抽象方法，获取敌人位置
    @abstractmethod
    def get_location(self):
        pass

    # 抽象方法，敌人死亡
    @abstractmethod
    def dead(self):
        pass


# 法师，实现了敌人的接口
class Mage(Enemy):

    # 构造函数，初始坐标为[0,0]
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def enemy_type(self):
        return self.__class__.__name__

    def set_location(self, x, y):
        self.__x = x
        self.__y = y

    def get_location(self):
        return [self.__x, self.__y]

    def dead(self):
        return self.enemy_type() + " is dead"


# 战士，实现了敌人的接口
class Warrior(Enemy):

    # 构造函数，初始坐标为[0,0]
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def enemy_type(self):
        return self.__class__.__name__

    def set_location(self, x, y):
        self.__x = x
        self.__y = y

    def get_location(self):
        return [self.__x, self.__y]

    def dead(self):
        return self.enemy_type() + " is dead"


# 声明了工厂方法, 该方法返回一个Enemy类型的对象
class EnemyCreator(object):
    @abstractmethod
    def create(self):
        pass


# 重定义，返回一个Mage实例
class MageCreator(EnemyCreator):

    def create(self):
        return Mage()


# 重定义，返回一个Warrior实例
class WarriorCreator(EnemyCreator):

    def create(self):
        return Warrior()

