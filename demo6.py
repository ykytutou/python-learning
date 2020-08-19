# -*- coding : UTF-8 -*-
# @Time : 2020/7/15 0015 3:46 09 PM
# @Author : OliverYin
# @File : demo6.py
# @Software : PyCharm

# 函数


# 定义函数


def printinfo():  # 定义函数前需要两行空行
    print("-"*30)
    print("   人生苦短，我用python   ")
    print("-"*30)

# 函数调用


printinfo()
printinfo()


# 带参数的函数


def add2num(a, b):
    c = a + b
    print(c)


add2num(7, 7)


# 带返回值的函数


def add2number(a, b):
    return a+b         # 通过return来返回运算结果


print(add2number(7, 7))

result = add2number(7, 7)
print(result)


# 返回多个值的函数


def divid(a, b):
    quo = a // b
    remain = a % b
    return quo, remain  # 可同时返回多个结果


q, r = divid(5, 2)      # 需要使用多个值来保存返回内容

print("商：%d, 余数：%d" % (q, r))


# 全局变量和局部变量


def test1():
    a = 300            # 局部变量
    print("test1-----修改前：a = %d" % a)
    a = 100
    print("test1-----修改后：a = %d" % a)


def test2():
    a = 500        # 不同函数可以定义相同变量名字，局部变量彼此无关
    print("test2-----修改前：a = %d" % a)


test1()
test2()


b = 100           # 全局变量


def test3():
    print("test3-----修改前：b = %d" % b)  # 调用全局变量


test3()


# 全局变量和局部变量相同名字

d = 200    # 全局变量


def test4():
    d = 400            # 自己有局部变量，输出局部变量(优先)
    print("test4-----修改前：d = %d" % d)
    d = 100
    print("test4-----修改后：d = %d" % d)


def test5():
    print("test5-----修改前：d = %d" % d)  # 没有变量声明，调用全局变量


test4()
test5()


# 在函数中修改全局变量

e = 200    # 全局变量


def test6():
    global e          # 声明全局变量在函数中的标识符
    print("test6-----修改前：e = %d" % e)
    e = 100           # 修改了全局变量
    print("test6-----修改后：e = %d" % e)


def test7():
    print("test7-----修改前：e = %d" % e)  # 全局变量已被修改


test6()
test7()
