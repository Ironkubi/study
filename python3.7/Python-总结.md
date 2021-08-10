# 九、python

   > 1、装饰器介绍  
    装饰器也是一个函数，它是让其他函数在不改变变动的前提下增加额外的功能。  
    装饰器是一个闭包，把一个函数当作参数返回一个替代版的函数，本质是一个返回函数的函数（即返回值为函数对象）。  
    python3支持用@符号直接将装饰器应用到函数。  
    装饰器工作场景：插入日志、性能测试、事务处理等等。  
    函数被装饰器装饰过后，此函数的属性均已发生变化，如名称变为装饰器的名称。  

  ## 2、什么是python生成器
  
    返回可迭代项集的函数称为生成器。
  
  ## 什么是python迭代器？

    迭代器是可以遍历或迭代的对象。
    
  ## 描述yeild作用
  
    保存当前运行状态（断点），然后暂停执行，即将函数挂起
    将yeild关键字后面表达式的值作为返回值返回，此时可以理解为起到了return的作用，当使用next()、send()函数让函数从断点处继续执行，即唤醒函数
    有yeild关键字的函数是生成器函数

    
  ## python中is 和== 比较的区别？
  
    is 比较两个对象的内存地址是否相同，

     == 比较连个对象的数据是否相等
     
  Python中文件读写read,readline,readlines函数的区别？
     
    read 每次会读取整个文件
    readline 每次读取一行信息
    readlines 读取整个文件返回一个列表，列表每个元素代表一行
    

  
  python中re模块的match,search方法的比较
     
     match 匹配字符串的开头，
     search匹配整个字符串
  
  写一个函数获取文件夹下所有文件的绝对路径
     
     import os
      def s(path):
        file_list=os.listdir(path)
          for file in file_list:
        print(os.path.realpath(file))

    s("/Users/xiangyong/PycharmProjects/11-13")
   
  python中的zip函数的使用
  
    zip函数接受任意多个（包括0个和1个）序列作为参数，返回一个tuple列表(2.x)在（3.x)返回一个zip对象

    x = [1, 2, 3]

    y = [4, 5, 6]

    z = [7, 8, 9]

    xyz = list(zip(x, y, z))  #压缩象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    unxyz=zip(*xyz)   #  拆包
    print(xyz)
    print(list(unxyz))
   
  python 中list去重复
    方法1  list=[1,1,2,3] 

    set=set(list)

    list2=list(set)

    方法2

    list2=[]

    for i in list:

    if i not in list2:

        list2.append(i)
  


  多进程和多线程的理解
  
    进程是操作系统分配资源的基本单位，线程是cpu调度的基本单位
    进程是程序运行的实例，可以有多个线程，单独占有内存空间，多个线程贡献进程资源
    一个程序至少有一个进程,一个进程至少有一个线程，
    进程在执行过程中拥有独立的内存单元，而多个线程共享内存，从而极大地提高了程序的运行效率
    线线程不能够独立执行，必须依存在进程中
    优缺点：线程和进程在使用上各有优缺点：线程执行开销小，但不利于资源的管理和保护；而进程正相反。

  [:: - 1}表示什么？

     [:: - 1]用于反转数组或序列的顺序。
  
  
  你如何把字符串的第一个字母大写？

    在Python中，capitalize()函数可以将字符串的第一个字母大写。如果字符串在开头已经包含大写字母，那么它将返回原始字符串。
    
  1、闭包

    定义：闭包是由函数及其相关的引用环境组合而成的实体(即：闭包=函数+引用环境)(想想Erlang的外层函数传入一个参数a, 内层函数依旧传入一个参数b, 内层函数使用a和b, 最后返回内层函数)
     代码：def ExFunc(n):

        sum=n

        def InsFunc():

             return sum+1

          return InsFunc
          
  3、迭代器

    1、可以直接作用于for循环的数据类型

    第一类：集合数据类型，如list、tuple、dict、set、str等；
    第二类：generator，包括集合定义generator和带yield的generator(也就是generator function)。
    
    以上这些可以直接作用于for循环的对象统称为可迭代对象：Iterable。

    可以使用isinstance()判断一个对象是否是Iterable对象：

    generator不但可以作用于for循环，还可以被next()函数不断调用并返回下一个值，直到最后抛出StopIteration错误表示无法继续返回下一个值了。那么定义来了，可以被next（）调用并不断返回下一个值得对象称为迭代器（Iterator）

    把list、dict、str等Iterable变成Iterator可以使用iter()函数

 

  4、     生成器

    为什么使用生成式：

    更容易使用，代码量较小内存使用更加高效
   
 

8、     字符串用法

内建函数：

         Capitalize() 字符串第一个大写

Center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串

Count(str,beg=0,end=len(string)) 返回 str 在 string 里面出现的次数，如果 beg 或者 end 指定则返回指定范围内 str 出现的次数

decode(encoding=’utf-8’) 以 encoding 指定的编码格式解码 string，如果出错默认报一个 ValueError 的 异 常 ， 除非 errors 指 定 的 是 'ignore' 或 者'replace'

encode(encoding=’utf-8’) 以 encoding 指定的编码格式编码 string，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace'

endswith(obj,beg=0,end=len(string)) 检查字符串是否以 obj 结束，如果beg 或者 end 指定则检查指定的范围内是否以 obj 结束，如果是，返回 True,否则返回 False.

expandtabs(tabsize=8) 把字符串 string 中的 tab 符号转为空格，tab 符号默认的空格数是 8。

Format() 格式化字符串

Index() 跟find()方法一样，只不过如果str不在 string中会报一个异常

Isalnum() 如果 string 至少有一个字符并且所有字符都是字母或数字则返回 True,否则返回 False

Isalpha() 如果 string 至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

Isdigit() 如果 string 只包含数字则返回 True 否则返回 False.

Lstrip() 截掉 string 左边的空格

Replace(str1,str2,num=string.count(str1) 把 string 中的 str1 替换成 str2,如果 num 指定，则替换不超过 num 次

Rstrip() 删除 string 字符串末尾的空格.

Split(str=’’,num=string.count(str)) 以 str 为分隔符切片 string，如果 num 有指定值，则仅分隔 num+ 个子字符串

Strip() 在 string 上执行 lstrip()和 rstrip()

6、     内置模块

re（正则）、math（数学）、os（系统）、datetime、sys、json

sys：

     sys.argv

功能：在外部向程序内部传递参数

sys.exit(n)

功能：执行到主程序末尾，解释器自动退出，但是如果需要中途退出程序，可以调用sys.exit函数，带有一个可选的整数参数返回给调用它的程序，表示你可以在主程序中捕获对sys.exit的调用。（0是正常退出，其他为异常）

sys.path

功能：获取指定模块搜索路径的字符串集合，可以将写好的模块放在得到的某个路径下，就可以在程序中import时正确找到。

sys.modules

功能：sys.modules是一个全局字典，该字典是python启动后就加载在内存中。每当程序员导入新的模块，sys.modules将自动记录该模块。当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。它拥有字典所拥有的一切方法。

17、    正则

功能函数：

     compile() 编译正则表达式模式，返回一个对象的模式

     match() 只匹配字符串的开始，如果开始不匹配，函数返回None

     search() 在整个字符串中寻找，找到返回，匹配不成功返回None

     findall() 遍历匹配，可以获取字符串中所有匹配的字符串，返回一个列表

finditer() 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。找到 RE 匹配的所有子串，并把它们作为一个迭代器返回

       贪婪匹配和费贪婪匹配

前面的*,+,?等都是贪婪匹配，也就是尽可能匹配，后面加?号使其变成惰性匹配

      \d   数字:[0-9]

      \D   非数字:[^\d]

      \s   匹配任何空白字符:[<空格>\t\r\n\f\v]

\S   非空白字符:[^\s]

\w   匹配包括下划线在内的任何字字符:[A-Za-z0-9_]

\W   匹配非字母字符，即匹配特殊字符

\A   仅匹配字符串开头,同^

\Z   仅匹配字符串结尾，同$

\b   匹配\w和\W之间，即匹配单词边界匹配一个单词边界，也就是指单词和空格间的位置。例如， 'er\b' 可以匹配"never" 中的 'er'，但不能匹配 "verb" 中的'er'。

\B   [^\b]

.    匹配任意除换行符"\n"外的字符(在DOTALL模式中也能匹配换行符

\    转义字符，使后一个字符改变原来的意思

l   匹配前一个字符0或多次

+   匹配前一个字符1次或无限次

?   匹配一个字符0次或1次

 

19、    线程、进程和协程

线程：轻量级进程，线程是进程中的一个实体，是被系统独立调度和分派的基本单位，线程自己不拥有系统资源，只拥有一点儿在运行中必不可少的资源，但它可与同属一个 进程的其它线程共享进程所拥有的全部资源

使用threading这个高级模块

多个线程访问同一资源时需要加线程锁lock

获取锁：lock.acquire()

释放锁：lock.release()

进程：进程是一个实体。每一个进程都有它自己的地址空间

创建进程的类：process

协程：一个程序可以包含多个协程，可以对比与一个进程包含多个线程，因而下面我们来比较协程和线程。我们知道多个线程相对独立，有自己的上下文，切换受系统控制；而协程也相对独立，有自己的上下文，但是其切换由自己控制，由当前协程切换到其他协程由当前协程来控制。

优点：IO资源、减少callback的使用

用第三方库 gevent 来支持协程。gevent用到的主要模式是greenlet


  ## 列出5个python标准库

    os：提供了不少与操作系统相关联的函数
    sys:   通常用于命令行参数
    re:   正则匹配
    math: 数学运算
    datetime:处理日期时间


  ## 谈下python的GIL

    GIL 是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。
    多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大
    
  
  ## fun(*args,**kwargs)中的*args,**kwargs什么意思？
  
  ## 一句话解释什么样的语言能够用装饰器?

    函数可以作为参数传递的语言，可以使用装饰器
  
  ## python内建数据类型有哪些?

    整型--int
    布尔型--bool
    字符串--str
    列表--list
    元组--tuple
    字典--dict
    
  ## 避免转义给字符串加哪个字母表示原始字符串？
     
     r , 表示需要原始字符串，不转义特殊字符
     
  ## 列出python中可变数据类型和不可变数据类型，并简述原理

    不可变数据类型：数值型、字符串型string和元组tuple
    不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址），如下图用id()方法可以打印对象的id
    
    可变数据类型：列表list和字典dict；
    允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。      
