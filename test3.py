# -*- coding : UTF-8 -*-
# @Time : 2020/7/14 0014 11:52 24 PM
# @Author : OliverYin
# @File : test3.py
# @Software : PyCharm

# 三个办公室 八个老师  随机分配到办公室 并且打印

""""
import random

namelist = ["A", "B", "C", "D", "E", "F", "G", "H"]

officelist = [[], [], []]

numlist = []

for name in namelist:
    numlist.append(random.randint(0, 2))
print(numlist)
print("-"*30)

for j in range(0, 8):
    officelist[numlist[j]].append(namelist[j])
print(officelist)
print("-"*30)

num = [numlist.count(0), numlist.count(1), numlist.count(2)]
for k in range(0, 3):
    print(f"办公室{k + 1}中有{num[k]}个老师")
    print("其中老师有:")
    for name in officelist[k]:                   # print(f"其中老师有{officelist[k]}")
        print(f"{name}", end=" ")
    print("\r")
    print("-" * 30)
"""

# 商品购买

products = [["iphone", 6888], ["MacPro", 14800], ["Xiaomi6", 2499], ["Coffee", 31], ["Book", 60], ["Nike", 699]]

num = len(products)  # print(num)

'''
print("----- 以下为商品列表 -----")
for i in range(0, num):
    print(f'{i} {products[i][0]}  {products[i][1]}')
    i += 1
print("----- 以上为商品列表 -----")
'''

print("----- 以下为商品列表 -----")
i = 0
for product in products:
    print("%-3s%-10s%s" % (i, product[0], product[1]))
    i += 1
print("----- 以上为商品列表 -----")
print("\n")

shoplist = list()  # 申明一个空列表

while 1:
    print("加入购物车请输入商品编号，退出选购请输入q")
    input_ = input("请输入：")
    if input_.isdigit() and (0 <= int(input_) <= 5):
        shoplist.append(products[int(input_)])
        continue
    elif input_ == "q":
        break
    else:
        print("输入错误，请重新输入")
        continue

print("\n")
print("----- 以下为您要购买的商品 -----")
j = 1
price = 0
for shop in shoplist:
    print("%-3s%-10s%s" % (j, shop[0], shop[1]))
    j += 1
    price += int(shop[1])
print("-"*30)
print(f"TotalPrice:  {price}")
print("----- 以上为您要购买的商品 -----")

