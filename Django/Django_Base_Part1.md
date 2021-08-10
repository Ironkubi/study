[TOC]

# Django Base Part1

项目代码基于Django1.11

## 安装virtualenv

通过pip来安装virtualenv模块

```bash
[root@localhost ~]# pip3 install virtualenv
Collecting virtualenv
  Downloading https://files.pythonhosted.org/packages/ed/ea/e20b5cbebf45d3096e8138ab74eda139595d827677f38e9dd543e6015bdf/virtualenv-15.2.0-py2.py3-none-any.whl (2.6MB)
    100% |████████████████████████████████| 2.6MB 31kB/s 
Installing collected packages: virtualenv
Successfully installed virtualenv-15.2.0
```

## 配置虚拟环境 

在venv文件夹下创建一个虚拟环境

```bash
[root@localhost ~]# python3 -m virtualenv --no-site-packages /home/tianjun/test/venv
Using base prefix '/usr/local'
New python executable in /home/tianjun/test/venv/bin/python3
Also creating executable in /home/tianjun/test/venv/bin/python
Installing setuptools, pip, wheel...done.
```

## 进入虚拟环境，安装Django模块

通过虚拟环境目录中的bin/activate来进入虚拟环境，然后再通过克隆过来的pip安装Django并指定对应的版本号

```bash
[root@localhost test]# source ./venv/bin/activate
(venv) [root@localhost test]# pip install django==1.11
Collecting django==1.11
  Downloading https://files.pythonhosted.org/packages/47/a6/078ebcbd49b19e22fd560a2348cfc5cec9e5dcfe3c4fad8e64c9865135bb/Django-1.11-py2.py3-none-any.whl (6.9MB)
    100% |████████████████████████████████| 6.9MB 152kB/s 
Collecting pytz (from django==1.11)
  Downloading https://files.pythonhosted.org/packages/dc/83/15f7833b70d3e067ca91467ca245bae0f6fe56ddc7451aa0dc5606b120f2/pytz-2018.4-py2.py3-none-any.whl (510kB)
    100% |████████████████████████████████| 512kB 432kB/s 
Installing collected packages: pytz, django
Successfully installed django-1.11 pytz-2018.4
```

## 新建一个项目

在虚拟环境中使用Django模块来创建一个新的项目

```bash
(venv) [root@localhost test]# python3 -m django startproject myProject  或者django-admin startproject myproject
(venv) [root@localhost test]# ls
myProject  README.md  venv
```

## 目录结构分析

在目录结构中

- 外面的myProject文件夹是你项目的根目录， 它的名字不影响Django项目的运行，可以对它进行重命名成任意名称。

- manage.py 命令行使用工具，允许你以任何方式与这个Django项目进行交互。（更多详细的功能在后面进行详细介绍）

- 里面的myProject文件夹是项目的实际的Python包。它的名字是Python包名，将会需要使用它来导入里面的任何东西。

- myProject/\_\_init\_\_.py 是一个空的文件，它会告诉Python，这个项目应该包含哪些额外Python包。

- myProject/setting.py 设置/配置这个Django项目。

- myProject/urls.py 这是一个Django项目的URL的声明文件。它是一个驱动你Django项目运行的目录。

- myPriject/wsgi.py WSGI兼容的Web服务器为您的项目服务的入口点。（Python Web Server Gateway Interface，缩写为WSGI）简单介绍，以前，如何选择合适的Web应用程序框架成为困扰Python初学者的一个问题，这是因为，一般而言，Web应用框架的选择将限制可用的Web服务器的选择，反之亦然。那时的Python应用程序通常是为CGI，FastCGI，mod_python中的一个而设计，甚至是为特定Web服务器的自定义的API接口而设计的。

  WSGI是作为Web服务器与Web应用程序或应用框架之间的一种低级别的接口，以提升可移植Web应用开发的共同点。WSGI是基于现存的[[CGI]]标准而设计的。

```bash
# 通过tree来查看项目的目录结构
(venv) [root@localhost test]# tree myProject/
myProject/
├── manage.py
└── myProject
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

1 directory, 5 files
```

## manage.py

这里简单介绍对应作用不做详解，具体的介绍参考对应文档 [django-admin and manage.py](https://docs.djangoproject.com/en/1.11/ref/django-admin/#changepassword)

```bash
(venv) [root@localhost test]# python3 ./myProject/manage.py 

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword  # changepassword [<username>] 允许更改用户密码
    createsuperuser  # 创建超级用户账户（拥有所有权限的用户）如果需要创建一个初始超级用户帐户，或者如果你需要以编程方式生成站点的超级用户账户，那么这很有用。

[contenttypes]
    remove_stale_contenttypes  # 删除数据库中过时的内容类型（从已删除的模型）。任何依赖于删除的内容类型的对象也将被删除。删除对象的列表之前将会显示提示让你确认可以继续删除。

[django]
    check  # 用于系统检查整个Django框架项目的常见问题。
    compilemessages  # 将Makememessage创建的.po文件编译为.mo文件，以便与内置的gettex支持一起使用。
    createcachetable  # 使用从设置文件中获得的信息创建与数据库缓存后端一起使用的缓存表。
    dbshell  # 运行引擎设置中指定的数据库引擎的命名行客户端，其中包含用户、密码等连接参数设置。
    diffsettings  # 显示当前设置文件和Django的默认设置之间的差异
    dumpdata  # 将与命名应用程序相关联的数据库中的所有数据，输出到标准输出。
    flush  # 从数据库中删除所有数据并重新执行任何后，同步处理程序，未应用迁移的表未被清除。
    inspectdb  # 内观由名称设置指向的数据库中的数据库表，并将Django模型模块（models.py）输出到标准输出。您可以选择将哪些表作为参数传递来检查哪些表。如果你有一个你想使用Django的遗留数据库，请使用它。脚本将检查数据库并为其内的每个表创建模型。
    loaddata  # 搜索并加载指定的内容到数据库
    makemessages  # 遍历当前目录的整个树，取出标记为翻译的所有字符串。它在conf/locale(Django树)或区域（项目和应用程序）目录中创建（或更新）消息文件。在对消息文件进行更改之后，需要用编译程序编译他们，以便使用内置的gettex支持。
    makemigrations  # （常用）根据检测到的模型创建新的迁移。迁移，他们与应用程序和更多的关系在迁移文档中被深度覆盖。提供一个或多个应用程序名称作为参数将向指定的应用成程序创建的迁移和所需的任何依赖项。
    migrate  # （常用）将数据库状态与当前的模型集进行迁移同步。
    sendtestemail  # 发送测试电子邮件给指定的接收者。
    shell  # 启动Python交互式解释器
    showmigrations  # 显示项目中的所有迁移
    sqlflush  # 打印将用于刷新命令的SQL语句
    sqlmigrate  # 打印命名迁移的SQL.这需要一个主动数据库连接，它将用来杰军约束名称；这意味着你必须更具你希望稍后应用的数据库副本生成SQL。
    sqlsequencereset  # 打印SQL语句，以便为给定的应用程序名称重新设置序列。序列是一些数据库引擎用来跟踪自动递增字段的下一个可用数字的索引。使用此命令生成SQL，它将修复序列与其自动递增的字段数据不同步的情况。
    squashmigrations  # 如果可能的话，将AppHyLabor的迁移压缩到迁移名中，并将其迁移到更少的迁移中。由此参数的拥挤的迁移可以安全的与未受挤压的迁移一起存在。
    startapp  # 为当前目录或给定目录中创建给定的应用名称的Django应用程序目录结构。
    startproject  # 为当前目录或给定的目录中创建给定名称的Django项目。
    test  # 运行所有安装的用于程序的测试
    testserver  # 使用给定的数据运行Django开发服务器

[sessions]
    clearsessions  # 可以作为CRON作业运行，也可以直接清理过期的会话。

[staticfiles]
    collectstatic  # 只有安装了静态文件应用程序（Django.Curib.StActFrasm）时，才能使用此命令
    findstatic  # 只有安装了静态文件应用程序（Django.Curib.StActFrasm）时，才能使用此命令。 
    runserver  # 在本地计算机上启动轻量级开发Web服务器。默认情况下，服务器在IP地址127.0.0.1上的端口8000上运行。可以明确的指定ip地址和端口号。
```

## setting.py

**SECRET_KEY** 一个特定Django安装的秘密密钥。这用于提供密码签名，并且应该设置为唯一的、不可预测的值。

**DEBUG** Default: `False` 一个打开/关闭调试模式的布尔值。 不要在调试打开时将站点部署到生产中

**ALLOWED_HOSTS** 表示这个Django站点可以服务的主机/域名的字符串列表。这是一种防止HTTP主机头攻击的安全措施，即使在许多看似安全的web服务器配置下也有可能发生。

**INSTALLED_APPS** 一个字符串列表，指定在这个Django安装中启用的所有应用程序。每个字符串应该是一条虚线的Python路径:应用程序配置类(首选)，或包含应用程序的包。

**MIDDLEWARE** 使用的中间件列表。

**ROOT_URLCONF** 一个字符串，表示您的根URLconf的完整Python导入路径。例如:“mydjangoapps.urls”。可以通过在传入的HttpRequest对象上设置属性urlconf来在每个请求的基础上重写。

**TEMPLATES** 包含用于Django的所有模板引擎的设置的列表。列表中的每一项都是包含单个引擎选项的字典。

**WSGI_APPLICATION** Django的内置服务器(例如runserver)将使用WSGI应用程序对象的完整Python路径。django-admin startproject管理命令将创建一个简单的wsgi。py文件中的应用程序可调用，并将此设置指向该应用程序。

**DATABASES** 包含用于Django的所有数据库的设置的字典。它是一个嵌套字典，其内容将数据库别名映射到包含单个数据库选项的字典。

**AUTH_PASSWORD_VALIDATORS** 用于检查用户密码强度的验证器列表。

**LANGUAGE_CODE** 表示此安装的语言代码的字符串。这应该是标准的语言ID格式。例如，美国英语是“en-us”，中国汉字是“zh-hans”。

**TIME_ZONE** 表示此安装的时区的字符串。"Asiz/Shanghai"表示东八时区北京时间。

**USE_I18N** 一个布尔值，指定是否启用Django的翻译系统。这提供了一个简单的方法来关闭它，用于性能。如果设置为False, Django将进行一些优化，以便不加载翻译机器。

**USE_L10N** 一个布尔值，它指定默认情况下是否启用本地数据格式化。如果设置为True，例如Django将使用当前语言环境的格式显示数字和日期。

**USE_TZ** 一个布尔值，它指定datetimes是否在默认情况下是timezone-aware。如果这个设置为True, Django将在内部使用timezone-aware datetimes。否则，Django将在本地时间使用自然的datetimes。

**STATIC_URL** 在引用位于STATIC_ROOT中的静态文件时使用的URL。

## 创建一个app

创建一个名字为stu的app

```bash
(venv) [root@localhost test]# python3 ./myProject/manage.py startapp stu
(venv) [root@localhost test]# tree myProject/
myProject/
├── db.sqlite3
├── manage.py
├── myProject
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-36.pyc
│   │   ├── settings.cpython-36.pyc
│   │   ├── urls.cpython-36.pyc
│   │   └── wsgi.cpython-36.pyc
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── stu
    ├── admin.py
    ├── apps.py  #应用程序配置
    ├── __init__.py
    ├── migrations #数据迁移，记录models中数据变更
    │   └── __init__.py
    ├── models.py #模型文件
    ├── tests.py
    └── views.py  #Django的视图文件

4 directories, 17 files
```

在项目目录中打开setting.py文件，在INSTALLED_APPS添加对应的app包名

```bash
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stu.apps.StuConfig',  # 对应app名称下的apps.py内的Config类
]
```

然后在stu中新键一个路由文件urls.py,在项目目录中的urls.py去include app的urls文件

```bash
# stu中新建的urls.py
(venv) [root@localhost stu]# cat urls.py 
from django.conf.urls import url
from stu import views

urlpatterns = [
    url(r'^test/', views.test)  # 添加应用中方法的路由
]


# 项目中的urls.py
(venv) [root@localhost myProject]# cat urls.py 
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^stu/', include('stu.urls')),  # 添加app应用的路由
]
```

这样APP一个应用就创建完成能够进行访问了

## 连接MySQL

通过pip安装pymysql模块

```bash
(venv) [root@localhost myProject]# pip install pymysql
Collecting pymysql
  Downloading https://files.pythonhosted.org/packages/e5/07/c0f249aa0b7b0517b5843eeab689b9ccc6a6bb0536fc9d95e65901e6f2ac/PyMySQL-0.8.0-py2.py3-none-any.whl (83kB)
    100% |████████████████████████████████| 92kB 104kB/s 
Installing collected packages: pymysql
Successfully installed pymysql-0.8.0
```

在项目目录中的\_\_init\_\_.py文件中导入pymysql模块

```bash
(venv) [root@localhost myProject]# cat __init__.py 
import pymysql
pymysql.install_as_MySQLdb()


```

在数据库中创建一个新的空数据库

```bash
MariaDB [(none)]> create database mydb charset utf8;
Query OK, 1 row affected (0.00 sec)
```

在项目目录中设置setting.py文件中的DATABASE的值

```bash
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 使用哪种数据库，这里使用的是mysql
        'NAME': 'mydb',  # 数据库名称
        'HOST': 'localhost',  # 数据库主机地址
        'POST': '3306',  # 端口号
        'USER': 'root',  # 用户
        'PASSWORD': '123456',  # 密码
     }
}
```

配置完成，运行项目查看是否能成功运行

```bash
(venv) [root@localhost myProject]# python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

April 24, 2018 - 21:04:31
Django version 1.11, using settings 'myProject.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

成功连接数据库