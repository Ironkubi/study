# -*-coding:utf-8 -*-
# # File : debug_tuple.py
# # @Time : 2021/8/10 15:53
# # @Author : Sf
# # version : python 3.7.8

print("===》元祖索引：利用索引访问元祖元素")
tup1 = ('Google', 'Runoob', 1997, 2000)
print("元祖操作前tup1：", tup1)
tup2 = (1, 2, 3, 4, 5, 6, 7)
print("元祖操作前tup2：", tup2)
print("元祖访问-tup1[0]: ", tup1[0])
print("元祖访问-tup1[-1]: ", tup1[-1])
print("元祖访问-tup2[1:5]: ", tup2[1:5])
print("\n")


print("===》修改元祖：元组中的元素值是不允许修改的，但我们可以对元组进行连接组合")
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
print("元祖操作前tup1：", tup1)
print("元祖操作前tup2：", tup2)

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2
print("元祖不能修改，只能合并：",tup3)
print("\n")


print("===》删除元祖：元组中的元素值是不允许删除的，但我们可以使用del语句来删除整个元组")
tup1 = ('Google', 'Runoob', 1997, 2000)
print("元祖操作前tup：", tup1)
del tup1
print("元祖不能删除元素值，可删除整个元组del tup1 : ")
print("\n")


print("===》元祖长度：len()")
tup1 = ('Google', 'Runoob', 'Taobao')
print("元祖操作前tup：", tup1)
print("元祖长度-len(tup1)：", len(tup1))
print("\n")


print("===》元祖最大值：max()")
tup1 = ('5', '4', '8')
print("元祖操作前tup：", tup1)
print("元祖最大值-max(tup1)：", max(tup1))
print("\n")


print("===》元祖最小值：mix()")
tup1 = ('5', '4', '8')
print("元祖操作前tup：", tup1)
print("元祖最小值-min(tup1)：", min(tup1))
print("\n")


print("===》元祖转化：将可迭代系列转换为元组")
alist = ['Google', 'Taobao', 'Runoob', 'Baidu']
print("列表操作前：", alist)
atuple = tuple(alist)
print("列表转化为元祖：", atuple)
print("\n")














