# -*- coding : UTF-8 -*-
# @Time : 2020/7/15 0015 7:02 18 PM
# @Author : OliverYin
# @File : demo7.py
# @Software : PyCharm

# 文件操作
"""
f = open("test.txt", "w")   # 在当前目录下打开test.txt ，w（write）:如果没有就新建
# f = open("test.txt")      # 默认读取 r 模式，没有文件就报错
f.write("hello world!")     # 写入文件
f.close()  # 关闭文件
"""

'''
# read方法 读取指定字符 开始定位在文件头部，每执行一次向后移动指定字符
f = open("test.txt", "r")
content = f.read(5)  # 读5个字符
print(content)
content = f.read(6)  # 依次再读6个字符
print(content)
f.close()

# readlines方法
f = open("test.txt", "r")
content = f.readlines()  # 一次性读取整个文件（读完）为列表，每行一个字符串元素
print(content)

i = 1
for temp in content:
    print("%d:%s" % (i, temp))
    i += 1
f.close()

print("\n")
print("-"*30)


# readline方法   一行一行读取
f = open("test.txt", "r")
content = f.readline()
print("1:%s" % content, end="")

content = f.readline()
print("2:%s" % content)
f.close()
'''


import os   # os模块

# os.rename("*.txt", "**.txt")  # 重命名

# os.remove("*.txt")    # 删除文件

# os.mkdir("filename")  # 创建文件夹

# os.getcwd()           # 创建文件夹

# os.chdir("../")       # 改变默认目录

# os.lisdir("./")       # 获取目录列表

# os.rmdir("filename")  # 删除文件夹


# 错误和异常

# 错误Error
''' 
print("-----test - 1-----")
f = open("123.txt", "r")     # 用只读打开不存在的文件，报错
print("-----test - 2-----")  # 此行代码不执行
'''

# 将错误Error 进行处理 -> 异常

# 捕获异常
'''
try:
    print("-----test - 1-----")
    f = open("123.txt", "r")
    print("-----test - 2-----")
except IOError:                 # 排除IO异常（根据Error类型捕获）
    pass                        # 捕获后 进行的操作

try:
    print("-----test - 1-----")
    f = open("123.txt", "r")
    print("-----test - 2-----")

    print(num)                  # num未定义 属于NameError
except (IOError, NameError):    # 排除多种异常（使用括号与逗号）
    print("产生错误")
'''

# 获取错误描述（将错误信息打印出来）
'''
try:
    print("-----test - 1-----")
    f = open("123.txt", "r")              # [Errno 2] No such file or directory: '123.txt'
    print("-----test - 2-----")

    print(num)                            # name 'num' is not defined
except (IOError, NameError) as result:    # 保存错误信息
    print("产生错误")
    print(result)
'''

# 捕获所有异常 Exception
'''
try:
    print("-----test - 1-----")
    f = open("123.txt", "r")              # [Errno 2] No such file or directory: '123.txt'
    print("-----test - 2-----")

    print(num)                            # name 'num' is not defined
except Exception as result:    # Exception 承接所有异常
    print("产生错误")
    print(result)
'''

# try ... finally 和嵌套

try:
    f = open("test.txt", "r")
    print(num)                 # NameError
except Exception as result:
    print("发生异常")
finally:
    f.close()
    print("文件关闭")


import time
try:
    f = open("123.txt", "r")
    try:
        while 1:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(2)
            print(content)
    finally:
        f.close()
        print("文件关闭")
except Exception as result:
    print("发生异常")



