# Flask
#20170509 今天试着用阿里云服务器做开发  发现easy_install都没有安装(也可能我用的时候漏掉了下划线)  用wget的方法先安装
#20170509 在安装MySQL-python时报错  运行yum install python-devel mysql-devel zlib-devel openssl-devel安装依赖包后，重新pip install MySQL-python，成功！
#20170510 为了把项目部署到阿里云上面  先在云服务器上pip install uwsgi（touch xxx.ini然后修改） 然后pip install nginx （修改default.conf）
#20170510 悲催 用的阿里云服务器 被要求备案 现在准备弄一个AWS的云主机
