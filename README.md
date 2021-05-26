一、装饰器介绍
装饰器也是一个函数，它是让其他函数在不改变变动的前提下增加额外的功能。
装饰器是一个闭包，把一个函数当作参数返回一个替代版的函数，本质是一个返回函数的函数（即返回值为函数对象）。
python3支持用@符号直接将装饰器应用到函数。
装饰器工作场景：插入日志、性能测试、事务处理等等。
函数被装饰器装饰过后，此函数的属性均已发生变化，如名称变为装饰器的名称。

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
