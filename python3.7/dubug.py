# -*-coding:utf-8 -*-
# File : dubug.py
# @Time : 2021/7/22 11:18
# @Author : Sf
# version : python 3.7.8



"""一行带实现1-100之和"""
sum = sum(range(0, 100))
print("实现1-100之和：%s \n" % sum)



"""python中生成随机整数、随机小数、0--1之间小数方法
随机整数：random.randint(a,b),生成区间内的整数
随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数
0-1随机小数：random.random(),括号中不传参"""
import random
import numpy as np
result = random.randint(10,20)
print("随机生成区间内的整数: %s \n" % result)
result1 = np.random.randn(5)
print("随机生成5个随机小数: %s \n" % result1)
result2 = random.random()
print("随机生成0-1随机小数: %s \n" % result2)



"""字符串去重并重小到大排序输出"""
str = "ajldjlajfdljkogfdd"
str = set(str)
str = list(str)
str.sort(reverse=False)
res = "".join(str)
print("字符串去重并重小到大排序输出: %s \n" % res)



"""用lambda 函数实现两个数据相乘"""
sum = lambda a,b :a*b
print("字符串去重并重小到大排序输出:", sum(5,4),"\n")



"""统计字符串中每个字符出现的次数"""
a = "a;lskdh!`foiegn``as;ldnf,asd.121,2ljladsfkja`sdijfhaosjlfd,gjsdfg.as.dl"
# 1) 使用方法库
from collections import Counter
b = Counter(a)
print(b)

# 2) 使用字典处理
dict_ = {}
for i in a:
    if i in dict_:
        dict_[i] += 1
    else:
        dict_[i] = 1
print(dict_)







