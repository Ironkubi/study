# -*-coding:utf-8 -*-
# File : debug_lambda.py
# @Time : 2021/5/26 18:05
# @Author : Sf
# version : python 3.7.8


"""
想写出更Pythonic的代码，必须学会lambda表达式。用lambda表达式创建匿名函数，能治好
起函数名引起的头痛，不过只适合写简单逻辑的函数。

# lambda语法
lambda [arg1[, arg2, .....argn]]: expression

冒号: 左边arg1
~argn是传入参数，可以传入多个值，也可以添加默认值，跟正常函数一样，冒号: 右边是expression，参数的表达式。表达式中出现的参数需要在: 左边中有定义，注意: 表达式只能是单行

lambda实例
计算arg1, arg2的和：

def sum(arg1, arg2):
    total = arg1 + arg2
    return total


sum(10, 20)
30
使用lambda表达式的写法：

lambda arg1, arg2: arg1 + arg2  # arg1, arg2可以传入默认值
可以看出使用lambda更加简美。

lambda用法
独孤球是

1.
将lambda函数赋值给一个变量，通过这个变量间接调用该lambda函数。
例如，执行语句add = lambda x, y: x + y，定义了加法函数lambda
x, y: x + y，并将其赋值给变量add，这样变量add便成为具有加法功能的函数。例如，执行add(1, 2)，输出为3。

2.
将lambda函数赋值给其他函数，从而将其他函数用该lambda函数替换。
例如，为了把标准库time中的函数sleep的功能屏蔽，我们可以在程序初始化时调用：time.sleep = lambda
    x: None。这样，在后续代码中调用time库的sleep函数将不会执行原有的功能。例如，执行time.sleep(3)
时，程序不会休眠3秒钟。

3.
将lambda函数作为其他函数的返回值，返回给调用者。
函数的返回值也可以是函数。例如return
lambda x, y: x + y返回一个加法函数。这时，lambda函数实际上是定义在某个函数内部的函数，称之为嵌套函数，或者内部函数。对应的，将包含嵌套函数的函数称之为外部函数。内部函数能够访问外部函数的局部变量，这个特性是闭包(
    Closure)
编程的基础。

4.
将lambda函数作为参数传递给其他函数。
filter函数。此时lambda函数用于指定过滤列表元素的条件。
例如filter(lambda x: x % 3 == 0, [1, 2, 3])
指定将列表[1, 2, 3]
中能够被3整除的元素过滤出来，其结果是[3]。

sorted函数。此时lambda函数用于指定对列表中所有元素进行排序的准则。
例如sorted([1, 2, 3, 4, 5, 6, 7, 8, 9], key=lambda x: abs(5 - x))
将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]
按照元素与5距离从小到大进行排序，其结果是[5, 4, 6, 3, 7, 2, 8, 1, 9]。

map函数。此时lambda函数用于指定对列表中每一个元素的共同操作。
例如map(lambda x: x + 1, [1, 2, 3])
将列表[1, 2, 3]
中的元素分别加1，其结果[2, 3, 4]。

reduce函数。此时lambda函数用于指定列表中两两相邻元素的结合条件。
例如reduce(lambda a, b: '{}, {}'.format(a, b), [1, 2, 3, 4, 5, 6, 7, 8, 9])
将列表[1, 2, 3, 4, 5, 6, 7, 8, 9]
中的元素从左往右两两以逗号分隔的字符的形式依次结合起来，其结果是
'1, 2, 3, 4, 5, 6, 7, 8, 9'。

"""""
