# -*-coding:utf-8 -*-
# File : debug_list.py
# @Time : 2021/7/22 16:17
# @Author : Sf
# version : python 3.7.8


"""列表的用法:访问列表里的值"""

print("===》列表索引：利用索引访问列表元素")
alist = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print("列表操作前：", alist)
print("列表访问-list[1]， 读取第二位: ", alist[1])      # 读取第二位
print("列表访问-list[-1]， 读取倒数第一位: ", alist[-1])    # 读取倒数第一位
print("列表访问-list[1:-2]， 从第二位开始（包含）截取到倒数第二位（不包含）: ", alist[1:-2])   # 从第二位开始（包含）截取到倒数第二位（不包含）
print("\n")



"""列表的用法:函数用法"""

print("===》列表比较：operator 返回布尔值")
import operator
a = [1, 2]
b = [1, 3]
print("列表操作前a:", a)
print("列表操作前b:", b)
print("列表比较-operator.lt(a, b)，a < b: ", operator.lt(a, b))
print("列表比较-operator.le(a, b)，a <= b: ", operator.le(a, b))
print("列表比较-operator.eq(a, b)，a == b: ", operator.eq(a, b))
print("列表比较-operator.ne(a, b)，a != b: ", operator.ne(a, b))
print("列表比较-operator.ge(a, b)，a > b: ", operator.ge(a, b))
print("列表比较-operator.gt(a, b)，a >= b: ", operator.gt(a, b))
print("\n")


print("===》列表长度：len()")
alist = ['Google', 'Runoob', 'Taobao']
print("列表操作前：", alist)
print ("列表长度-len(list): ", len(alist))
blist=list(range(5)) # 创建一个 0-4 的列表
print ("列表长度-len(list(range(5))): ", len(blist))
print("\n")


print("===》列表最大值：max()")
alist, blist = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
print("列表操作前alist：", alist)
print("列表操作前blist：", blist)
print ("列表最大值：max(alist) : ", max(alist))
print ("列表最大值：max(blist) : ", max(blist))

print("===》列表中元素为字符串的时候，max函数的比较是根据id的大小来判断的。")
alist = ['我', '爱', 'python']
blist = [100, 200, 300]
print("列表操作前alist：", alist)
print("列表操作前blist：", blist)
print('列表最大值：max(alist):', max(alist))
print('列表最大值：max(blist):', max(blist))
print("id(alist[0])：", id(alist[0]))
print("id(alist[1])：", id(alist[1]))
print("id(alist[2])：", id(alist[2]))
print("'我' > '爱':", '我' > '爱')
print("'爱' > 'python':", '爱' > 'python')
print("'我' > 'python':", '我' > 'python')
print("\n")



print("===》列表最小值：min()")
alist, blist = ['Google', 'Runoob', 'Taobao'], [456, 700, 200]
print("列表操作前alist：", alist)
print("列表操作前blist：", blist)
print ('列表最大值：min(alist):', min(alist))
print ('列表最大值：min(blist):', min(blist))
print("\n")


print("===》列表转化：list()")
aTuple = (123, 'Google', 'Runoob', 'Taobao')
print("tuple操作前：", aTuple)
list1 = list(aTuple)
print ("列表转化-list(tuple): ", list1)

str="Hello World"
print("str操作前：", str)
list2=list(str)
print ("列表转化-list(str): ", list2)
print("\n")



"""列表的用法:方法"""

print("===》List.append():在列表末尾添加新对象")
alist = ['Google', 'Runoob', 'Taobao']
print("列表操作前alist：", alist)
list1.append('Baidu')
print ("List.append('Baidu')更新后的列表 : ", alist)
print("\n")


#
print("===》List.count():统计某个元素在列表中出现的次数")
aList = [123, 'Google', 'Runoob', 'Taobao', 123]
print("列表操作前alist：", alist)
print ("List.count()统计某个元素在列表中出现的次数，123 元素个数 : ", aList.count(123))
print ("List.count()统计某个元素在列表中出现的次数，Runoob 元素个数 : ", aList.count('Runoob'))
print("\n")


print("===》List.extend():在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）")
print("语法： list.extend(seq)")
print("参数: seq -- 元素列表，可以是列表、元组、集合、字典，若为字典,则仅会将键(key)作为元素依次添加至原列表的末尾。")
language = ['French', 'English', 'German']
print("列表操作前language：", language)
language_list = ['USA']
print("列表操作前language_list：", language_list)
language_tuple = ('Spanish', 'Portuguese')
print("元祖操作前language_tuple：", language_tuple)
language_set = {'Chinese', 'Japanese'}
print("集合操作前language_set：", language_set)
# 添加列表元素到列表末尾
language.extend(language_list)
print('List.extend(language_list)追加列表，新列表: ', language)
# 添加元组元素到列表末尾
language.extend(language_tuple)
print('List.extend(language_tuple)追加元祖，新列表: ', language)
# 添加集合元素到列表末尾
language.extend(language_set)
print('List.extend(language_set)追加集合，新列表: ', language)
print("\n")


# List.index() 从列表中找出某个值第一个匹配项的索引位置
print("语法： list.index(x[, start[, end]])")
print("参数: x-- 查找的对象")
print("参数: start-- 可选，查找的起始位置")
print("参数: end-- 可选，查找的结束位置")
list1 = ['Google', 'Runoob', 'Taobao', 'Facebook', 'QQ']
print ('List.index()找出某个元素索引的位置，Runoob 索引值为', list1.index('Runoob'))
print ('List.index()找出某个元素索引的位置，Taobao 索引值为', list1.index('Taobao'))
# 从指定位置开始搜索
print ('List.index()找出某个元素索引的位置，Runoob 索引值为', list1.index('Runoob',1))
print("\n")


# List.insert() 将对象插入列表
print("语法 list.insert(index, obj)")
print("参数 index -- 对象obj需要插入的索引位置")
print("参数 obj -- 要插入列表中的对象")
list1 = ['Google', 'Runoob', 'Taobao']
list1.insert(1, 'Baidu')
print ('List.insert()按照索引插入元素，新列表 : ', list1)
print("\n")


# List.pop() 移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print("语法 list.pop([index=-1])")
print("参数 index -- 可选参数，要移除列表元素的索引值，不能超过列表总长度，默认为 index=-1，删除最后一个列表值")
list1 = ['Google', 'Runoob', 'Taobao']
list_pop = list1.pop()
print ("List.pop()删除的项为 :", list_pop)
print ("List.pop()列表现在为 : ", list1)
list_pop = list1.pop(1)
print ("List.pop(1)删除的项为 :", list_pop)
print ("List.pop(1)列表现在为 : ", list1)
print("\n")


# List.remove() 移除列表中某个值的第一个匹配项
print("语法 list.remove(obj)")
print("参数 obj -- 列表中要移除的对象")
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.remove('Taobao')
print ("List.remove('Taobao')列表现在为 : ", list1)
list1.remove('Baidu')
print ("List.remove('Baidu')列表现在为 : ", list1)
print("\n")


# List.reverse() 反向列表中元素
print("语法 list.reverse()")
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.reverse()
print ("List.reverse()列表反转后: ", list1)
print("\n")


# List.sort() 对原列表进行排序 reverse=False(默认升序)
print("语法 list.sort( key=None, reverse=False)")
print("参数 key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序")
print("参数 reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）")
aList = ['Google', 'Runoob', 'Taobao', 'Facebook']
aList.sort()
print("List.sort()升序输出List: ", aList)

vowels = ['e', 'a', 'u', 'o', 'i']
vowels.sort(reverse=True)
print('List.sort(reverse=True) 降序输出list:', vowels)


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]

# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

# 输出类别
print('List.sort(key=args)指定列表中的元素排序来输出列表：', random)
print("\n")


# list.clear() 清空列表
print("语法 list.clear()")
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list1.clear()
print ("list1.clear() 列表清空后 : ", list1)
print("\n")

# list.copy() 复制列表
print("语法 list.copy()")
list1 = ['Google', 'Runoob', 'Taobao', 'Baidu']
list2 = list1.copy()
print ("list.copy() list2复制list1列表: ", list2)
print("\n")

# .join() 将列表转化为字符串
print("语法")
print("参数 ")
print("\n")



"""列表的用法:高级方法"""

print("===》列表去重：-set()")
alist = [11,12,13,12,14,15,16,13]
a = set(alist)
print("列表去重set()后类型：", type(a))
print("列表去重set()为集合:", a)
b = [x for x in a]
print("列表去重列表解析：" , b)
print("\n")


print("===》列表解析：[func(x) for x in list]")
alist = [x for x in range(5)]
print("列表解析-输出元素: ", alist)
l1 = [1,2,3,4]
alist = [ x*2 for x in l1]
print("列表解析-列表乘法: ", alist)
print("\n")


print("===》列表解析：[x for x in range(100) if x%2 ==0]，列表推导式求列表所有奇数并构造新列表")
alist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in alist if i%2==1]
print("条件列表解析-求奇数:", res)
print("\n")


print("===》列表解析：嵌套列表解析-交换行列")
mat = [[1, 2, 3],[4, 5, 6], [7, 8, 9]]
print("嵌套列表解析前: ", mat)
res = [[row[i] for row in mat] for i in (0,1,2)]
print("嵌套列表解析后-交换行列: ", res)
print("\n")


print("===》列表合并：sum()")
alist = ['a','b'],['a','b'],['a','b']
print("列表合并前：", alist)
res = sum ([[ 'a', 'b' ],['a' , 'b'],[ 'a' ,'b']], [])
print("列表合并后-sum: ", res)
print("\n")



# 嵌套列表合并-列表解析
print("===》列表解析：嵌套列表合并-列表解析")
alist = [[1,2],[3,4],[5,6]]
print("嵌套列表合并-列表解析前:", alist)
res = [j for i in alist for j in i]
print("嵌套列表合并-列表解析后:", res)
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




