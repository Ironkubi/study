[TOC]

# MongoDB基础（一）

## 一、MongoDB在Linux环境下的安装

​	进入MongoDB数据库的[官网]:https://www.mongodb.com/找到社区版Mongo服务的Linux系统下的安装包，由于我使用的是CentOS 7,所以下载的是RedHat版本的MongoDB 3.6.5（不同版本可能会有些小差异）

> 资源包下载地址：https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-3.6.5.tgz

```bash
wget https://fastdl.mongodb.org/linux/mongodb-linux-x86_64-rhel70-3.6.5.tgz
```

对文件进行解压缩和解归档。

```bash
$ tar -zxvf mongodb-linux-x86_64-rhel70-3.6.5.tgz 
mongodb-linux-x86_64-rhel70-3.6.5/README
mongodb-linux-x86_64-rhel70-3.6.5/THIRD-PARTY-NOTICES
mongodb-linux-x86_64-rhel70-3.6.5/MPL-2
mongodb-linux-x86_64-rhel70-3.6.5/GNU-AGPL-3.0
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongodump
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongorestore
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongoexport
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongoimport
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongostat
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongotop
mongodb-linux-x86_64-rhel70-3.6.5/bin/bsondump
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongofiles
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongoreplay
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongoperf
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongod
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongos
mongodb-linux-x86_64-rhel70-3.6.5/bin/mongo
mongodb-linux-x86_64-rhel70-3.6.5/bin/install_compass
```

接下来将解压出来的放在自己喜欢的目录下

```bash
[root@localhost ~]# mv /home/tianjun/mongodb-linux-x86_64-rhel70-3.6.5 /usr/local/mongodb
```

## 二、MongoDB的简单配置

我们要启动mongo的服务需要启动mongod。先编写配置文件。

```bash
$ mkdir mongoConfig
$ cd mongoConfig
$ mkdir -p data/db
$ touch mongod.conf
$ vim mongod.conf
```

`mongod.conf`

```yaml
systemLog:  # 系统日志
  destination: file  # 以文件形式存储
  path: "./mongod.log"  # 文件路径和名称
  logAppend: true  # 日志添加
storage:  # 存储
  dbPath: "./data/db"  # 数据存储的地方
  journal:
    enabled: true
processManagement:
  fork: true  # 后台运行
net:
  bindIp: 127.0.0.1  # 绑定IP地址，如果需要外部访问，绑定外部地址
  port: 2333  # 端口
setParameter:
  enableLocalhostAuthBypass: false  # 本地登录不需要密码
```

设置环境变量

```bash
$ vim .bash_profile  # 编写当前用户的环境
$ source .bash_profile  # 加载环境变量
```

##三、启动和关闭mongod服务

启动

```bash
$ mongod -f mongod.conf 
about to fork child process, waiting until server is ready for connections.
forked process: 5956
child process started successfully, parent exiting
```

关闭

```bash
[root@VM_186_206_centos mongoConfig]# mongod -f mongod.conf --shutdown
killing process with pid: 5956
```



## 四、数据库安全配置

进入mongo客户端，输入一下类容设置全局用户

```javascript
use admin
db.createUser(
  {
    user: "myUserAdmin",
    pwd: "abc123",
    roles: [ { role: "userAdminAnyDatabase", db: "admin" } ]
  }
)
```

详细的roles规则请查看mongo[官方文档](https://docs.mongodb.com/manual/reference/built-in-roles/index.html)

重新启动服务

```bash
$ mongod -f mongod.conf --auth
about to fork child process, waiting until server is ready for connections.
forked process: 21334
child process started successfully, parent exiting
```




