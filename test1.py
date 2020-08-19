# -*- coding : UTF-8 -*-
# @Time : 2020/7/14 0014 4:36 25 PM
# @Author : OliverYin
# @File : test1.py
# @Software : PyCharm

import random

a = int(input("请输入数字：剪刀（0）、石头（1）、布（2）："))
b = random.randint(0, 2)
x = ""
y = ""

if a == 0:
    x = "剪刀"
elif a == 1:
    x = "石头"
elif a == 2:
    x = "布"
print("你出的是：%s（%d）" % (x, a))

if b == 0:
    y = "剪刀"
elif b == 1:
    y = "石头"
elif b == 2:
    y = "布"
print("电脑出的是：%s（%d）" % (y, b))

if a == b:
    print("平局！")
elif ((a - b) == 1) or ((b - a) > 1):
    print("恭喜，你赢了！")
elif ((b - a) == 1) or ((a - b) > 1):
    print("哈哈，你输了！")






