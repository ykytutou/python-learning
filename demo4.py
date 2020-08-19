# -*- coding : UTF-8 -*-
# @Time : 2020/7/14 0014 8:25 59 PM
# @Author : OliverYin
# @File : demo4.py
# @Software : PyCharm
"""
# 字符串拼接和截取

str_ = "shanghai"

print(str_)
print(str_[0:5])   # 截取str_ 前5个字符 （包前不包后）
print(str_[4])    # 截取单个字符
print(str_[0:8:2])   # [起始位置:结束位置:步进值]

# 简写
print(str_[:5])  # （包前不包后）
print(str_[5:])  # （包前不包后）

print(str_ + "，你好")
print((str_ + " ") * 3)

print("hello\nshanghai")   # 转义字符有效
print(r"hello\nshanghai")  # r"" 直接显示转义字符
"""

'''
# List（列表）
# namelist = []  定义一个空的列表
namelist = ["小张", "小王", "小李"]
testlist = ["测试", 1]   # 列表中可以存储混合类型

print(type(testlist[0]))  # 保持固有类型存储
print(type(testlist[1]))  # 保持固有类型存储

print(namelist[0])
print(namelist[1])
print(namelist[2])
print(testlist[0])
print(testlist[1])

# 遍历 循环输出
for name in namelist[1:]:
    print(name)

print(len(namelist))

len_ = len(namelist)

i = 0
while i < len_:
    print(namelist[i])
    i += 1
'''


# 列表的数据操作


# 增加: [append]、[extend]、[insert]

'''
namelist = ["小张", "小王", "小李"]
print("-----增加前，名单列表的数据-----")
for name in namelist:
    print(name)

nametemp = input("请输入添加的人员姓名：")
namelist.append(nametemp)     # 在列表末尾增加一个元素

print("-----增加后，名单列表的数据-----")
for name in namelist:
    print(name)
'''

# [append]
'''
a = [1, 2]
b = [3, 4]
a.append(b)   # 将列表b作为一个整体的元素，加入到a列表中
print(a)
'''
# [extend]
'''
a = [1, 2]
b = [3, 4]
a.extend(b)   # 将b列表中每一个元素，逐一追加到a列表中
print(a)
'''
# [insert]
'''
a = [0, 1, 2]
a.insert(1, 3)  # 第一个变量表示下标，第二个表示元素（对象）
print(a)        # [0, 3, 1, 2]
'''


# 删除: [del]、[pop]、[remove]

'''
movielist = ["哈利波特", "指环王", "星际穿越", "黑天鹅"]

print("-----删除前，电影列表的数据-----")
for name in movielist:
    print(name)

del movielist[2]    # 在指定位置删除一个元素
movielist.pop()     # 弹出末尾最后一个元素
movielist.remove("指环王")  # 直接删除指定内容的元素（如果有重复内容，只会删除找到的第一个）

print("-----删除后，电影列表的数据-----")
for name in movielist:
    print(name)
 '''

# 修改: []

'''
namelist = ["小张", "小王", "小李"]
print("-----增加前，名单列表的数据-----")
for name in namelist:
    print(name)

namelist[1] = "小红"     # 修改指定下标元素内容

print("-----增加后，名单列表的数据-----")
for name in namelist:
    print(name)
'''

# 查询: [in, not in]

'''
namelist = ["小张", "小王", "小李"]

findName = input("请输入要找的人员姓名：")

if findName in namelist:
    print(f"名单中有{findName}")
else:
    print(f"名单中没有{findName}")
'''

# index
mylist = ["a", "b", "c", "a", "b"]
print(mylist.index("c", 0, 4))       # index查找指定范围内的元素，并返回对应元素下标
                                     # index查找不在范围内的元素，会报错

# count
print(mylist.count("a"))    # 统计元素出现了几次

# 排序

a = [1, 4, 2, 3]
print(a)
a.reverse()      # reverse将列表所有元素反转
print(a)

a.sort()         # sort 升序
print(a)
a.sort(reverse=True)   # sort(reverse=True) 降序
print(a)

# 列表嵌套

schoolNames = [[], [], []]    # 有一个空列表，每个元素也是一个空列表

schoolName = [["格兰", "芬多"], ["赫奇", "帕奇"], ["拉", "文克", "劳"], ["斯莱特林"]]

print(schoolName[0][1])  # 打印嵌套列表元素 （二维参数）
