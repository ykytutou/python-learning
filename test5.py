# -*- coding : UTF-8 -*-
# @Time : 2020/7/15 0015 8:43 15 PM
# @Author : OliverYin
# @File : test5.py
# @Software : PyCharm

# 解法一
"""
f = open("shi.txt", "w", encoding="utf-8")
f.write("床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。")
f.close()


def copyshi():
    fi = open("shi.txt", "r")
    shi = fi.readlines()
    fi.close()
    print(shi)
    fi2 = open("copy.txt", "w")
    for i in shi:
        fi2.write(i)
    fi2.close()
    print("复制完毕")


copyshi()
"""

# 解法二


def readfile(filename):
    f = open(filename, "r")
    content = f.readlines()
    f.close()
    return content


def writefile(filename, content):
    f = open(filename, "w", encoding="GBK")
    for i in content:
        f.write(i)
    f.close()


gushi = "床前明月光，\n疑是地上霜。\n举头望明月，\n低头思故乡。"

writefile("gushi.txt", gushi)

content = readfile("gushi.txt")

writefile("copy3.txt", content)





