#!/usr/bin/env python
# -*- coding:utf-8 -*-

# roleinformation.py
#
# 角色信息：名称和衣服搭配方案

from clothes import *


# 角色类
class Role(object):
    # 构造函数，初始化名称和衣服搭配方案，衣服搭配方案默认为方案1
    def __init__(self):
        self.__name = ""
        self.__cloth = ConcreteClothesFactory1()
        self.__location_x = 0
        self.__location_y = 0

    # 设置名称
    def set_name(self, name):
        self.__name = name

    # 设置衣服搭配方案
    def set_cloth(self, clo):
        self.__cloth = clo

    # 设置角色位置
    def set_location(self, x, y):
        self.__location_x = x
        self.__location_y = y

    # 获取名称
    def get_name(self):
        return self.__name

    # 获取衣服搭配方案
    def get_cloth(self):
        return self.__cloth

    # 获取角色位置
    def get_location(self):
        return [self.__location_x, self.__location_y]

