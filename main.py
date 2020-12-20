#!/usr/bin/env python
# -*- coding:utf-8 -*-

from UI import *
import random


if __name__ == '__main__':

    # 例1
    role_1 = Role()
    role_1.set_name("tony")
    role_1.set_cloth(ConcreteClothesFactory2())
    role_1.set_location(1, 1)

    enemies_1 = []
    for i in range(0, 20):
        j = random.randrange(0, 2)
        if j == 0:
            enemy_1 = MageCreator().create()
            enemy_1.set_location(random.randrange(2, 40), random.randrange(1, 20))
            enemies_1.append(enemy_1)
        else:
            enemy_1 = WarriorCreator().create()
            enemy_1.set_location(random.randrange(2, 40), random.randrange(1, 20))
            enemies_1.append(enemy_1)

    # 生成地图
    b1 = BuilderA()
    Director.construct(b1, role_1, enemies_1)
    m1 = b1.get_result()

    # 例2
    role_2 = Role()
    role_2.set_name("nick")
    role_2.set_cloth(ConcreteClothesFactory1())
    role_2.set_location(1, 1)

    enemies_2 = []
    for i in range(0, 20):
        j = random.randrange(0, 2)
        if j == 0:
            enemy_1 = MageCreator().create()
            enemy_1.set_location(random.randrange(2, 40), random.randrange(1, 20))
            enemies_2.append(enemy_1)
        else:
            enemy_1 = WarriorCreator().create()
            enemy_1.set_location(random.randrange(2, 40), random.randrange(1, 20))
            enemies_2.append(enemy_1)

    b2 = BuilderB()
    Director.construct(b2, role_2, enemies_2)
    m2 = b2.get_result()

    GameUI(m2)

