# -*- coding : UTF-8 -*-
# @Time : 2020/8/12 0012 8:50 21 PM
# @Author : OliverYin
# @File : scripttest.py
# @Software : PyCharm

import re

pattern = re.compile('c')
print(pattern.match('comcdc').group())

pattern = re.compile('1')
print(pattern.search('abcdefg1').group())