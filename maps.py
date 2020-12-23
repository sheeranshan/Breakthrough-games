#!/usr/bin/env python
# -*- coding:utf-8 -*-
# maps.py
# 建造者模式
# 用于生成地图，包括地形（landform）、角色（role）、敌人（enemy）

from abc import ABCMeta, abstractmethod
from enemy import *
from roleinformation import *


# 具体地图类
class Map(object):

    # 构造函数
    def __init__(self):
        self.__landform = ""
        self.__role = Role()
        self.__enemies = []

    # 设置地形
    def set_landform(self, landform="default"):
        self.__landform = landform

    # 创建角色
    def set_role(self, role):
        self.__role = role

    # 添加敌人
    def add_enemy(self, enemies):
        self.__enemies = enemies

    def get_landform(self):
        return self.__landform

    def get_role(self):
        return self.__role

    def get_enemy(self):
        return self.__enemies


# 创建一个Map对象的各个部件指定的抽象接口
class Builder(metaclass=ABCMeta):

    # 设置地形
    @abstractmethod
    def build_landform(self):
        pass

    # 创建角色
    @abstractmethod
    def build_role(self, role):
        pass

    # 添加敌人
    @abstractmethod
    def build_enemy(self, enemy):
        pass

    # 获取结果
    @abstractmethod
    def get_result(self):
        pass


# 具体地图A
class BuilderA(Builder):

    def __init__(self):
        self.__map = Map()

    def build_landform(self):
        self.__map.set_landform()

    def build_role(self, role):
        self.__map.set_role(role)

    def build_enemy(self, enemy):
        self.__map.add_enemy(enemy)

    def get_result(self):
        return self.__map


# 具体地图B
class BuilderB(Builder):

    def __init__(self):
        self.__map = Map()

    def build_landform(self):
        self.__map.set_landform("forest")

    def build_role(self, role):
        self.__map.set_role(role)

    def build_enemy(self, enemy):
        self.__map.add_enemy(enemy)

    def get_result(self):
        return self.__map


# 指挥生成地图过程
class Director(object):

    @staticmethod
    def construct(builder, role, enemy):
        builder.build_landform()
        builder.build_role(role)
        builder.build_enemy(enemy)


