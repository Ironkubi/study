# -*-coding:utf-8 -*-
# File : debug_oracle.py
# @Time : 2021/8/6 8:41
# @Author : Sf
# version : python 3.7.8

# python3.7.8 链接Oracle数据库

"""
环境：Windows10 python3.7+pycharm2019 oracle11g instantclient_18_5

1、首先要安装python3.7，pycharm，均可在官网下载安装最新版本，pycharm专业版需要破解

2、python有一个cx_Oracle的模块可以用来访问和操作Oracle数据库
    在命令行或者pycharm中的terminal中执行如下语句：
      python -m pip install cx_Oracle

3、Oracle instant client 下载安装（不安装它导入cx_Oracle的时候会报错）
下载地址（下载最新的基础包就可以，需要登录Oracle账户，没有可以注册一个，免费）
https://www.oracle.com/database/technologies/instant-client/winx64-64-downloads.html


安装
首先：
解压下载的安装包，把解压的路径添加到环境变量–path中，（计算机->属性->高级系统设置->环境变量->系统变量->编辑系统变量->将解压后的路径加在后面，比如我的是：D:\Oracle_cllient\basic\instantclient_18_5，其中D:\Oracle_cllient\basic\是自己选择的）
然后：
将Oracle instant client目录下的oraocci18.dll、oraociei18.dll、oci.dll复制到python安装目录下的\Lib\site-packages\下

4、在pycharm中执行导入不报错则安装成功
import cx_Oracle

5、连接规则
import cx_Oracle as cx

# 参数：用户名/密码@监听(server主机：server端口/server名称)
# server名称：SID
connection=cx.connect("user_name/password@192.168.1.195:1521/SID")
# 创建cursor
cursor = connection.cursor()
# 编写SQL语句（增删改查）  示例：从表中条件查询
sql = " select * from CRIMINAL where js = '13101' "
# 执行sql语句
res = cursor.execute(sql)
# 获取所有数据
one = cursor.fetchall()
# 逐条打印
for x in one:
    print(x)

# 关闭cursor
cursor.close()
# 关闭连接
connection.close()

"""