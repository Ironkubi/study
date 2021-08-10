# -*-coding:utf-8 -*-
# File : debug_list.py
# @Time : 2021/7/22 16:17
# @Author : Sf
# version : python 3.7.8


"""列表的用法:访问列表里的值"""

# 访问列表中的值-索引
alist = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print("list[1]读取第二位: ", alist[1])      # 读取第二位
print("list[-1]读取倒数第一位: ", alist[-1])    # 读取倒数第一位
print("list[1:-2]从第二位开始（包含）截取到倒数第二位（不包含）: ", alist[1:-2])   # 从第二位开始（包含）截取到倒数第二位（不包含）
print("\n")



"""列表的用法:函数用法"""

# cmp ：比较两个列表的元素

# len ：列表元素个数

# max ：返回列表元素最大值

# min ：返回列表元素最小值

# list ：将元组转化为列表



"""列表的用法:方法"""


"""列表的用法:高级方法"""

# 方法：

# List.append() 在列表末尾添加新对象
#
# List.count() 统计某个元素在列表中出现的次数
#
# List.extend() 在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#
# List.index() 从列表中找出某个值第一个匹配项的索引位置
#
# List.insert() 将对象插入列表
#
# List.pop() 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#
# List.remove() 移除列表中某个值的第一个匹配项
#
# List.reverse() 反向列表中元素
#
# List.sort() 对原列表进行排序 reverse=False(默认升序)
#
# .join() 将列表转化为字符串



# 实现列表去重的方法-set
alist = [11,12,13,12,14,15,16,13]
a = set(alist)
print("列表去重-set：%s %s" % (type(a), a))
b = [x for x in a]
print("列表去重：" , b)
print("\n")



# 列表解析-[func(x) for x in l1]
alist = [x for x in range(5)]
print("列表解析-打字每个值: ", alist)
l1 = [1,2,3,4]
alist = [ x*2 for x in l1]
print("列表解析-列表乘以2: ", alist)
print("\n")



# 条件列表解析-[x for x in range(100) if x%2 ==0]
# 列表推导式求列表所有奇数并构造新列表
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in alist if i%2==1]
print("条件列表解析-求奇数:", res)
print("\n")



# 嵌套列表解析-交换行列
mat = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
res = [[row[i] for row in mat] for i in (0,1,2)]
print("嵌套列表解析-交换行列: ", res)
print("\n")


# 列表合并-extend
alist = [1,5,7,9]
blist = [2,2,6,8]
alist.extend(blist)   # 合并
print("列表合并-extend:", alist)
alist.sort(reverse=False)   # 排序
print("列表排序-sort: ", alist)
print("\n")


# 列表合并-sum
alist = ['a','b'],['a','b'],['a','b']
res = sum ([[ 'a', 'b' ],['a' , 'b'],[ 'a' ,'b']], [])
print("列表合并-sum: ", res)
print("\n")



# 嵌套列表合并-列表解析
alist = [[1,2],[3,4],[5,6]]
res = [j for i in alist for j in i]
print("嵌套列表合并-列表解析:", res)
print("\n")



# 求两个列表的交集、差集、并集
a = [1,2,3,4]
b = [4,3,5,6]
jj1 = [i for i in a if i in b]
jj2 = list(set(a).intersection(set(b)))
bj1 = list(set(a).union(set(b)))
cj1 = list(set(b).difference(set(b)))
cj2 = list(set(a).difference(set(b)))
print("list-交集：",jj1)
print("list-交集：",jj2)
print("list-并集：",bj1)
print("list-差集：",cj1)
print("list-差集：",cj2)
print("\n")


"""列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求"""
alist = [1,2,3,4,5]
def fn(x):
    return x**2
res = map(fn,alist)
res = [i for i in res if i >10]
print("列表利用map()函数输出: ", res)
print("\n")


# list-join()拼接
x = "abc"
y = "def"
z = ["d","e","f"]
m = x.join(y)
n = x.join(z)
print("list-join()拼接字符串: ", m)
print("list-join()拼接列表: ", n)
print("\n")



# zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表(2.
# x)在（3.
# x)返回一个zip对象

x = [1, 2, 3]

y = [4, 5, 6]

z = [7, 8, 9]

xyz = list(zip(x, y, z))  # 压缩象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
unxyz = zip(*xyz)  # 拆包
print(xyz)
print(list(unxyz))


# zip()函数用法：会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表，同时将这些序列中并排的元素配对。
a = [1,2]
b = [3,4]
res = [i for i in zip(a,b)]
print("list-zip()：", res)

a = (1,2)
b = (3,4)
res = [i for i in zip(a,b)]
print("tuple-zip()：", res)

a = "ab"
b = "xyz"
res = [i for i in zip(a,b)]
print("str-zip()：", res)
print("\n")



# sort和 sorted对列表排序
alist = [0, -1, 3, -10, 5, 9]
alist.sort(reverse=False)
print("list.sort在list基础上修改，无返回值:", alist)

alist = [0, -1, 3, -10, 5, 9]
res = sorted(alist, reverse=False)
print("list.sorted有返回值，是新的list:", alist)
print("返回值:", res)
print("\n")


# list-lambda:从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo,key=lambda x:x)
print("list-lambda从小到大排序:", a)

# list-lambda:正负数从小到大排序
foo = [-5,8,0,4,9,-4,-20,-2,8,2,-4]
a = sorted(foo, key=lambda x:(x<0,abs(x)))
print("list-lambda正负数从小到大排序:", a)
print("\n")

# 列表嵌套字典的排序,分别根据年龄和姓名排序
foo = [{"name":"zs","age":"19"},{"name":"||","age":"54"},{"name":"wa","age":"17"},{"name":"df","age":"23"},]
a = sorted(foo, key=lambda x:x["age"],reverse=True)
print(a)
a = sorted(foo, key=lambda x:x["name"])
print(a)
print("\n")

# 列表嵌套元祖，分别按照字母和数字排序
foo = [("zs",19),("11",54),("wa",17),("df",23)]
a = sorted(foo, key=lambda x:x[1],reverse=True)
print(a)
a = sorted(foo, key=lambda x:x[0])
print(a)
print("\n")

# 列表嵌套列表，年龄数字相同怎么办？
foo = [["zs",19],["11",54],["wa",23],["df",23],["xf",23]]
a = sorted(foo, key=lambda x:(x[1],x[0]),reverse=True)
print(a)
a = sorted(foo, key=lambda x:x[0])
print(a)
print("\n")


# 列表推导式、字典推导式、生成器
import random
td_list = [i for i in range(10)]
print("列表推导式", td_list,type(td_list))
get_list = (i for i in range(10))
print("生成器", get_list)
dic = {k:random.randint(4,9) for k in ["a","b","c","d"]}
print("字典推导式", dict, type(dict))
print("\n")


# 根据字符串长度排序
s = ["ab","abc","a","djkj"]
b =sorted(s, key=lambda x:len(x))
print(b,s)
s.sort(key=len)
print(s)




