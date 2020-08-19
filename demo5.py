# -*- coding : UTF-8 -*-
# @Time : 2020/7/15 0015 11:44 10 AM
# @Author : OliverYin
# @File : demo5.py
# @Software : PyCharm

# 元组 tuple
"""
tup1 = ()   # 创建空的元组
print(type(tup1))

# tup2 = (50)   # <class 'int'>   只是一个整型

tup2 = (50, )   # <class 'tuple'>
print(type(tup2))

tup3 = (50, 60, 70)
"""

'''
tup1 = ("abc", "def", 200, 2000, 333, 444, 555)

print(tup1[0])
print(tup1[-1])
print(tup1[1:5])  # 同样左闭右开进行切片
'''
# -----------------------------------------
# 增（新建、连接）
'''
tup1 = (12, 34, 56)
tup2 = ("abc", "xyz")
tup3 = tup1 + tup2
print(tup3)
'''
# -----------------------------------------
# 删（不能删除单个元素）
'''
tup1 = (12, 34, 56)
print(tup1)
del tup1           # 直接删除了整个元组变量
print("删除后：")
print(tup1)
'''
# -----------------------------------------
# 改（不允许修改）

# tup1 = (12, 34, 56)
# tup1[0] = 100          # 报错！！！
# -----------------------------------------
# 查（访问、切片）


# 字典 dict
# 以键值对形式储存  key-value

# info = {"name": "印可阳", "age": 25}   # 字典的定义

# 字典的访问
# print(info["name"])
# print(info["age"])

# 访问不存在的key
# print(info["gender"])  # 未知时，直接访问会报错

# print(info.get("gender"))  # 使用get方法，未找到时返回：None

# print(info.get("gender", "male"))  # get方法:未找到时还可设置返回的默认值

# print(info.get("age", "male"))  # get方法:找到的时候还还是返回原来值


# -----------------------------------------
# 增

'''
info = {"name": "印可阳", "age": 25}
newID = input("输入新的学号：")
info["id"] = newID
print(info["id"])
'''

# -----------------------------------------
# 删 [del]、[clear]

# [del] 删除
# info = {"name": "印可阳", "age": 25}
# print("删除前：%s" % info["name"])
# del info["name"]
# print("删除后：%s" % info["name"])  # 删除键值对后，访问报错

# info = {"name": "印可阳", "age": 25}
# print("删除前：%s" % info)
# del info
# print("删除后：%s" % info)  # 删除整个字典后，访问报错

# [clear] 清空
# info = {"name": "印可阳", "age": 25}
# print("删除前：%s" % info)
# info.clear()
# print("删除后：%s" % info)  # 清空整个字典，字典仍存在

# -----------------------------------------
# 改

# info = {"name": "印可阳", "age": 25}
# info["age"] = 20
# print(info["age"])

# -----------------------------------------
# 查

info = {"id": 1, "name": "印可阳", "age": 25}

'''
print(info.keys())  # 得到所有的键（列表形式）

print(info.values())  # 得到所有的值（列表形式）

print(info.items())  # 得到所有的项（元组形式），每个键值对是一个元组元素
'''

# 遍历所有的键
for key in info.keys():
    print(key)

# 遍历所有的值
for value in info.values():
    print(value)

# 遍历所有的项（键值对）
for key, value in info.items():
    print("key=%s, value=%s" % (key, value))

mylist = ["a", "b", "c", "d", ]

for x in mylist:   #遍历
    print(x)

print(enumerate(mylist))  # 枚举函数，列出数据和下标，需要接收

for i, x in enumerate(mylist):
    print(i+1, x)


# set 集合
# set和dict类似，也是一组key的集合，但是不存储value。key不能重复。
# set是无序的，重复元素会被自动过滤

# ————————————————————————————————————————————————————
# 列表[]         有序               可变类型

# 元组()         有序               内容不可变

# 字典{}         无序               key不可变，value可变

# 集合{}         无序               可变类型（不重复）
# ————————————————————————————————————————————————————
