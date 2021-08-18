## 创建Dockerfile文件路径
  
    mkdir /mydocker/nginx
    cd /mydocker/nginx
    vim Dockerfile
    将软件包考入当前目录:
    1、jdk-8u221-linux-x64.tar.gz
    2、nginx-1.13.7.tar.gz


 > 构建镜像
   docker build -t nginx:v3 . 