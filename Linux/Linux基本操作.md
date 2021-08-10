# 七、Linux [菜鸟教程](https://www.runoob.com/w3cnote/linux-common-command-2.html)

 ## **配置网关**
 
   - ***虚拟机网络模式选择： NET模式***
    
   - ***centos下修改静态IP***  
   > 添加DNS地址，打开/etc/resolv.conf文件，添加DNS如下：    
       nameserver 114.114.114.114  
       nameserver 8.8.8.8  

   > 修改、添加网关配置文件，打开/etc/sysconfig/network-scripts/ifcfg-eth33文件，修改为以下内容：      
       BOOTPROTO="dhcp"  # 是否启动DHCP：none为禁用DHCP；static为使用静态ip地址；设置DHCP为使用DHCP服务    
       DEFROUTE="yes"  # 就是default route，是否把这个网卡设置为ipv4默认路由    
       ONBOOT="yes"  # 启动或者重启网络时是否启动该设备：yes是启用；no是禁用   
       IPADDR=192.xxx.188.30    # IP地址，自己设置的IP静态地址，前三位和主机的IP一样   
       GATEWAY=192.xxx.188.2    # 网关和主机的一样   
       NETMASK=255.255.255.0    
       DNS1=114.114.114.114     # NDS1  
       DNS2=8.8.8.8             # NDS2  

   > 重启网络：systemctl start NetworkManager  
   > 重启网关文件：nmcli c reload ifcfg-ens33  
    
 ## **JAVA 安装**
  
   > 检查旧版本：rpm -aq | grep java  
   > 卸载旧版本：rpm -e --nodeps java-1.7.0-openjdk  
   
   > 新建一个java目录存放JDK：mkdir /usr/java    
   > 修改java目录权限，否上上传不了：chmod 777 /usr/java/  
   > 解压命令：tar zxvf 压缩包名称 （例如：tar zxvf jdk-8u152-linux-x64.tar.gz）  
   > 删除命令：rm -f 压缩包名称 （例如 rm -f jdk-8u152-linux-x64.tar.gz）
   
   > 编辑命令：vi /etc/profile  
     export JAVA_HOME=/usr/java/jdk1.8.0_152  
     export CLASSPATH=.:$JAVA_HOME/jre/lib/rt.jar:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar  
     export PATH=$PATH:$JAVA_HOME/bin  
      
   > 生效文件：source /etc/profile  
   > 查看版本：java -version
   
 ## **安装 Android SDK**
   
   > 下载 Android SDK： https://www.androiddevtools.cn/ 
    
   > mkdir /opt/androidSdk  
   > cd /opt/androidSdk  
   > wget https://dl.google.com/android/repository/sdk-tools-linux-3859397.zip  
   > unzip sdk-tools-linux-3859397.zip  
   
   > 编辑命令：vi /etc/profile  
     export PATH USER LOGNAME MAIL HOSTNAME HISTSIZE HISTCONTROL  
     export PATH=$PATH:/opt/androidSdk/tools/bin  
     
   > 文件生效： source /etc/profile  
   
   > 查看已安装信息: sdkmanager --list  
   > 安装需要的package： sdkmanager "build-tools;26.0.2"  
   > 安装需要的package： sdkmanager "platform-tools"  
    
   > 编辑命令：vi /etc/profile  
     export PATH USER LOGNAME MAIL HOSTNAME HISTSIZE HISTCONTROL  
     export PATH=$PATH:/opt/androidSdk/tools/bin  
     export PATH=$PATH:/opt/androidSdk/platform-tools  
      
   > 文件生效： source /etc/profile  
   
   > 查看adb版本： adb version  


 ## **ls 查看目录文件**
 
   > ls -a    列出目录所有文件，包含以.开始的隐藏文件    
   > ls -A    列出除.及..的其它文   
   > ls -r    反序排列   
   > ls -t    以文件修改时间排序   
   > ls -S    以文件大小排序   
   > ls -h    以易读大小显示   
   > ls -l    除了文件名之外，还将文件的权限、所有者、文件大小等信息详细列出来    

 ## **cd 切换**
   
   > cd /    进入要目录  
   > cd ~    进入"家"目录  
   > cd -    进入上一次工作路径  
   > cd !$   把上个命令的参数作为cd参数使用。  

 ## **pwd 查看当前工作目录路径**
 
   > pwd    查看当前路径  
   > pwd -P    查看软链接的实际路径  

 ## **mkdir 创建文件夹**
 
   > mkdir t    当前工作目录下创建名为t的文件夹  
   > mkdir -p /tmp/test/t1/t    在tmp目录下创建路径为test/t1/t的目录，若不存在，则创建   

 ## **rm 删除文件**
 
   > rm -i *.log    删除任何.log文件；删除前逐一询问确认  
   > rm -rf test    删除test子目录及子目录中所有档案删除,并且不用一一确认   
   > rm -- -f*    删除以-f开头的文件  

 ## **rmdir 删除空目录**
 
   > rmdir -p parent/child/child11    当parent子目录被删除后使它也成为空目录的话，则顺便一并删除  

 ## **mv 移动/修改文件名**
 
   > mv test.log test1.txt    将文件test.log重命名为test1.txt  
   > mv llog1.txt log2.txt log3.txt /test3    将文件log1.txt,log2.txt,log3.txt移动到根的test3目录中  
   > mv -i log1.txt log2.txt    将文件file1改名为file2，如果file2已经存在，则询问是否覆盖   
   > mv * ../    移动当前文件夹下的所有文件到上一级目录    

 ## **cp 复制**
 
   > 命令参数：       
    -i   提示   
    -r   复制目录及目录内所有项目    
    -a   复制的文件与原文件时间一样   
     
   > 实例：  
    cp -ai a.txt test   复制a.txt到test目录下，保持原文件时间,如果原文件存在提示是否覆盖    
    cp -s a.txt link_a.txt   为a.txt建议一个链接（快捷方式）    

 ## **cat 显示文件详情**
 
   > cat主要有三大功能：  
    cat filename    一次显示整个文件    
    cat > filename    从键盘创建一个文件，只能创建新文件,不能编辑已有文件.    
    cat file1 file2 > file    将几个文件合并为一个文件   
     
   > 命令参数：     
    -b   对非空输出行号   
    -n   输出所有行号
      
   > 实例：   
    cat -n log2012.log log2013.log   把log2012.log的文件内容加上行号后输入 log2013.log 这个文件里   
    cat -b log2012.log log2013.log log.log   把log2012.log和log2013.log的文件内容加上行号（空白行不加）之后将内容附加到 log.log 里  
    cat >log.txt <<EOF   使用here doc生成新文件  

 ## **more　分页显示**
 
   > 功能类似于cat, more会以一页一页的显示方便使用者逐页阅读，而最基本的指令就是按空白键（space）就往下一页显示，按 b 键就会往回（back）一页显示     
    
   > 命令参数：   
    +n   从笫n行开始显示  
    -n   定义屏幕大小为n行  
    +/pattern   在每个档案显示前搜寻该字串（pattern），然后从该字串前两行之后开始显示  
    -c   从顶部清屏，然后显示  
    -d   提示“Press space to continue，’q’ to quit（按空格键继续，按q键退出）”，禁用响铃功能  
    -l   忽略Ctrl+l（换页）字符  
    -p   通过清除窗口而不是滚屏来对文件进行换页，与-c选项相似  
    -s   把连续的多个空行显示为一行  
    -u   把文件内容中的下画线去掉  

   > 常用操作命令：   
    Enter   向下n行，需要定义。默认为1行  
    Ctrl+F  向下滚动一屏  
    空格键   向下滚动一屏  
    Ctrl+B  返回上一屏  
    =       输出当前行的行号  
    ：f     输出文件名和当前行的行号  
    V      调用vi编辑器  
    !命令   调用Shell，并执行命令  
    q      退出more  

   > 实例：  
    more +3 text.txt 显示文件中从第3行起的内容  
    ls -l | more -5 在所列出文件目录详细信息，借助管道使每次显示5行  

 ## **less命令**
 
   > less 与 more 类似，但使用 less 可以随意浏览文件，而 more 仅能向前移动，却不能向后移动，而且 less 在查看之前不会加载整个文件。  

   > 常用命令参数  
    -i   忽略搜索时的大小写  
    -N   显示每行的行号  
    -o <文件名>   将less 输出的内容在指定文件中保存起来  
    -s   显示连续空行为一行  
    /字符串：  向下搜索“字符串”的功能  
    ?字符串：  向上搜索“字符串”的功能  
    n：  重复前一个搜索（与 / 或 ? 有关）  
    N：  反向重复前一个搜索（与 / 或 ? 有关）  
    -x <数字>   将“tab”键显示为规定的数字空格  
    b   向后翻一页  
    d   向后翻半页  
    h   显示帮助界面  
    Q   退出less 命令  
    u   向前滚动半页  
    y   向前滚动一行  
    空格键   滚动一行  
    回车键   滚动一页  
    [pagedown]： 向下翻动一页  
    [pageup]： 向上翻动一页  

   > 实例：  
    ps -aux | less -N    ps查看进程信息并通过less分页显示  
    less 1.log 2.log    查看多个文件  


 ## **head　从头ｎ行文本内容**
 
   > head 用来显示档案的开头至标准输出中，默认head命令打印其相应文件的开头 10 行。     

   > 常用参数：  
    -n<行数>   显示的行数（行数为复数表示从最后向前数）  
  
   > 实例：  
    head 1.log -n 20  显示 1.log 文件中前 20 行  
    head -c 20 log2014.log  显示 1.log 文件前 20 字节  
    head -n -10 t.log  显示 t.log最后 10 行  

 ## **tail　从尾ｎ行文本**
 
   > 用于显示指定文件末尾内容，不指定文件时，作为输入信息进行处理。常用查看日志文件。  

   > 常用参数：  
    -f 循环读取（常用于查看递增的日志文件）  
    -n<行数> 显示行数（从后向前）  
  
   > （1）循环读取逐渐增加的文件内容  
    ping 127.0.0.1 > ping.log &（后台运行：可使用jobs -l查看，也可使用fg将其移到前台运行）  
    tail -f ping.log（查看日志）  

 ## **which　查看可执行文件的位置**
 
   > 在linux要查找某个文件，但不知道放在哪里了，可以使用下面的一些命令来搜索：  
    ​which 查看可执行文件的位置。  
    ​whereis 查看文件的位置。  
    ​locate 配合数据库查看文件位置。  
    ​find 实际搜寻硬盘查询文件名称。  
    ​which是在PATH就是指定的路径中，搜索某个系统命令的位置，并返回第一个搜索结果。使用which命令，就可以看到某个系统命令是否存在，以及执行的到底是哪一个位置的命令。  

   > 常用参数：  
    -n 　指定文件名长度，指定的长度必须大于或等于所有文件中最长的文件名。  

   > 实例：  
    which ls 查看ls命令是否存在，执行哪个  
    which which 查看which    
    which cd（显示不存在，因为cd是内建命令，而which查找显示是PATH中的命令） 查看cd  

 ## **locate命令**
 
   > locate通过搜寻系统内建文档数据库达到快速找到档案，数据库由updatedb程序来更新，updatedb是由cron daemon周期性调用的。默认情况下locate命令在搜寻数据库时比由整个由硬盘资料来搜寻资料来得快，但较差劲的是locate所找到的档案若是最近才建立或 刚更名的，可能会找不到，在内定值中，updatedb每天会跑一次，可以由修改crontab来更新设定值。(etc/crontab)。  
   > locate与find命令相似，可以使用如*、?等进行正则匹配查找  

   > 常用参数：  
    ​-l num（要显示的行数）  
    -f 将特定的档案系统排除在外，如将proc排除在外  
    -r 使用正则运算式做为寻找条件  
    ​locate pwd 查找和pwd相关的所有文件(文件名中包含pwd）  
    ​locate /etc/sh 搜索etc目录下所有以sh开头的文件  
    locate -r '^/var.reason$'（其中.表示一个字符，表示任务多个；.*表示任意多个字符） 查找/var目录下，以reason结尾的文件  

 ## **find　文件树中查找文件**

   > find -atime -2   查找48小时内修改过的文件  
    find ./ -name '*.log'   在当前目录查找 以.log结尾的文件。 ". "代表当前目录  
    find /opt -perm 777   查找/opt目录下 权限为 777的文件  
    find -size +1000c   查找大于1K的文件  
    find -size 1000c 查找等于1000字符的文件  
    
   > -exec 参数后面跟的是command命令，它的终止是以;为结束标志的，所以这句命令后面的分号是不可缺少的，考虑到各个系统中分号会有不同的意义，所以前面加反斜杠。{} 花括号代表前面find查找出来的文件名。  
    find . -type f -mtime +10 -exec rm -f {} ; 在当前目录中查找更改时间在10日以前的文件并删除它们(无提醒）  
    find . -name '*.log' mtime +5 -ok -exec rm {} ; 当前目录中查找所有文件名以.log结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示。 按y键删除文件，按n键不删除  
    find . -f -name 'passwd*' -exec grep "pkg" {} ; 当前目录下查找文件名以passwd开头，内容包含"pkg"字符的文件  
    find . -name '*.log' -exec cp {} test3 ; 用exec选项执行cp命令  

   > -xargs find命令把匹配到的文件传递给xargs命令，而xargs命令每次只获取一部分文件而不是全部，不像-exec选项那样。这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。  

   > 实例：  
    （1）查找 48 小时内修改过的文件  
    find -atime -2  
    （2）在当前目录查找 以 .log 结尾的文件。 . 代表当前目录  
    find ./ -name '*.log'  
    （3）查找 /opt 目录下 权限为 777 的文件  
    find /opt -perm 777  
    （4）查找大于 1K 的文件  
    find -size +1000c  
    查找等于 1000 字符的文件  
    find -size 1000c   
    -exec 参数后面跟的是 command 命令，它的终止是以 ; 为结束标志的，所以这句命令后面的分号是不可缺少的，考虑到各个系统中分号会有不同的意义，所以前面加反斜杠。{} 花括号代表前面find查找出来的文件名。    
    （5）在当前目录中查找更改时间在10日以前的文件并删除它们(无提醒）  
    find . -type f -mtime +10 -exec rm -f {} \;  
    （6）当前目录中查找所有文件名以.log结尾、更改时间在5日以上的文件，并删除它们，只不过在删除之前先给出提示。 按y键删除文件，按n键不删除  
    find . -name '*.log' mtime +5 -ok -exec rm {} \;  
    （7）当前目录下查找文件名以 passwd 开头，内容包含 "pkg" 字符的文件  
    find . -f -name 'passwd*' -exec grep "pkg" {} \;  
    （8）用 exec 选项执行 cp 命令  
    find . -name '*.log' -exec cp {} test3 \;  
    -xargs find 命令把匹配到的文件传递给 xargs 命令，而 xargs 命令每次只获取一部分文件而不是全部，不像 -exec 选项那样。这样它可以先处理最先获取的一部分文件，然后是下一批，并如此继续下去。  
    find . -type f -print | xargs file    
    （10）查找当前目录下所有以 js 结尾的并且其中包含 'editor' 字符的普通文件  
    find . -type f -name "*.js" -exec grep -lF 'ueditor' {} \;  
    find -type f -name '*.js' | xargs grep -lF 'editor'    
    （11）利用 xargs 执行 mv 命令  
    find . -name "*.log" | xargs -i mv {} test4  
    （12）用 grep 命令在当前目录下的所有普通文件中搜索 hostnames 这个词，并标出所在行：  
    find . -name \*(转义） -type f -print | xargs grep -n 'hostnames'    
    （13）查找当前目录中以一个小写字母开头，最后是 4 到 9 加上 .log 结束的文件：  
    find . -name '[a-z]*[4-9].log' -print  
    （14）在 test 目录查找不在 test4 子目录查找  
    find test -path 'test/test4' -prune -o -print   
    （15）实例1：查找更改时间比文件 log2012.log新但比文件 log2017.log 旧的文件  
    find -newer log2012.log ! -newer log2017.log  
    # 使用 depth 选项：  
    depth 选项可以使 find 命令向磁带上备份文件系统时，希望首先备份所有的文件，其次再备份子目录中的文件。    
    实例：find 命令从文件系统的根目录开始，查找一个名为 CON.FILE 的文件。 它将首先匹配所有的文件然后再进入子目录中查找    
    find / -name "CON.FILE" -depth -print    

 ## **grep　文本搜索命令**
 
   > 强大的文本搜索命令，grep(Global Regular Expression Print)全局正则表达式搜索  

   > grep的工作方式是这样的，它在一个或多个文件中搜索字符串模板。如果模板包括空格，则必须被引用，模板后的所有字符串被看作文件名。搜索的结果被送到标准输出，不影响原文件内容。  

   > 命令格式：  
    grep [option] pattern file|dir  
  
   > 常用参数：    
     -A n --after-context显示匹配字符后n行  
     -B n --before-context显示匹配字符前n行  
     -C n --context 显示匹配字符前后n行  
     -c --count 计算符合样式的列数  
     -i 忽略大小写  
     -l 只列出文件内容符合指定的样式的文件名称  
     -f 从文件中读取关键词  
     -n 显示匹配内容的所在文件中行数  
     -R 递归查找文件夹  

   > 实例：   
     ps -ef | grep svn  查找指定进程  
     ps -ef | grep svn -c  查找指定进程个数  
     cat test1.txt | grep -f key.log  从文件中读取关键词  
     grep -lR '^grep' /tmp  从文件夹中递归查找以grep开头的行，并只列出文件  
     grep '[x]' test.txt  查找非x开关的行内容  
     grep -E 'ed|at' test.txt  显示包含ed或者at字符的内容行  

 ## **chmod　访问权限**
 
   > 常用参数：    
    -c   当发生改变时，报告处理信息  
    -R   处理指定目录以及其子目录下所有文件  
  
   > 权限范围：   
    u ：  目录或者文件的当前的用户  
    g ：  目录或者文件的当前的群组  
    o ：  除了目录或者文件的当前用户或群组之外的用户或者群组  
    a ：  所有的用户及群组  

   > 权限代号：   
    r ：  读权限，用数字4表示  
    w ：  写权限，用数字2表示  
    x ：  执行权限，用数字1表示   
    - ：  删除权限，用数字0表示  
    s ：  特殊权限  

   > 实例：  
    chmod a+x t.log    增加文件t.log所有用户可执行权限  
    chmod u=r t.log -c    撤销原来所有的权限，然后使拥有者具有可读权限,并输出处理信息  
    chmod 751 t.log -c（或者：chmod u=rwx,g=rx,o=x t.log -c)    给file的属主分配读、写、执行(7)的权限，给file的所在组分配读、执行(5)的权限，给其他用户分配执行(1)的权限  
    chmod u+r,g+r,o+r -R text/ -c    将test目录及其子目录所有文件添加可读权限   

 ## **chown　改为指定的用户或组**
 
   > 常用参数：    
    -c 显示更改的部分的信息  
    -R 处理指定目录及子目录  
  
   > 实例：    
    chown -c mail:mail log2012.log   改变拥有者和群组 并显示改变信息  
    chown -c :mail t.log   改变文件群组  
    chown -cR mail: test/   改变文件夹及子文件目录属主及属组为mail  

 ## **df　显示磁盘空间**
 
   > 显示磁盘空间使用情况。获取硬盘被占用了多少空间，目前还剩下多少空间等信息，如果没有文件名被指定，则所有当前被挂载的文件系统的可用空间将被显示。默认情况下，磁盘空间将以 1KB 为单位进行显示，除非环境变量 POSIXLY_CORRECT 被指定，那样将以512字节为单位进行显示    
   
   > 常用参数：   
    -a   全部文件系统列表     
    -h   以方便阅读的方式显示信息    
    -i   显示inode信息    
    -k   区块为1024字节    
    -l   只显示本地磁盘   
    -T   列出文件系统类型    

   > 实例：  
    （1）显示磁盘使用情况    
      df -l   
    （2）以易读方式列出所有文件系统及其类型   
      df -haT   

 ## **date　显示时间**
 
   > 显示或设定系统的日期与时间  

   > 命令参数：  
    -d<字符串> 　显示字符串所指的日期与时间。字符串前后必须加上双引号。  
    -s<字符串> 　根据字符串来设置日期与时间。字符串前后必须加上双引号。  
    -u 　显示GMT   
    %H  小时(00-23)  
    %I  小时(00-12)  
    %M  分钟(以00-59来表示)  
    %s  总秒数。起算时间为1970-01-01 00:00:00 UTC。  
    %S  秒(以本地的惯用法来表示)  
    %a  星期的缩写。  
    %A  星期的完整名称。  
    %d  日期(以01-31来表示)。  
    %D  日期(含年月日)。  
    %m  月份(以01-12来表示)。  
    %y  年份(以00-99来表示)。  
    %Y  年份(以四位数来表示)。  

   > 实例：  
    （1）显示下一天  
      date +%Y%m%d --date="+1 day" //显示下一天的日         
    （2）-d参数使用  
      date -d "nov 22" 今年的 11 月 22 日是星期三  
      date -d '2 weeks' 2周后的日期  
      date -d 'next monday' (下周一的日期)  
      date -d next-day +%Y%m%d（明天的日期）或者：date -d tomorrow +%Y%m%d  
      date -d last-day +%Y%m%d(昨天的日期) 或者：date -d yesterday +%Y%m%d  
      date -d last-month +%Y%m(上个月是几月)  
      date -d next-month +%Y%m(下个月是几月)   

 ## **ps　查看进程**
 
   > 实例：  
    ps -ef 显示当前所有进程环境变量及进程间关系  
    ps -A 显示当前所有进程  
    ps -aux | grep apache 与grep联用查找某进程  
    ps aux | grep '(cron|syslog)' 找出与 cron 与 syslog 这两个服务有关的 PID 号码  

 ## **kill　杀死进程**
 
   > 实例：  
   > kill -9 $(ps -ef | grep pro1) 先使用ps查找进程pro1，然后用kill杀掉  

 ## **free　显示内存使用情况**
  
   > 显示内存使用情况  
    free  
    free -k  
    free -m  

   > 以总和的形式显示内存的使用信息  
    free -t  

   > 周期性查询内存使用情况  
    free -s 10  

 ## **VI 和vim 编辑文本**
 
   > 打开编辑  
    vi filename   :打开或新建文件,并将光标置于第一行首  
    vi n filename   ：打开文件,并将光标置于第n行首  
    vi filename   ：打开文件,并将光标置于一行首  
    vi /pattern filename  ：打开文件,并将光标置于第一个与pattern匹配的串处  
    vi -r filename   ：在上次正用vi编辑时发生系统崩溃,恢复filename  
    vi filename....filename   ：打开多个文件,依次进行编辑  

   > 屏幕翻滚类命令  
    Ctrl u  ：向文件首翻半屏  
    Ctrl d  ：向文件尾翻半屏  
    Ctrl f  ：向文件尾翻一屏  
    Ctrl＋b  ：向文件首翻一屏  
    nz  ：将第n行滚至屏幕顶部,不指定n时将当前行滚至屏幕顶部.  

   > 插入文本类命令  
    i  ：在光标前  
    I  ：在当前行首  
    a  ：光标后  
    A  ：在当前行尾  
    o  ：在当前行之下新开一行  
    O  ：在当前行之上新开一行  
    r  ：替换当前字符  
    R  ：替换当前字符及其后的字符,直至按ESC键  
    s  ：从前光标位置处开始,以输入的文本替代指定数目的字符  

   > 编辑保存  
    按ESC键   跳到命令模式，然后：  
    :w   保存文件但不退出vi  
    :w file   将修改另外保存到file中，不退出vi  
    :w!   强制保存，不推出vi  
    :wq   保存文件并退出vi  
    :wq!   强制保存文件，并退出vi  
    :q   不保存文件，退出vi
    :q!  不保存文件，强制退出vi  
    e!   放弃所有修改，从上次保存文件开始再编辑  

 ## **echo指令向文件写入内容**
 
   > 参数：  
    -n 不尾随换行符  
    -e 启用解释反斜杠的转义功能  
    -E 禁用解释反斜杠的转义功能(默认)  
    
   > 实例：  
     1、覆盖文件内容    
      echo "Raspberry" > test.txt  使用>指令覆盖文件原内容并重新输入内容，若文件不存在则创建文件。  
     2、追加文件内容  
      echo "Intel Galileo" >> test.txt  使用>>指令向文件追加内容，原内容将保存。  

