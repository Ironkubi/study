# Docker

## [Docker](https://www.runoob.com/docker/centos-docker-install.html) 基本命令
***
* **Docker 安装**   

  * 卸载旧版本  
  
   > sudo yum remove docker \
             docker-client \
             docker-client-latest \
             docker-common \
             docker-latest \
             docker-latest-logrotate \
             docker-logrotate \
             docker-engine
       
  * 安装所需的软件包。yum-utils 提供了 yum-config-manager ，并且 device mapper 存储驱动程序需要 device-mapper-persistent-data和lvm2    
    
   > sudo yum install -y yum-utils device-mapper-persistent-data lvm2  
  
  * 设置稳定的仓库(添加软件源信息)   
  
   > sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo  
    
  * 更新 yum 缓存：  
  
   > sudo yum makecache fast  
    
  * 安装 Docker Engine-Community   
   
   > sudo yum install docker-ce docker-ce-cli containerd.io  
  
  * 启动docker  
  
   > sudo systemctl start docker   
  
  * 通过运行 hello-world 映像来验证是否正确安装了 Docker Engine-Community  
    
   > sudo docker run hello-world  
  
  * 配置镜像加速器  
  
   > sudo mkdir -p /etc/docker     
   > sudo tee /etc/docker/daemon.json <<-'EOF'   
    {
      "registry-mirrors": ["https://o9nqigxx.mirror.aliyuncs.com"]  
    }  
    EOF  
   > sudo systemctl daemon-reload   
   > sudo systemctl restart docker  
    
  * systemctl命令是系统服务管理器指令: 

   > 启动docker： systemctl start docker  
   > 停止docker： systemctl stop docker  
   > 重启docker： systemctl restart docker  
   > 查看docker状态： systemctl status docker  
   > 开机启动： systemctl enable docker  

  * **Docker 基本命令**
  
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
       
       
  * **Docker 容器卷**
  
    * 用处 
      > 容器的持久化
      > 容器间继承+数据共享
    
    * 基本用法
      > docker run -it -v /mydatavolume:/mydatavolumecontainer centos
      > 设置只读权限：docker run -it -v /mydatavolume:/mydatavolumecontainer:ro centos
      > docker inspect <容器 ID>
   
    * 利用 Dockerfile 创建容器卷  
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
      
       
  * **Dockerfile**   
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


