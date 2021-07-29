# -*-coding:utf-8 -*-
# File : debug_list.py
# @Time : 2021/7/22 16:17
# @Author : Sf
# version : python 3.7.8



# 访问列表中的值
list1 = ['red', 'green', 'blue', 'yellow', 'white', 'black']
print("list1[1]: ", list1[1])      # 读取第二位
print("list1[-1]: ", list1[-1])    # 读取倒数第一位
print("list1[1:-2]: ", list1[1:-2])   # 从第二位开始（包含）截取到倒数第二位（不包含）



"""实现列表去重的方法"""
list2 = [11,12,13,12,14,15,16,13]
a = set(list2)
print("列表去重-先转为set：%s %s" % (type(a), a))
b = [x for x in a]
print("列表去重：%s \n" % a)



"""列表推导式求列表所有奇数并构造新列表"""
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = [i for i in a if i%2==1]
print("列表推导式求列表所有奇数并构造新列表:", res, "\n")



"""列表[1,2,3,4,5],请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]
map（）函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求"""
list4 = [1,2,3,4,5]
def fn(x):
    return x**2
res = map(fn,list2)
res = [i for i in res if i >10]
print("列表利用map()函数输出: %s \n" % res)



"""列表合并"""
list5 = [1,5,7,9]
list6 = [2,2,6,8]
list5.extend(list6)   # 合并
print("列表合并:", list5)
list5.sort(reverse=False)   # 排序
print("列表排序:", list5, "\n")


"""[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5]"""
list7 = [[1,2],[3,4],[5,6]]
x = [j for i in list7 for j in i]
print("多列表展开为一个列表:",x)


# 求两个列表的交集、差集、并集
a = [1,2,3,4]
b = [4,3,5,6]
jj1 = [i for i in a if i in b]
jj2 = list(set(a).intersection(set(b)))
bj1 = list(set(a).union(set(b)))

cj1 = list(set(b).difference(set(b)))
cj2 = list(set(a).difference(set(b)))
print("交集：",jj1)
print("交集：",jj2)
print("并集：",bj1)
print("差集：",cj1)
print("差集：",cj2)


