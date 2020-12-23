#!/usr/bin/env python
# -*- coding:utf-8 -*-
# operation.py
# 定义玩家操作，前后左右行走、攻击和退出六种操作方式，并添加空操作

from roleinformation import *
from enemy import *


class Operation(object):

    # property装饰器，可以通过访问方法名来获得私有属性
    @property
    def role_a(self):
        return self.__role_a

    @role_a.setter
    def role_a(self, value):
        self.__role_a = value

    @property
    def role_b(self):
        return self.__role_b

    @role_b.setter
    def role_b(self, value):
        self.__role_b = value


# 攻击
class OperationAtc(Operation):
    def op(self):
        if self.role_a.get_location() == self.role_b.get_location():
            return "attack"
        else:
            return "missed attack"

    def isNil(self):
        return False


# 向上走
class OperationUp(Operation):
    def op(self):
        if self.role_a.get_location()[1] > 0:
            self.role_a.set_location(self.role_a.get_location()[0], self.role_a.get_location()[1]-1)
            return self.role_a.get_name() + " go forward "

    def isNil(self):
        return False


# 向下走
class OperationDown(Operation):
    def op(self):
        if self.role_a.get_location()[1] < 19:
            self.role_a.set_location(self.role_a.get_location()[0], self.role_a.get_location()[1]+1)
            return self.role_a.get_name() + " go back "

    def isNil(self):
        return False


# 向左走
class OperationLeft(Operation):
    def op(self):
        if self.role_a.get_location()[0] > 0:
            self.role_a.set_location(self.role_a.get_location()[0]-1, self.role_a.get_location()[1])
            return self.role_a.get_name() + " go left "

    def isNil(self):
        return False


# 向右走
class OperationRight(Operation):
    def op(self):
        if self.role_a.get_location()[0] < 39:
            self.role_a.set_location(self.role_a.get_location()[0]+1, self.role_a.get_location()[1])
            return self.role_a.get_name() + " go right "

    def isNil(self):
        return False


# 退出
class OperationExit(Operation):
    def op(self):
        return "you failed"

    def isNil(self):
        return False


# 空操作
class OperationPass(Operation):
    def op(self):
        return "pass"

    def isNil(self):
        return True


# 操作工厂
class OperationFactory(object):
    @staticmethod
    def create_operation(operation):
        if operation == "w" or operation == "W":
            return OperationUp()
        elif operation == "s" or operation == "S":
            return OperationDown()
        elif operation == "a" or operation == "A":
            return OperationLeft()
        elif operation == "d" or operation == "D":
            return OperationRight()
        elif operation == "j" or operation == "J":
            return OperationAtc()
        elif operation == "t" or operation == "T":
            return OperationExit()
        else:
            return OperationPass()

