一、装饰器介绍
装饰器也是一个函数，它是让其他函数在不改变变动的前提下增加额外的功能。
装饰器是一个闭包，把一个函数当作参数返回一个替代版的函数，本质是一个返回函数的函数（即返回值为函数对象）。
python3支持用@符号直接将装饰器应用到函数。
装饰器工作场景：插入日志、性能测试、事务处理等等。
函数被装饰器装饰过后，此函数的属性均已发生变化，如名称变为装饰器的名称。

1. 简单的装饰器
1.1. 被装饰的函数不带参数
"""入门装饰器：函数功能不带参数"""
def my_decorator(func):
    def inner():
        print("**********")
        print("要添加的功能代码")
        func()
    return inner

# script1()函数调用装饰器的第一种方法
def script1():
    print("测试")
runScript1 = my_decorator(script1)    # 运行script()函数的同时添加有my_decorator()函数的功能
runScript1()
# script1()函数调用装饰器的第二种方法：使用@符号，简单明了
@my_decorator
def script1():
    print("测试")
script1()

1.2. 被装饰的函数带参数
可变参数args和关键字参数*kwargs添加函数通用的装饰器

"""入门装饰器：函数带参数"""
def my_decorator(func):
    def inner(*args, **kwargs):     # 可变参数*args和关键字参数**kwargs
        print("**********")
        print("要添加的功能代码")
        func(*args, **kwargs)
    return inner

# script2()函数调用装饰器的第一种方法：了解即可
def script2(arg):
    print("测试：%s" % arg)
runScript2 = my_decorator(script2)
runScript2("aaa")
# script2()函数调用装饰器的第二种方法：使用@符号，目前使用此方法
@my_decorator
def script2(arg):
    print("测试：%s" % arg)
script2("aaa")


"""装饰器：装饰器带参数"""
def my_decorator(name):
    def outer(func):
        def inner(*args, **kwargs):
            print("********")
            print("添加带装饰器参数%s的功能代码" % self.name)
            func(*args, **kwargs)
        return inner
    return outer

@my_decorator(name='settings')
def script3(arg):
    print("测试----%s" % arg)
script3("bbb")
