# -*- coding : UTF-8 -*-

# @Time : 2020/7/14 0014 4:06 50 PM
# @Author : OliverYin
# @File : demo3.py
# @Software : PyCharm

# if True
"""
if True :  # 非零即可， false可写为0 或 none
    print("True")  # 此行开头缩进表示从属（缩进尺寸必须统一）
    print("Answer")
else :
    print("False")

print("end")
"""

# elif
'''
score = 87

if score >= 90 and score <= 100:  
    print("本次考试，等级为A")
elif score >= 80 and Score <90:
    print("本次考试，等级为B")
else :
    print("本次考试，等级为E")
'''

import random  # 引入随机库

x = random.randint(0, 2)  # 随机生成[0,2]的随机数，三个数字

'''
import module  引入模块、库

from module import function  从某模块中引入某个函数

from module import function1,function2,function3   引入多个函数

from module import \*  将某个模块的全部函数导入

'''

# for...in循环
'''
for i in range(5):  # 0 1 2 3 4 五个数字 默认从0开始
    print(i)

for j in range(0, 11, 3):  # 从0开始，到11结束，步进值为3 即每次加3
    print(j)

for k in range(-10, -100, -30):
    print(k)

name = "shanghai"   # 遍历字符串
for x in name:
    print(x, end="\t")


a = ["aa", "bb", "cc", "dd"]    # 遍历数组、列表 
for i in range(len(a)):    # len(a)是求数组a的长度，即0~3 长度4
    print(i, a[i], end="\t")
'''

# while循环
'''
i = 0
while i < 5:
    print("当前是第%d次执行循环" % (i+1))
    print("i = %d" % i)
    i += 1
'''

'''
# 1~100求和
i = 1
n = 100
sum_ = 0
while i < 101:
    sum_ += i
    i += 1

# print("1~%d的和是%d" %(n, sum_))   # %d 占位符
# print(f'1~{n}的和是{sum_}')   # python3.6开始 F-string 方面快捷（和Ruby、ES6类似）
'''


'''
# format() 是专门用来 格式化字符串 的函数，它最常用的功能就是「插入数据」和「数字格式化」。 
# 插入数据：

name = input('请输入姓名：')
age = input('请输入年龄')

print('你叫'+name+'，今年' + age + '岁了')
# 或者
print('你叫{}，今年{}岁了'.format(name,age))
# {} 为占位符


# 数字格式化：
# format() 的第二种常用功能，是格式化数字，比如我们要输出圆周率，但只保留两位小数，可以这么写：
print("{:.2f}".format(3.1415926))
# 如果要保留三位，则改成 {:.3f}；不带小数，则改成 {:.0f}，依次类推。
'''


'''

count = 0
while count < 5:
    print(count, "小于5")
    count += 1
else:                            # 可用else
    print(count, "大于或等于5")
'''

# break continue pass用法
'''
i = 0
while i < 10:
    i = i+1
    print("-"*30)
    if i == 5:
        break       # 跳出循环体    
    print(i)                     
'''

i = 0
while i < 10:
    i = i+1
    print("-"*30)
    if i == 5:
        continue      # 跳过当前循环，进入下一轮循环(不打印 5 )
    print(i)

# pass 空语句，用作占位语句，不做任何事
