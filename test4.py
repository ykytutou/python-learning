# -*- coding : UTF-8 -*-
# @Time : 2020/7/15 0015 4:14 19 PM
# @Author : OliverYin
# @File : test4.py
# @Software : PyCharm

# 1.写一个打印一条横线的函数。 提示：横线是若干个“-”组成


def printline():
    print("-"*30)
printline()

# 2.写一个函数，可以通过输入的参数，打印出自定义行数的横线。（调用1.中函数）


# def printnline():
#     n = int(input("请输入行数："))
#     for i in range(0, n):
#         printline()
# printnline()


def printnline(n):
    i = 0
    while i < n:
        printline()
        i += 1
printnline(3)

# 3.写一个函数求三个数的和


def sum3num(a, b, c):
    sum3 = a + b + c
    print(sum3)
    return sum3
sum3num(1, 2, 3)


# 4.写一个函数求三个数的平均值（提示：调用上面的函数）

def aver3num(a, b, c):
    sum3 = sum3num(a, b ,c)
    aver = sum3 / 3.0
    print(aver)
    return  aver
aver3num(10, 20, 30)