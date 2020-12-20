# python3 使用 tkinter
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from maps import *
from enemy import *
from changer import *
from roleinformation import *
from clothes import *
from operation import *
import random


# 游戏界面
class GameUI:
    def __init__(self, my_map):
        # 像素点宽度
        self.step = 15
        # 计时器
        self.time = 20
        # 当前层数
        self.level = 1
        # 当前层敌人数量
        self.num = 1
        self.image = None
        self.__map = my_map

        self.root = Tk()
        self.frame1 = Frame(self.root)
        self.frame1.pack(padx=1, pady=1)
        self.frame2 = Frame(self.root)
        self.frame2.pack()
        self.label1 = Label(self.frame2, text="")
        self.label1.pack(padx=2, side=LEFT, fill=Y)
        self.label2 = Label(self.frame2, text="")
        self.label2.pack(padx=2, side=RIGHT, fill=Y)
        self.canvas = Canvas()

        self.update_clock()
        while True:
            self.label2.configure(text="level: %d" % self.level)
            self.canvas.destroy()
            self.draw_map()
            self.draw_enemy()
            self.canvas.bind("<Key>", self.move)
            self.canvas.focus_set()

            while True:
                self.canvas.delete("coats")
                self.canvas.delete("pants")
                self.canvas.delete("shoes")
                self.canvas.delete("role_name")
                self.draw_role()
                e = False
                for i in range(self.num):
                    if self.canvas.find_withtag("enemy%d" % i):
                        e = True
                        break
                if not e:
                    self.time = self.time + 10 - self.level
                    if self.time < 0:
                        self.time = 0
                    self.level = self.level + 1
                    self.num = int(self.level/2) + 1
                    self.__map.get_role().set_location(1, 1)
                    for i in self.__map.get_enemy():
                        i.set_location(random.randrange(2, 39), random.randrange(1, 19))
                    break
                self.canvas.update()

        self.root.mainloop()

    # 玩家角色
    def draw_role(self):
        role_x = self.__map.get_role().get_location()[0] * self.step
        role_y = self.__map.get_role().get_location()[1] * self.step
        role_coats = self.__map.get_role().get_cloth().create_coats()
        role_pants = self.__map.get_role().get_cloth().create_pants()
        role_shoes = self.__map.get_role().get_cloth().create_shoes()
        self.canvas.create_rectangle(role_x, role_y, role_x + self.step, role_y + self.step / 3, fill=role_coats,
                                     tags="coats")
        self.canvas.create_rectangle(role_x, role_y + self.step / 3, role_x + self.step,
                                     role_y + self.step * 2 / 3, fill=role_pants, tags="pants")
        self.canvas.create_rectangle(role_x, role_y + self.step * 2 / 3, role_x + self.step,
                                     role_y + self.step, fill=role_shoes, tags="shoes")
        self.canvas.create_text(role_x + 8,  role_y - 10, text=self.__map.get_role().get_name(), tags="role_name")

    # 敌人
    def draw_enemy(self):
        for i in range(self.num):

            enemy_x = self.__map.get_enemy()[i].get_location()[0] * self.step
            enemy_y = self.__map.get_enemy()[i].get_location()[1] * self.step
            if self.__map.get_enemy()[i].enemy_type() == "Warrior":
                self.image = Image.open("warrior.png")
            elif self.__map.get_enemy()[i].enemy_type() == "Mage":
                self.image = Image.open("mage.png")
            else:
                self.image = Image.open("monster.png")

            # paned的作用：让每个敌人的图片都显示出来
            paned = tkinter.PanedWindow(self.root)
            paned.pack(fill=tkinter.X, side=tkinter.LEFT)
            paned.im = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(enemy_x+8, enemy_y+8, image=paned.im, tags="enemy%d" % i)
            self.canvas.create_text(enemy_x + 8, enemy_y - 10, text=self.__map.get_enemy()[i].enemy_type(), tags="enemy_name%d" % i)

    # 地图
    def draw_map(self):

        self.root.title(self.__map.get_landform())

        if self.__map.get_landform() == "forest":
            self.canvas = Canvas(self.frame1, bg="#1AFD9C", width=600, height=300)
        else:
            self.canvas = Canvas(self.frame1, bg="#00FFFF", width=600, height=300)

        self.canvas.pack()

    # 移动操作
    def move(self, event):
        opt = OperationFactory.create_operation(event.char)
        opt.role_a = self.__map.get_role()
        opt.role_b = self.__map.get_enemy()[self.num]
        for i in range(self.num):
            if opt.role_a.get_location() == self.__map.get_enemy()[i].get_location():
                opt.role_b = self.__map.get_enemy()[i]
                break
        operation_result = opt.op()
        if operation_result == "you failed":
            messagebox.showinfo("result", "you failed")
            self.root.destroy()
        if operation_result == "attack":
            dead = DecoratorDead(opt.role_b).dead()
            messagebox.showinfo("result", dead)
            self.canvas.delete("enemy%d" % i)
            self.canvas.delete("enemy_name%d" % i)
        if operation_result == "missed attack":
            messagebox.showinfo("result", "missed attack")

    # 更新倒计时
    def update_clock(self):
        now = "Time: %d s" % self.time
        self.label1.configure(text=now)

        if self.time < 1:
            messagebox.showinfo("result", "Game over! Your grades: %d" % self.level)
            self.root.destroy()
        else:
            self.time = self.time - 1
        self.root.after(1000, self.update_clock)
