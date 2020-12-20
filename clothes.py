#!/usr/bin/env python
# -*- coding:utf-8 -*-

# clothes.py
#
# 抽象工厂模式
# 定义服装套装，包括上衣，裤子，鞋
# 每组套装具有固定的搭配方式

from abc import ABCMeta, abstractmethod


# 抽象产品——上衣
class AbstractCoats(object):
    # 构造函数
    def __init__(self, color):
        self.color = color

    # 返回具体对象属性（color）值
    def __str__(self):
        return self.color


# 抽象产品——裤子
class AbstractPants(object):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color


# 抽象产品——鞋子
class AbstractShoes(object):
    def __init__(self, color):
        self.color = color

    def __str__(self):
        return self.color


# 六个具体产品
class ConcreteCoats1(AbstractCoats):
    pass


class ConcreteCoats2(AbstractCoats):
    pass


class ConcretePants1(AbstractPants):
    pass


class ConcretePants2(AbstractPants):
    pass


class ConcreteShoes1(AbstractShoes):
    pass


class ConcreteShoes2(AbstractShoes):
    pass


# 抽象工厂接口 包含所有服装产品创建的抽象方法
class AbstractClothesFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_coats(self):
        pass

    @abstractmethod
    def create_pants(self):
        pass

    @abstractmethod
    def create_shoes(self):
        pass


# 衣服搭配方案1
class ConcreteClothesFactory1(AbstractClothesFactory):
    def create_coats(self):
        return ConcreteCoats1("red")

    def create_pants(self):
        return ConcretePants1("blue")

    def create_shoes(self):
        return ConcreteShoes1("grey")


# 衣服搭配方案2
class ConcreteClothesFactory2(AbstractClothesFactory):
    def create_coats(self):
        return ConcreteCoats2("green")

    def create_pants(self):
        return ConcretePants2("black")

    def create_shoes(self):
        return ConcreteShoes2("white")

