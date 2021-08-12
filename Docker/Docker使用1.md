# Docker

## [Docker](https://www.runoob.com/docker/centos-docker-install.html) 基本命令

### Docker 安装   

- 卸载旧版本  

 > sudo yum remove docker \
           docker-client \
           docker-client-latest \
           docker-common \
           docker-latest \
           docker-latest-logrotate \
           docker-logrotate \
           docker-engine
     
- 安装所需的软件包。yum-utils 提供了 yum-config-manager ，并且 device mapper 存储驱动程序需要 device-mapper-persistent-data和lvm2    
  
 > sudo yum install -y yum-utils device-mapper-persistent-data lvm2  

- 设置稳定的仓库(添加软件源信息)   

 > sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo  
  
- 更新 yum 缓存：  

 > sudo yum makecache fast  
  
- 安装 Docker Engine-Community   
 
 > sudo yum install docker-ce docker-ce-cli containerd.io  

- 启动docker  

 > sudo systemctl start docker   

- 通过运行 hello-world 映像来验证是否正确安装了 Docker Engine-Community  
  
 > sudo docker run hello-world  

- 配置镜像加速器  

 > sudo mkdir -p /etc/docker     
 > sudo tee /etc/docker/daemon.json <<-'EOF'   
  {
    "registry-mirrors": ["https://o9nqigxx.mirror.aliyuncs.com"]  
  }  
  EOF  
 > sudo systemctl daemon-reload   
 > sudo systemctl restart docker  
  
- systemctl命令是系统服务管理器指令:
 > 启动docker： systemctl start docker  
 > 停止docker： systemctl stop docker  
 > 重启docker： systemctl restart docker  
 > 查看docker状态： systemctl status docker  
 > 开机启动： systemctl enable docker  
***

### Docker 基本命令
  
 > 查看docker概要信息: docker info  
 > 查看docker帮助文档: docker ‐‐help  
 > 查看镜像：docker images  
 > 查看运行的容器：docker ps  
 > 查看所有的容器：docker ps -a  
 > 停止运行容器：docker stop <容器 ID>  
 > 运行容器：docker run -it <容器 ID> /bin/bash  
 > 进入容器：docker exec -it <容器 ID> /bin/bash  
 > 删除容器：docker rm -f <容器 ID>  
 > 查看容器内的标准输出：docker logs -f <容器 ID>  
***     
     
### Docker 容器卷
  
- 用处 
 > 容器的持久化
 > 容器间继承+数据共享
  
- 基本用法
 > docker run -it -v /mydatavolume:/mydatavolumecontainer centos
 > 设置只读权限：docker run -it -v /mydatavolume:/mydatavolumecontainer:ro centos
 > docker inspect <容器 ID>
 
- 利用 Dockerfile 创建容器卷  
 > 创建Dockerfile文件目录： 
   mkdir /mydocker/  
   vim /mydocker/dockerfile  
   FROM centos  
   VOLUME ["/dataVolumeContainer1","/dataVolumeContainer2"]   
   CMD echo "finished,------success1"   
   CMD /bin/bash  
 
 > 等价于：docker run -it -v /host1:/dataVolumeContainer1 -v /host2:/dataVolumeContainer2 /bin/bash

 > 运行 Dockerfile  
   docker build -f /mydocker/Dockerfile -t sunfei/centos .  
   docker images
    
 > 运行容器卷镜像   
   docker run -it  sunfei/centos  
 
 > 容器数据卷-容器间数据共享  
   docker run -it --name dc01 sunfei/centos  
   docker run -it --name dc02 --volumes-from dc01 sunfei/centos  
   docker run -it --name dc03 --volumes-from dc01 sunfei/centos  
   创建文件：touch dc01_add.txt  
      
       
### Dockerfile   
 > 创建Dockerfile文件目录： 
   mkdir /mydocker/
   vim /mydocker/dockerfile

     # Base images 基础镜像
     FROM centos

     # MAINTAINER 维护者信息  
     MAINTAINER lorenwe   

     # ENV 设置环境变量  
     ENV PATH /usr/local/nginx/sbin:$PATH  

     # ADD  文件放在当前目录下，拷过去会自动解压  
     ADD nginx-1.13.7.tar.gz /tmp/ 

     # RUN 执行以下命令  
     RUN rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 \
     && yum update -y \
     && yum install -y vim less wget curl gcc automake autoconf libtool make gcc-c++ zlib zlib-devel openssl openssl-devel perl perl-devel pcre pcre-devel libxslt libxslt-devel \
     && yum clean all \  
     && rm -rf /usr/local/src/*  
     RUN useradd -s /sbin/nologin -M www  

     # WORKDIR 相当于cd  
     WORKDIR /tmp/nginx-1.13.7    

     RUN ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module --with-pcre && make && make install  

     RUN cd / && rm -rf /tmp/  

     COPY nginx.conf /usr/local/nginx/conf/  

     # EXPOSE 映射端口  
     EXPOSE 80 443  

     # ENTRYPOINT 运行以下命令  
     ENTRYPOINT ["nginx"]  

     # CMD 运行以下命令  
     CMD ["-h"]复制代码  
        
 > 构建镜像
   docker build -t nginx:v3 . 
   docker build -f /mydocker/Dockerfile -t sunfei/centos . 

   
 关于dockerfile

虽然我们可以通过docker commit命令来手动创建镜像，但是通过Dockerfile文件，可以帮助我们自动创建镜像，并且能够自定义创建过程。本质上，Dockerfile就是由一系列命令和参数构成的脚本，这些命令应用于基础镜像并最终创建一个新的镜像。它简化了从头到尾的构建流程并极大的简化了部署工作。使用dockerfile构建镜像有以下好处：

像编程一样构建镜像，支持分层构建以及缓存；

可以快速而精确地重新创建镜像以便于维护和升级；

便于持续集成；

可以在任何地方快速构建镜像

 

Dockerfile指令

我们需要了解一些基本的Dockerfile 指令，Dockerfile 指令为 Docker 引擎提供了创建容器映像所需的步骤。这些指令按顺序逐一执行。以下是有关一些基本 Dockerfile 指令的详细信息。

1.FROM

FROM 指令用于设置在新映像创建过程期间将使用的容器映像。

格式：FROM 

示例：

FROM nginx

FROM microsoft/dotnet:2.1-aspnetcore-runtime

 

 

2.RUN

RUN 指令指定将要运行并捕获到新容器映像中的命令。 这些命令包括安装软件、创建文件和目录，以及创建环境配置等。

格式：

RUN ["", "", ""]

RUN

示例：

RUN apt-get update

RUN mkdir -p /usr/src/redis

RUN apt-get update && apt-get install -y libgdiplus

RUN ["apt-get","install","-y","nginx"]

注意：每一个指令都会创建一层，并构成新的镜像。当运行多个指令时，会产生一些非常臃肿、非常多层的镜像，不仅仅增加了构建部署的时间，也很容易出错。因此，在很多情况下，我们可以合并指令并运行，例如：RUN apt-get update && apt-get install -y libgdiplus。在命令过多时，一定要注意格式，比如换行、缩进、注释等，会让维护、排障更为容易，这是一个比较好的习惯。使用换行符时，可能会遇到一些问题，具体可以参阅下节的转义字符。

 

3.COPY

COPY 指令将文件和目录复制到容器的文件系统。文件和目录需位于相对于 Dockerfile 的路径中。

格式：

COPY

如果源或目标包含空格，请将路径括在方括号和双引号中。

 

COPY ["", ""]

示例：

COPY . .

COPY nginx.conf /etc/nginx/nginx.conf

COPY . /usr/share/nginx/html

COPY hom* /mydir/

 

4.ADD

ADD 指令与 COPY 指令非常类似，但它包含更多功能。除了将文件从主机复制到容器映像，ADD 指令还可以使用 URL 规范从远程位置复制文件。

格式：

ADD<source> <destination>

示例：

ADD https://www.python.org/ftp/python/3.5.1/python-3.5.1.exe /temp/python-3.5.1.exe

此示例会将 Python for Windows下载到容器映像的 c:\temp 目录。

 

5.WORKDIR

WORKDIR 指令用于为其他 Dockerfile 指令（如 RUN、CMD）设置一个工作目录，并且还设置用于运行容器映像实例的工作目录。

格式：

WORKDIR

示例：

WORKDIR /app

 

6.CMD

CMD指令用于设置部署容器映像的实例时要运行的默认命令。例如，如果该容器将承载 NGINX Web 服务器，则 CMD 可能包括用于启动Web服务器的指令，如 nginx.exe。 如果 Dockerfile 中指定了多个CMD 指令，只会计算最后一个指令。

格式：

CMD ["<executable", "

CMD

示例：

CMD ["c:\\Apache24\\bin\\httpd.exe", "-w"]

CMD c:\\Apache24\\bin\\httpd.exe -w

 

7.ENTRYPOINT

配置容器启动后执行的命令，并且不可被 docker run 提供的参数覆盖。每个 Dockerfile 中只能有一个ENTRYPOINT，当指定多个时，只有最后一个起效。

格式：

ENTRYPOINT ["", ""]

示例：

ENTRYPOINT ["dotnet", "Magicodes.Admin.Web.Host.dll"]

 

8.ENV

ENV命令用于设置环境变量。这些变量以”key=value”的形式存在，并可以在容器内被脚本或者程序调用。这个机制给在容器中运行应用带来了极大的便利。

格式：

ENV==...

示例：

ENV VERSION=1.0 DEBUG=on \

NAME="Magicodes"

 

9.EXPOSE

EXPOSE用来指定端口，使容器内的应用可以通过端口和外界交互。

格式：

EXPOSE

示例：

EXPOSE 80  

下图来一言以蔽之：
![images](./img/Dockerfile.png)
   
   
   
   
## [Docker-Selenium](https://www.lfhacks.com/tech/selenium-docker)

  > Docker-Selenium项目将传统的selenium集成在docker容器中，方便使用和携带。另外还包括了用于调试的 headless 浏览器、VNC server等工具，用于调试和开发。    
   
  > Docker-Selenium项目（镜像仓库,代码仓库 ）是将 selenium、webdriver、VNC server、chrome（或者firefox）集成在一个docker镜像里的项目。提供如下的功能：  
    代替原有的 remote webdriver
    单个容器就能提供全套 selenium+webdriver+headless 浏览器的功能
    几个容器配合就能完全代替 selenium grid（目前仅限chrome和firefox）
    包含 VNC server（远程桌面），方便远程调试 headless 浏览器
    全部在 linux 环境下执行，无需设置 windows 节点机，方便自动化
    方便自定义 Dockerfile ，用户可以自己制作镜像
     
     
### 背景
               
  > Selenium（官网链接）是我们开展web ui自动化测试的利器，可以很方便的用代码模拟人工在浏览器上的操作，实现 BDD（Behavior-driven development），节约大量的人力。  

  - 然而，selenium在实际使用又有些痛处：  
    - 往往需要在windows主机上安装、运行浏览器（比如chrome），甚至同时安装多种浏览器，不利于在Linux命令行下自动化执行  
    - 浏览器版本难以管理，回退到特定的版本比较困难  
    - 持续集成时需要配置 windows 节点机  
    - 需要为每种浏览器配置 webdriver  
  - 所以我们期望有这样的特点：  
    - 在 Linux 命令行下启动 headless 无界面浏览器  
    - 方便启动和销毁特定版本的浏览器  
    - 一体化，减少多个服务的安装配置
    - 自带webdriver，docker-selenium项目实现了上述这些特点。  
        
### 下载对应的容器
  
    在运行docker的时候是看不到任何界面的，但是有的时候为了debug方便，我们需要看容器里到底在干什么。  
    所以，docker-selenium提供了debug模式。 

    输入命令：sudo docker pull selenium/hub
    输入命令：sudo docker pull selenium/node-chrome

    debug模式:
    
    输入命令：docker pull selenium/node-chrome-debug
    输入命令：docker pull selenium/node-firefox-debug

    如要本地调试的镜像:
    输入命令：docker pull selenium/standalone-chrome-debug
    输入命令：docker pull selenium/standalone-firefox-debug

    查看镜像：docker images
 
 
 ### 启动镜像
 
  - 第一步，启动 selenium-hub
    - 输入命令：docker run -d -p 5555:4444 --name selenium_hub selenium/hub

  - 第二步，启动 selenium/node-chrome-debug，注册到hub节点上
    - 输入命令：docker run -d -p 5901:5900 --link selenium_hub:hub --shm-size=512m selenium/node-chrome-debug

  - 第三步，启动 selenium/node-firefox-debug，注册到hub节点上
    - 输入命令：docker run -d -p 5902:5900 --link selenium_hub:hub --shm-size=512m selenium/node-firefox-debug

  - 说明
    - -p 5555:4444 将容器的5900端口映射到docker的5901端口，访问Docker的5901端口即可访问到node容器；
    - -d 在后台运行
    - --name 给这个容器起一个容易明白的名字，这里我就直接把这个容器成为hub。
    - -shm-size参数：docker默认的共享内存/dev/shm只有64m，有时导致chrome崩溃，该参数增加共享内存大小到512m.*

  - 查看当前运行容器
     - 命令行输入：docker ps 
     - 命令行输入：docker rm -f containe id
  - 查看当前存在的所有容器
     - 命令行输入：docker ps -a
   

 ### 查看控制台
 
  - standalone 的容器正常运行后，用浏览器打开 http://容器地址:4444
    - 在浏览器输入http://192.168.188.30:4444/grid/console，查看是否运行起来
  

 ### 远程桌面调试
 
  - Windows 环境下可以使用 VNC viewer 连接 selenium debug 容器
  - VNC 默认密码为：secret
  
 ### 执行脚本 

    from selenium import webdriver

    chrome_capabilities ={
    "browserName": "chrome",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    # "marionette": True,
    }
    browser = webdriver.Remote("http://192.168.188.30:5555/wd/hub", desired_capabilities=chrome_capabilities)
    browser.get("http://www.163.com")
    browser.get_screenshot_as_file(r"D:/sample/chrome.png")
    browser.quit()

 ## docker-appnium
 
   * 搜索镜像： docker search appium
   * 拉取镜像： docker pull appium/appium
   * 启动容器： docker run --privileged -d -p 4723:4723 --name container-appium appium/appium
   --privileged： 使用该参数，容器内的root真正拥有root权限，否则容器内的root只是外部的一个普通用户权限
   -d: 以分离模式启动容器，分离模式指的是后台运行；而前景模式指的是前台运行，默认分离模式设置为False;
   -p: 指定要映射的IP和端口；
   --name: 为容器指定一个名字


