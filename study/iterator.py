# -*-coding:utf-8 -*-
# File : iterator.py
# @Time : 2021/5/26 18:10
# @Author : Sf
# version : python 3.7.8

"""
一、迭代器
1、迭代器协议
对象必须提供一个__next__()方法，执行该方法要么返回下一项值，要么返回一个StopIteration异常错误。

2、可迭代对象
实现了迭代器协议的对象，即可以执行__next__()方法的对象。

字符串、列表、元组、字典、集合、文件对象都不是可迭代对象，因为它们都没有next()方法。使用__itre__()方法可以将这些数据类型变为可迭代对象。

list01 = [1, 2, 3]
iter_list = list01.__iter__()
print(iter_list.__next__())
print(iter_list.__next__())
print(iter_list.__next__())
print(iter_list.__next__())
运行结果：

Traceback (most recent call last):
1
2
  File "E:/Python学习/8、迭代器和生成器/迭代器.py", line 11, in <module>
3
    print(iter_list.__next__())
StopIteration
通过上面的运行结果可知在执行到第四个print的时候Python给出了一个StopIteration错误，因为可迭代对象iter_list一共就三个参数

既然字符串、列表、元组、字典、集合、文件对象都不是可迭代对象，那为什么这些数据类型都可以在for循环中被遍历呢？接下去讨论一下for循环的机制后即可知晓。

3、for循环的机制
在使用for循环对数据类型进行遍历的时候实际上是调用了__iter__()方法将数据类型变为了可迭代对象
在for循环将可迭代对象中的元素全部遍历完后也会给出一个StopIteration错误，但for循环遇到StopIteration错误后就结束了对可迭代对象的遍历
for循环机制使用while循环体现：

list01 = [1, 2, 3]
init_num = 0
iter_list = list01.__iter__()
while init_num < len(list01):
    init_num += 1
    print(iter_list.__next__())
运行结果：

1

2

3

4、迭代器的特性
可迭代对象只能被迭代一次
二、生成器
1、生成器的定义
生成器就是一个数据类型，但是这个数据类型可以自动实现迭代器协议

2、生成器的表达形式
生成器的表达形式有两种：一种是生成器函数，另一种是生成器表达式

2.1、生成器函数
在函数中使用yield语句替换return函数，当函数碰到了yield时会返回一个相应的值，并记录当前函数运行的状态，在下次调用函数的时候会从当前状态运行函数；如：

def test():
    print("这是1")
    yield 1
    print("这是2")
    yield 2
    print("这是3")
    yield 3

l = test()
print(l.__next__())
print(l.__next__())
print(l.__next__())
运行结果：

这是1

1

这是2

2

这是3

3

send()方法：

send()方法和__next__方法实现的功能类似，都是取出生成器中的值，但send()方法需要传递一个参数，可以将该参数传递给yield并赋值给一个变量，如：

def test():
    f = yield 1
    print(f)
    yield 2

t = test()
print(t.__next__())
t.send("yield一个1")
运行结果：

1

yield一个1

2.1.2、生成器函数和普通函数比较的好处
生成器函数无需完整生成一个列表，yield一个至即可处理一个值，简约了内存空间。

2.2、生成器表达式
2.2.1、三元表达式
num = 5
res = "这是为True时返回的值" if num == 5 else "这是为False时返回的值"
print(res)
运行结果：

这是为True时返回的值

在上面的三元表达式中的三元指的是：

"这是为True时返回的值"
if num == 5
else "这是为False时返回的值"
2.2.2、列表解析式
l = ["列表元素%s" %i for i in range(5)]
print(l)
运行结果：

['列表元素0', '列表元素1', '列表元素2', '列表元素3', '列表元素4']

上面的解析式就相当于下面的代码：

l = []
for i in range(5):
    l.append("列表元素%s" %i)
print(l)
列表解析式还可以和三元表达式结合在一起使用

l = ["列表元素%s" %i for i in range(10) if i > 5]
print(l)
运行结果：

['列表元素6', '列表元素7', '列表元素8', '列表元素9']

列表解析式的缺点：
当在数据较大的情况下会占用大量的内存空间，因为列表解析式最后输出的结果直接存放在内存中

2.2.3、生成器表达式：
使用方法：
将列表解析式中的方括号改为小括号即可，如

l = ("列表元素%s" %i for i in range(10) if i > 5)
print(l)
运行结果：

<generator object <genexpr> at 0x00A0D770>

生成器表达式相比较于列表解析式的优点在于占用的内存空间小，因为生成器表达式是直接生成一个迭代器而不是一个存放在内存中的列表

3、生成器的特性
延迟计算，一次只返回一个结果
提高代码的可读性

Python3
迭代器与生成器
迭代器
迭代是Python最强大的功能之一，是访问集合元素的一种方式。

迭代器是一个可以记住遍历的位置的对象。

迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。

迭代器有两个基本的方法：iter()
和
next()。

字符串，列表或元组对象都可用于创建迭代器：
>> > list = [1, 2, 3, 4]
>> > it = iter(list)  # 创建迭代器对象
>> > print(next(it))  # 输出迭代器的下一个元素
1
>> > print(next(it))
2
迭代器对象可以使用常规for语句进行遍历：
list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象 
for x in it:
    print(x, end=" ")
执行以上程序，输出结果如下：

1
2
3
4
也可以使用
next()
函数：


import sys  # 引入 sys 模块   

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象   
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()

执行以上程序，输出结果如下：

1
2
3
4
创建一个迭代器
把一个类作为一个迭代器使用需要在类中实现两个方法
iter()
与
next() 。

如果你已经了解的面向对象编程，就知道类都有一个构造函数，Python
的构造函数为
init(), 它会在对象初始化的时候执行。

iter()
方法返回一个特殊的迭代器对象， 这个迭代器对象实现了
next()
方法并通过
StopIteration
异常标识迭代的完成。

next()
方法（Python
2
里是
next()）会返回下一个迭代器对象。

创建一个返回数字的迭代器，初始值为
1，逐步递增
1：

class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
执行输出结果为：

1
2
3
4
5
StopIteration
StopIteration
异常用于标识迭代的完成，防止出现无限循环的情况，在
next()
方法中我们可以设置在完成指定循环次数后触发
StopIteration
异常来结束迭代。

在
20
次迭代后停止执行：

class MyNumbers:

    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration


myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
执行输出结果为：

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
生成器
在
Python
中，使用了
yield 的函数被称为生成器（generator）。

跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。

在调用生成器运行的过程中，每次遇到
yield 时函数会暂停并保存当前所有的运行信息，返回
yield 的值, 并在下一次执行
next()
方法时从当前位置继续运行。

调用一个生成器函数，返回的是一个迭代器对象。

以下实例使用
yield 实现斐波那契数列：
import sys


def fibonacci(n):  # 生成器函数 - 斐波那契     
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成 

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
执行以上程序，输出结果如下：


0
1
1
2
3
5
8
13
21
34
55

"""""