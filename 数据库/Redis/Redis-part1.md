[TOC]

# Redis 的安装与配置

Redis是一个开源（BSD许可），内存数据结构存储，用作数据库，缓存和消息代理。它支持数据结构，如字符串，散列，列表，集合，具有范围查询的排序集，位图，超级日志和具有半径查询的地理空间索引。 Redis具有内置复制，Lua脚本，LRU驱逐，事务和不同级别的磁盘持久性，并通过Redis  Sentinel提供高可用性，并通过Redis群集实现自动分区。 

## 一、Redis的安装

先将安装需要的环境配置好比如gcc，我们通过YUM包管理工具来进行安装。

```bash
[root@VM_186_206_centos ~]# yum install gcc
```

然后通过wget对redis的源码压缩归档文件进行下载（在这下载的是Redis4.0.9的稳定版， 在Redis3.2中有一个较大的漏洞，核客会通过你启动的redis-server获取电脑控制权，安装挖矿病毒）

[Redis官网](https://redis.io/)

> Redis-4.0.9的下载地址
>
> http://download.redis.io/releases/redis-4.0.9.tar.gz

通过wget下载源码资源

```bash
[root@VM_186_206_centos ~]# wget http://download.redis.io/releases/redis-4.0.9.tar.gz
```

然后对下载的文件进行解压解归档

```bash
[root@VM_186_206_centos ~]# tar -zxvf redis-4.0.9.tar.gz 
```

将解压解归档的文件夹放入你希望的目录

```bash
[root@VM_186_206_centos ~]# rm redis-4.0.9 /usr/local/redis-4.0.9
```

对源码进编译

```bash
[root@VM_186_206_centos ~]# cd /usr/local/redis-4.0.9
[root@VM_186_206_centos redis-4.0.9]# make
```

> 编译的过程中可能会出错，最重要的是你的linux中是否已经安装gcc的编译环境
>
> 在编译的过程中可能会报下面的错误
>
> ```bash
> In file included from adlist.c:34:0:
> zmalloc.h:50:31: fatal error: jemalloc/jemalloc.h: No such file or directory
>  #include <jemalloc/jemalloc.h>
> ```
>
> 错误的解决方法为在make后加上参数MALLOC=libc
>
> ```bash
> [root@VM_186_206_centos redis-4.0.9]# make MALLOC=libc
> ```

编译完成后可以对编译进行检查是否有错误

```bash
[root@VM_186_206_centos redis-4.0.9]# make test
...
\o/ All tests passed without errors!

Cleanup: may take some time... OK
```

源码编译完成后就可以进行使用了，但是在使用之前需要将redis加入环境变量中方便以后使用

先进入用户家目录，然后编写.bash_profile文件，将redis的路径添加到PATH中

```bash
[root@VM_186_206_centos redis-4.0.9]# cd ~
[root@VM_186_206_centos ~]# vim .bash_profile
```

```shell
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
        . ~/.bashrc
fi

# User specific environment and startup programs


REDIS_HOME=/usr/local/redis-4.0.9
PATH=$PATH:$HOME/bin:$REDIS_HOME/src

export PATH
```

这样安装就完成了

## 二、Redis-server的配置

对redis的配置我们需要在Redis的目录中复制一份配置文件，不在原来的配置文件上进行修改，避免修改错误无法找到原文件。

```bash
[root@VM_186_206_centos ~]# cp /usr/local/redis-4.0.9/redis.conf ./redisConfig/redis.conf
[root@VM_186_206_centos ~]# cd redisConfig
[root@VM_186_206_centos redisConfig]# vim redis.conf 
```

Redis的配置文件非常的长，在这就不全部贴出，以行号作为标识，进行讲解如何配置

首先配置redis绑定哪个IP地址

>这里绑定的IP地址一定得是ifconfig中的网卡地址，不然会出错启动失败
>
>```bash
>[root@VM_186_206_centos ~]# ifconfig
>eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
>        inet xxx.xxx.xxx.xxx  netmask 255.255.224.0  broadcast xxx.xxx.xxx.255
>        ether XX:XX:XX:XX:XX:XX  txqueuelen 1000  (Ethernet)
>        RX packets 29994  bytes 4629635 (4.4 MiB)
>        RX errors 0  dropped 0  overruns 0  frame 0
>        TX packets 28531  bytes 4220669 (4.0 MiB)
>        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
>
>lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
>        inet 127.0.0.1  netmask 255.0.0.0
>        loop  txqueuelen 1  (Local Loopback)
>        RX packets 4632659  bytes 1237206796 (1.1 GiB)
>        RX errors 0  dropped 0  overruns 0  frame 0
>        TX packets 4632659  bytes 1237206796 (1.1 GiB)
>        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
>```
>
>如果绑定127.0.0.1网络回环地址着只有本机可以使用，外部无法访问，所以这我们需要绑定外部IP地址（如果使用云服务，这里绑定你的内网地址即可）

69行`  bind xxx.xxx.xxx.xxx`

接着是监听的端口号

92行`port 8464`

最大TCP连接数

101行 `tcp-backlog 128`(这里我改为和linux内核相同的值了，如果大型应用需要将内核的值修改到2048左右以应对更多的连接)

将Redis设置为守护进程（可选）

136行 `daemonize yes`

设置Redis日志路径

171行 `logfile "./redis.log"`

Redis的数据库个数（默认16个数据库）

186行 `databases 16`

在196行介绍的就是关于数据持久化的设置，这里简单解释下

`save 900 1`有一条数据发生了变化在 900秒(15分钟)后进行持久化

`save 300 10` 有十条数据发生了变化在 300秒（5分钟）后进行持久化

`save 60 10000` 有一万条数据发生了变化在60秒（1分钟）后进行持久化

设置RDB持久化保存的文件名,和路径

253行 `dbfilename dump.rdb`

263行 `dir ./`(当前配置文件的路径)

在265行进行设置的是Redis集群的读写分离（奴从模式）主人进行数据的写入， 奴隶进行数据的读取（后面详细介绍）

在487行是关于数据库安全的设置

500行 `requirepass xxxx`设置访问Redis的口令（尽量写复杂的口令）

在521行是关于最大客户端的连接数的设置

532行`maxclients 10000`

534行是关于内存的调度和限制的设置

在603行是关于懒释放的（这是在Redis4.0中新加的配置）

> ​	Redis重度使用患者应该都遇到过使用 DEL 命令删除体积较大的键， 又或者在使用 FLUSHDB 和 FLUSHALL  删除包含大量键的数据库时，造成Redis阻塞的情况；另外Redis在清理过期数据和淘汰内存超限的数据时，如果碰巧撞到了大体积的键也会造成服务器阻塞。
> 	为了解决以上问题， Redis4.0 引入了Redis的机制，它可以将删除键或数据库的操作放在后台线程里执行， 从而尽可能地避免服务器阻塞。

在652行关于Append Only Mode的配置，改模式会记录下所有对数据库的添加操作（删除了某条数据会将添加的数据删除），是防止服务器意外宕机数据丢失是另外一种手段，所有当服务器意外宕机优先使用Append Only Mode进行数据恢复，如果AOM无法恢复再使用RDB进行数据恢复，这样数据丢失的概率较低。

672行 `appedonly yes` 启动Append Only Mode

676行 `appendfilename "appendonly.aof"` 该模式下文件保存的名称（路径默认与redis.conf在同一路径）

差不多就是这些配置了，后面的配置当需要的时候再来进行修改就可以了。

加载我们的配置启动Redis服务

```bash
[root@VM_186_206_centos redisConfig]# redis-server redis.conf 
[root@VM_186_206_centos redisConfig]# cat redis.log 
15119:C 02 Jun 11:29:14.658 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
15119:C 02 Jun 11:29:14.658 # Redis version=4.0.9, bits=64, commit=00000000, modified=0, pid=15119, just started
15119:C 02 Jun 11:29:14.658 # Configuration loaded
                _._                                                  
           _.-``__ ''-._                                             
      _.-``    `.  `_.  ''-._           Redis 4.0.9 (00000000/0) 64 bit
  .-`` .-```.  ```\/    _.,_ ''-._                                   
 (    '      ,       .-`  | `,    )     Running in standalone mode
 |`-._`-...-` __...-.``-._|'` _.-'|     Port: XXXX
 |    `-._   `._    /     _.-'    |     PID: 15120
  `-._    `-._  `-./  _.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |           http://redis.io        
  `-._    `-._`-.__.-'_.-'    _.-'                                   
 |`-._`-._    `-.__.-'    _.-'_.-'|                                  
 |    `-._`-._        _.-'_.-'    |                                  
  `-._    `-._`-.__.-'_.-'    _.-'                                   
      `-._    `-.__.-'    _.-'                                       
          `-._        _.-'                                           
              `-.__.-'                                               

15120:M 02 Jun 11:29:14.660 # Server initialized
15120:M 02 Jun 11:29:14.661 # WARNING you have Transparent Huge Pages (THP) support enabled in your kernel. This will create latency and memory usage issues with Redis. To fix this issue run the command 'echo never > /sys/kernel/mm/transparent_hugepage/enabled' as root, and add it to your /etc/rc.local in order to retain the setting after a reboot. Redis must be restarted after THP is disabled.
15120:M 02 Jun 11:29:14.661 * Ready to accept connections

```

在redis.log中看见上面的内容说明你已经配置成功，并成功运行。

接下来我们通过redis-cli尝试连接下服务器

```bash
[root@VM_186_206_centos ~]# redis-cli -h xxx.xxx.xxx.xxx -p xxxx
xxx.xxx.xxx.xxx:xxxx> AUTH xxxx
OK
xxx.xxx.xxx.xxx:xxxx> PING
PONG
```



