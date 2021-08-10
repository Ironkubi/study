# MySQL知识

## 操作数据库相关SQL

连接数据库：
```
mysql -uroot -p  # u 后面跟用户名 p 后面是密码
```
查看数据库：
```
show databases
```
使用数据库：
```
use databases;
```
查看数据库中的所有表：
```
show tables;
```
创建数据库：
```
create database db_name
```

修改数据库：
```
aler db_name
```
删除数据库：
```
drop database db_name
```

## 用户相关SQL

### 创建用户

```
create user 'monkey’@'192.168.2.2’ identified by 'passwod’;
# 创建名为 ‘monkey’ 密码为’password’ 登陆IP只能为：192.168.2.2 的用户
 
create user 'monkey’@'192.168.2.%' identified by 'password’;
# 创建名为 ‘monkey’ 密码为’password’ 登陆IP为：192.168.2 网段的用户
 
create user 'monkey’@'%' identified by 'password’;
# 创建名为 ‘monkey’ 密码为’password’ 登陆IP不限的用户
```

### 创建表

```
create table tablename(
                id int auto_increment primary key,
                name varchar(32),
                age int
            )engine=innodb default charset=utf8;

其中 语法：create table +tablename(
                     列名1 类型 其他,
                     列名2 类型 其他) engine = innodb default=charset=utf-8;

engine:指明数据库建表引擎为 innodb （支持事务操作）。
myisam:不支持事务。
default:charset=utf-8 指明数据表的编码字符集 为 utf-8。
```
### 取别名 as
select age as "年龄"，sex "性别"，username "姓名" from yytest as a;

### 查看表的创建语句

show create table table_name

### 在表中添加数据（三种）

```

insert into tablename(name,age) values('monkey’,18);
             
insert into tablename(name,age) values('JIAJIA’,18),('xiaoliu’,18);
# 可以跟多条记录，一元组的形式添加
             
insert into tablename(name,age) select name,age from tablename2;
# 从别的表查找数据 写入

```

### 复制表

```.bash
# 仅复制表结构
create table yytest2 like yytest;

# 复制表结构和数据
create table yytest3 as select  * from yytest;

# 仅复制表的指定字段结构
create table yytest4 as select id,uname,sex from yytest where 1<>1;

# 复制表的指定字段结构和数据
create table yytest5 as select id,uname,sex from yytest;

# 查看表创建语句：没有包含主键和自增
show create table yytest5;

```

### 修改表

修改表名：alter table 旧表名 rename 新表名

修改字段排列顺序： alert table 表名 modify 字段名 数据类型  [first/after,已存在的字段名]
```.bash
# 放在首位
alter table yytest22 modify sex int(2) first;

# 放在birth字段后面
alter table yytest22 modify sex int(2) after birth;

```

修改字段数据类型：alter table 表名 modify 字段名 数据类型
```.bash
# 修改字段数据类型
alter table yytest22 modify sex int(2);
```

修改字段名字： alter table 表名 change 旧字段 新字段 数据类型
```.bash
# 修改字段数据类型和字段名
alter table yytest22 change sexs sex varchar(4);
```

添加字段 ：ALTER TABLE <表名> ADD <字段名> <数据类型>  [约束条件] [FIRST|AFTER 已存在的字段名];

```.bash
# 添加字段
alter table yytest22 add  phone varchar(11);

# 添加字段到首位
alter table yytest22 add  phone varchar(11) not null default 2 first;

# 添加字段到某个字段后面
alter table yytest22 add  phone varchar(11) after sex;
```
删除字段：ALTER TABLE <表名> DROP <字段名>；
```
# 删除字段
alter table yytest22 drop  phone;
```

### 删除表中数据不删除表（三种）
```
delete from tablename;    # 删除数据，但是自增计数不会被删除 单纯的清掉数据
truncate table tablename;    # 清空表，相当于新的表 自增计数 0
delete from tb1 where id > 10    # 跟条件
```

### 删除表
```
drop table tablename;    # 删除表
```

### 修改数据
```
update tablename set age=1024;
update tablename set age=2048,name=lisa where age=18;
```

### 查看数据
```
desc tablename;查看表结构
select * from tablename; # 查看表的所有行列
select  name,age from tablename;    # 查看name和age 列
```
### 条件查询

distinct 去重数据
```
distinct只能在select语句中使用且必须在所有字段前面

如果有多个字段需要去重，则会对多个字段进行组合去重，即所有字段的数据重复才会被去重

查看去重字段有多少种值  ：select count(distinct age) from yyTest; 
```

排序 order by
```
select * form table_name order by id desc    # 从大到小
select * form table_name order by id asc    # 从小到大
```
限制 limit
```
select * form table_name order by id asc limit 10    # 取查询结果的前10条
 
select * form table_name order by id asc limit 20,10    # 取查询结果从第20条开始 往后查10条
 
select * form table_name order by id asc limit 10 offset 20   # 取查询结果从第20条开始 往后查10条
```
模糊查寻 like
```
%表示任意长度的字符  _表示单字符

select * from table_name where name like "张%"    # 以张开头的
 
select * from table_name where name like "%张%"    # 包含张的
 
select * from table_name where name like "%张"    # 以张结尾的
 
select * from table_name where name like "张_"    # 以张开头的 两个字的 
 
select * from table_name where name like "_浩_%"    # 三个字的 并且中间是 浩 的
```
日期查询
```
select * form table_name where date_key between '2019-10-10' and '2019-10-10';
```
判断为空值NULL
is null是一个关键字来的，用于判断字段的值是否为空值（NULL）
```
select * from yyTest where sex is null;
select * from yyTest where sex is not null;
```
between and 范围查询
```
BETWEEN 取值1 AND 取值2
NOT BETWEEN 取值1 AND 取值2
select * from yyTest where age between 19 and 21;
select * from yyTest where age not between 19 and 21;
```

group by 分组查询
```
group by 关键字可以根据一个或多个字段对查询结果进行分组
group by 一般都会结合Mysql聚合函数来使用
如果需要指定条件来过滤分组后的结果集，需要结合 having 关键字；

group by +聚合函数的栗子 （count(),sum(),max(),min(),avg()）
# count统计条数
select count(*) from yyTest group by department;

group by+group_concat()栗子
group_concat()可以将分组后每个组内的值都显示出来
select department,group_concat(username) as "部门员工名字" from yyTest group by department;

group by +having栗子
select *,GROUP_CONCAT(username) from yyTest group by age having department = "seewo";
```

### 外键
```
create table tablename1(id int auto_increment primary key ,
name char(32));
 
create table tablename2(id int auto_increment primary key ,
name char(32),
friend_id int,
constraint fk_t1_t2 foreign key (friend_id) references tablename1(id));

　　外键的创建：定义表的列时预料外键字段，之后 constraint fk_t1_t2 foreign key (friend_id) references tablename1(id));   constaint ... foreign key 预留字段名 references 被关联表名（字段名）
```

### 表的补充
```
desc t;    # 查看t 的表结构
         
show create table t;    # 查看创建t的创建语句
         
show create table t \G;    # 横向查看
         
alter table t10 AUTO_INCREMENT=10000;    # 设置自增的起始值
```

## MySQL的自增问题

### 自增的起始值
```
alter table t10 AUTO_INCREMENT=10000;    # 设置自增的起始值
```
### MySQL: 自增步长

#### 基于会话级别：
```
show session variables like 'auto_inc%';    查看全局变量
set session auto_increment_increment=2; 设置会话步长
# set session auto_increment_offset=10;
```
#### 基于全局级别：

```
show global variables like 'auto_inc%'; 查看全局变量
set global auto_increment_increment=2; 设置会话步长
# set global auto_increment_offset=10;
```

### SqlServer：自增步长

#### 基于表级别

```

CREATE TABLE `table1` (
`id` int(11) NOT NULL AUTO_INCREMENT,
) ENGINE=InnoDB AUTO_INCREMENT=3, 步长=2 DEFAULT CHARSET=utf8
# 自增起始值为 3 步长为 2
 
CREATE TABLE `table2` (
`id` int(11) NOT NULL AUTO_INCREMENT,
) ENGINE=InnoDB AUTO_INCREMENT=9, 步长=3 DEFAULT CHARSET=utf8
# 自增起始值为 9 步长为 3
```


```
E_R模型：实体-关系模型

描述两个实体之间的对应规则：
一对一；一对多；多对多；
三范式：
第一范式：1NF 列不可拆分
第二范式：2NF 唯一标识
第三范式:   3NF  引用主键

数据完整性：字段类型，约束

字段类型：
数字 int  decimal(5,2) 一共5位 小数2位
字符串：char ，varchar（可变） text
日期：datetime
布尔：bit

约束
主键：primary key
非空 not null
唯一：unique
默认：default
外键：foreign key

```


## 常用SQL语句

t - table, c - column, v - value, o - operation( = , < , > , <=, >=)

### where中的运算符

| 运算符  | 描述                                         |
| ------- | -------------------------------------------- |
| =       | 等于                                         |
| <>  !=  | 不等于                                         |
| >       | 大于                                         |
| <       | 小于                                         |
| >=的   | 大于等于                                     |
| <=     | 小于等于                                     |
| and  && | 所有查询条件均满足才会被查询出来                 |
| or  ||  | 满足任意一个查询条件就会被查询出来               |
| xor      | 满足任意一个查询条件就会被查询出来               |
| between | 在某个范围内                                 |
| like    | 模糊查询,通配符 （%like, %like%, like%,...） |
| in      | 指定针对某个列的多个可能值                   |

### like 通配符

| 通配符                   | 描述                       |
| ------------------------ | -------------------------- |
| %                        | 替代0个或多个字符（任意长度的字符串）          |
| _                        | 替代一个字符               |
| [charlist]               | 字符列中的任何单一字符     |
| [^charlist]或[!charlist] | 不在字符列中的任何单一字符 |

```
like 'Tc%' -- 将搜索以字母Tc开头的所有字符串（如 Tccisa）
like '%er' -- 将搜索以字符er结尾的所有字符串（如 teacher）
like '%know%' -- 将搜索在任何位置包含know的所有字符串（如 unknowledgeable）
like '_ove' -- 将搜索以字母ove结尾的所有四个字母的名称（如 love）
like '[CK]ars[eo]n' -- 将搜索下列字符串： Carsen、Karson、Carson和Karson
like '[A-Z]user' -- 将搜索以字符串user结尾、以从A-Z的任何单个字母开头的所有名称
like 'M[^c]%' -- 将搜索以字母M开头，并且第二个字母不是c的所有名称（如MiPro）
匹配的字符串必须加单引号或双引号 like "%test%" 
默认情况下，like匹配的字符串是不区分大小写的； like "test1" 和 like "TEST1" 匹配的结果是一样的
如果需要区分大小写，需要加入 binary 关键字
select * from yyTest where username like binary "TEST_";
```
 


> 关于删除的三个语句： `DROP`, `TRUNCATE`, `DELETE`的区别
>
> **DROP**
>
> ```sql
> drop t;
> ```
>
> 删除表，并释放空间，将test删除的一干二净。
>
> **TRUNCATE**
>
> ```mysql
> truncate t;
> ```
>
> 删除表中的内容，并释放空间，但不删除表的定义，表的结构还在。
>
> **DELETE**
>
> ```mysql
> delete from t;
> ```
>
> 仅删除表test内的所有内容，保留表的定义，不释放空间。

