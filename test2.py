# -*- coding : UTF-8 -*-
# @Time : 2020/7/14 0014 6:57 44 PM
# @Author : OliverYin
# @File : test2.py
# @Software : PyCharm

# 9*9乘法表
i = 1
while i <= 9:
    j = 0
    while j <= i:
        j += 1
        if j < i:
            print("%d*%d=%d" % (i, j, i*j), end='\t')
        elif j == i:
            print("%d*%d=%d" % (i, j, i*j), end='\n')
        else:
            break
    i += 1


for m in range(1, 10):
    for n in range(1, 10):
        if m > n:
            print("%s*%s=%s" % (m, n, m*n), end="\t")
        elif m == n:
            print("%s*%s=%s" % (m, n, m*n), end="\n")


m = 0
while m < 9:
    m += 1
    n = 1
    while n <= m:
        print("%d*%d=%d" % (m, n, m*n), end="\t")
        n += 1
    else:
        print(" ")
        continue



