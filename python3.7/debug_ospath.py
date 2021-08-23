# -*-coding:utf-8 -*-
# File : debug_ospath.py
# @Time : 2021/8/23 9:06
# @Author : Sf
# version : python 3.7.8
import os


# 获取文件所在目录的完整路径
a = os.path.dirname(__file__)
print(a)

# 返回的是.py文件的绝对路径
print(os.path.abspath(__file__))
print(os.path.abspath("."))
print(os.path.abspath(".."))
print(os.path.abspath("曹挣钱"))


