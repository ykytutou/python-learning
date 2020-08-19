# -*- coding : UTF-8 -*-
# @Time : 2020/8/16 0016 2:32 52 PM
# @Author : OliverYin
# @File : TEST.py
# @Software : PyCharm


a = 0
while a < 100:
    a += 1
    if (a % 7 == 0) or ((a - 7) % 10 == 0) or ((a // 10) == 7):
        continue
    else:
        print(a)
