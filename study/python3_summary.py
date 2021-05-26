# -*-coding:utf-8 -*-
# File : python3_summary.py
# @Time : 2021/5/26 14:05
# @Author : Sf
# version : python 3.7.8

"""
一、了解python
python是一种解释型、面向对象、动态数据类型的高级程序设计语言。python程序以.py结尾。
python是解释型语言：python开发过程中无需编译，发布的是源代码
python是交互式语言：可以在python提示符下直接执行程序
python是面向对象语言：支持封装
python优缺点
（1）python优点：

易学习：python的关键字较少、结构简单
易阅读
易于维护
标准库丰富
互动模式：可在终端输入执行程序
可移植
可扩展：可用C或C++完成部分代码，然后用pyton调用
数据库
GUI编程：
可嵌入：可将python嵌入到C/C++等程序中
（2）python缺点：

运行速度慢：执行时需翻译成CPU可认识的机器码（翻译耗时），然后再执行
代码不能加密
python特点
python是以缩进来表示代码块，缩进的空格数是可变的，但同一个代码块的语句必须包含相同的缩进空格数
二、python基本语法
1. 注释
程序运行时不执行注释，只用来作代码的解释说明。
单行注释：以 # 开头
多行注释：以三个单引号或三个双引号包裹要注释内容
写注释的规则：注释必须准确、简洁、易懂。
一般“类/接口、构造函数、方法、全局变量、字符/属性"等必须加注释；
“代码不明晰处、代码修改处、逻辑处”等特殊地方也须加注释
""""""

2. 编码
# -*- coding: utf-8 -*-
表示文件以utf-8编码
3. 脚本执行
直接在pycharm软件中运行
打开终端进入代码的目录下输入python XX.py（或XX.py）来启动脚本
在linux系统中若在终端输入时若不想输入python，仅输入XX.py，解决方法：
在代码中添加：#! /usr/bin/env python3
然后修改脚本权限：chmod +x XX.py
执行命令：./XX.py
4. 输出函数
print(*args)
将内容输出打印到屏幕上。
*args：可输入数字、字符串、表达式等等。
同时输入多个内容：内容之间用逗号分隔，python执行时若遇到逗号会输出一个空格。
print中自定义分隔符：sep和end
sep：表示print的每个表达式之间添加分隔符，默认为空格符（sep='_'，表示添加分隔符下划线）
end：表示print打印结束后的字符串，默认为换行符（end=''，表示结束字符串指定为空字符串，这种写法后面的打印会紧跟在此次打印后面）

"""
print("hello")    # hello
x = "hello"
y = "学习"
z = "ok"
print(x, y, z)     # hello 学习 ok
# 添加分隔符
print('I', 'want', 'go', 'home')    # 结果：I want go home
print('I', 'want', 'go', 'home', sep='_')   # 结果：I_want_go_home
print('Hello,', end='')
print('world')                  # 结果：Hello,world

"""
5. 输入
input()
从外部获取变量的值，返回值为字符串类型。
"""
num = input("请输入你要传入的数字：")
print(num)                 # 获取的值为字符串类型
num = int(num)        # 将获取的值转化为数字
"""
6. 标识符
标识符作用：
标识符用来给函数或变量命名的。
标识符规则：
标识符由字母、数字和下划线组成；
标识符首字符不能是数字；
标识符区分大小写；
标识符不能是关键字（保留字）（关键字即有特殊含义的字符）；
标识符见名知意：方便其他人一看就知道这个标识符是来干什么的；
标识符遵循驼峰原则：首单词小写，从第二个单词开始首字母大写（如，writeFile）；
标识符注意事项：
标识符一定是字符串，但字符串不一定是标识符。
python3中允许非 ASCII 标识符。
"""
import keyword
print(keyword.kwlist)
"""python自带的关键字：
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 
'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 
'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 
'return', 'try', 'while', 'with', 'yield']
"""

"""
7. 变量
7.1. 变量定义
变量是“程序可操作的存储空间的名称、程序运行期间能改变的数据”
每个变量都有特定的类型
定义变量的目的：将不同类型的数据存储到内存中。
定义变量：python中定义变量不需要声明，直接赋值即可。变量通过所赋的值来确定变量的类型。通过等号（=）来赋值。
查看变量信息
变量类型：type(变量名)
变量地址：id(变量名)
删除变量的方法： del 变量名
变量被删除后不可再引用，否则会报错提示变量已不存在。
7.2. 交换两个变量的值
通过赋值的方式直接交换两个变量的值而不经过中间变量

7.3. 多个变量同时赋值
若变量值相同，则变量之间用等号连接，从后向左前不断赋值；
若变量值不同，则变量之间以逗号分隔，变量值之间也用逗号分隔，变量与变量值之间用等号连接。
一般同时赋值给多个变量时，“等号左边的变量个数”必须与“等号右边的元素个数”相同，否则会报错。
当“等号左边的变量个数”小于“等号右边的元素个数”时，也可通过星号运行符*来收集多余的值（即在变量名前加*），则代表所传入的元素最终会被转化为列表。
7.4. 序列解包
将一个序列（或任何可迭代的对象）解包，并将得到的值存储到一系列变量中的方法为“序列解包（或可迭代对象解包）”。
将元组中的值通过赋值的方式同时传给给多个变量
"""

i = 10              # 定义变量
print(i)
print(type(i))           # 查看变量类型
print(id(i))             # 查看变量地址
del i                    # 删除变量

"""多个变量同时赋值"""
x = y = z = 10            # 给三个变量赋相同的值
x, y, z = 1, "hello", 2      # 给三个变量赋不同的值

"""将元组的值依次传给多个变量"""
tupleValues = 1, 2, 3
print(tupleValues)  # 结果：(1, 2, 3)
x, y, z = tupleValues
print(x, y, z)      # 结果：1 2 3

"""变量名前含有*"""
x, y, *z = 1, 2, 3, 4
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:1, y:2, z:[3, 4]
x, y, *z = [5, 6, 7, 8]
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:5, y:6, z:[7, 8]
s = 'abc'
x, *y, z = s
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:a, y:['b'], z:c
s = "appium is used by python."
x, *y, z = s.split()
print("x:%s, y:%s, z:%s" % (x, y, z))   # 结果：x:appium, y:['is', 'used', 'by'], z:python.

"""
三、python基本数据类型
数字Number：整数、浮点数、复数
字符串String
布尔类型Boolean：True、False
空值类型None
列表List
元组Tuple
字典Dictionary
集合Set
"""