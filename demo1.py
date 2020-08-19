# -*- coding : UTF-8 -*-
# @Time : 2020/7/14 0014 12:54 06 PM
# @Author : OliverYin
# @File : demo1.py
# @Software : PyCharm

#这是我的第一个python程序
print("hello,world!")       #这是单行注释

'''
这是第一行注释
这是第二行注释

'''

print("python")

'''
password = input("请输入密码：")
print("您刚才输入的密码是：", password)
'''

a = 10
print(type(a))  # 查看变量类型
b = "Oliver"
print(type(b))

c = input("输入：")
print(type(c))

print("输入了一个数字：%s" % c)  # input输入类型是字符串

d = int("123")  # 类型转换 字符串->整型
print(type(a))
e = d + 100
print(b)


f = int(input("输入f："))
print("输入一个数字：%d" % f)  # input转换成了整型

