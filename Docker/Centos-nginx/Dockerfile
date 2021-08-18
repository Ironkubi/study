# Base images 基础镜像
FROM centos:8

# MAINTAINER 维护者信息
MAINTAINER Ironkubi

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
CMD ["-h"]