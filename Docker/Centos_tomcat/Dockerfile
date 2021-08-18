#指定操作的镜像
FROM centos:8

#维护者信息
MAINTAINER Ironkubi

#把tomcat和jdk添加到容器中并解压
ADD jdk-8u221-linux-x64.tar.gz /usr/local/
ADD apache-tomcat-9.0.52.tar.gz /usr/local/

#进入工作目录
WORKDIR /usr/local/

#重命名
RUN mv jdk1.8.0_221 java
RUN mv apache-tomcat-9.0.52 tomcat9

#设置环境变量
ENV JAVA_HOME /usr/local/java
ENV JRE_HOME /usr/local/java/jre
ENV CLASSPATH /usr/local/java/lib:/usr/local/java/jre/lib
ENV PATH /usr/local/java/bin:$PATH

#安装vim编辑器
RUN yum -y install vim

#暴露端口
EXPOSE 8080

#启动tomcat
ENTRYPOINT ["/usr/local/tomcat9/bin/catalina.sh","run"]
