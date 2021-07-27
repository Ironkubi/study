# -*-coding:utf-8 -*-
# File : debug_re.py
# @Time : 2021/7/22 16:32
# @Author : Sf
# version : python 3.7.8


"""字符串a ="not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"""""
import re
a = "not 404 found 张三 99 深圳"
list = a.split(" ")  #
print(list)
res = re.findall('\d+|[a-zA-Z]+', a)   # 匹配数字与单词
for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)
print(res)
print(new_str)


b = "not 404 50.56 found 张三 99 深圳"
list = b.split(" ")  #
print(list)
res = re.findall('\d+\.?\d*|[a-zA-Z]+', b)  # 匹配小数、数字与单词
for i in res:
    if i in list:
        list.remove(i)
new_str = " ".join(list)
print(res)
print(new_str)



"""正则表达式匹配中，（.*）和（.*?）匹配区别？
（.* ）是贪婪匹配，会把满足正则的尽可能多的往后匹配
（.* ?）是非贪婪匹配，会把满足正则的尽可能少匹配"""
s = "<a>哈哈</a><a>呵呵</a>"
import re
res1 = re.findall("<a>(.*)</a>", s)
print("贪婪匹配", res1, "\n")
res2 = re.findall("<a>(.*?)</a>", s)
print("非贪婪匹配", res2, "\n")





