# -*-coding:utf-8 -*-
# File : debug_dict.py
# @Time : 2021/7/22 16:23
# @Author : Sf
# version : python 3.7.8


#python中创建字典的多种方法
dict = {}
dict['key'] = 'value'
dict = {'key': "value", "key2": "value2"}
#dict = dict(key=value, key2=value)


"""字典如何删除键和合并两个字典 del和update方法"""
dic = {"name":"zs", "age":"18"}
dic2 = {"name":"ls"}
del dic["name"]   # del 删除建
print("del 删除字典建：%s \n" % dic)
dic.update(dic2)  # update 合并字典
print("update 合并字典：%s \n" % dic)


"""字典根据键从小到大排序"""
dict = {"name":"zs", "age":18, "city":"深圳", "tel":1362626627}
list = sorted(dict.items(),key=lambda i:i[0],reverse=False)
print("sorted 根据字典键排序", list)
new_dict = {}
for i in list:
    new_dict[i[0]]=i[1]

print("新字典", new_dict)

