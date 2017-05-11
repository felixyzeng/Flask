# Flask
#20170509 今天试着用阿里云服务器做开发  发现easy_install都没有安装(也可能我用的时候漏掉了下划线)  用wget的方法先安装
#20170509 在安装MySQL-python时报错  运行yum install python-devel mysql-devel zlib-devel openssl-devel安装依赖包后，重新pip install MySQL-python，成功！
#20170510 为了把项目部署到阿里云上面  先在云服务器上pip install uwsgi（touch xxx.ini然后修改） 然后pip install nginx （修改default.conf）
#20170510 悲催 用的阿里云服务器 被要求备案 现在准备弄一个AWS的云主机

###20170511 
因为部署域名不想备案，所以从阿里云重新买了一个按使用时长付费的香港的云服务器EC2
下面就重新部署一次Flask吧，算是复习，这次也好把整个过程详细记录下来：
1.首先在/home目录下创建www目录  mkdir /home/venv
2.然后创建一个虚拟环境来隔离其它项目（虽然现在还没有其它项目，但以后肯定会有的）  pip install virtualenv
3.virtualenv /home/venv
4.source /home/venv/bin/activate  这个命令以后在做这个项目的时候要经常用
5.安装flask(pip install flask)  
flask以后会有各种依赖文件，可以写在requirements中 用pip install -r requirements.txt一次性安装
6.安装uwsgi(pip install uwsgi)  
uwsgi的依赖包有gcc和python-dev 分别可以用pip install gcc和yum install python-devel的方式安装，如果安装出错就试一下这两个命令
在/home/venv下信件uwsgiconfig.ini

7.安装nginx(yum install nginx)  

tips:
1.运行uwsgi时出问题import flask一直报错，后来退出venv虚拟环境后在全局环境下安装flask就成功了，这个问题以后再研究
2.yum install links可以用links命令来简单浏览网页
3.killall -9 uwsgi可以用来杀掉所有uwsgi进程

###20170511
