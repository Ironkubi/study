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