# -*- coding : UTF-8 -*-
# @Time : 2020/7/14 0014 12:54 06 PM
# @Author : OliverYin
# @File : demo1.py
# @Software : PyCharm

"""

print("标准化输出字符串")

a = 10

print(a)

print("这是变量：", a)

# 变量是任意的数据类型，变量名必须是大小写英文、数字或下划线，开头不能是数字。

"""

name = 'Oliver'
age = 18

print("我的名字是%s,我的国籍是%d" % ("Oliver", age))  # %s字符串
print("我的年纪是：%d岁" % age)  # %d 有符号十进制整数

print("aaa", "bbb", "ccc")  # 拼接字符串

print("www", "baidu", "com", sep=".")  # 拼接时以 . 进行分割

print("hello", end="")  # 后续直接连接不空格
print("world", end="\t")  # 后续空格 同tab键
print("python", end="\n")  # 后续换行
print("end")
