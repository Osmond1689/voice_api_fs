# voice_api_fs
just-study<br>
### fs接口规划
	呼叫接口
		点击拨号
			crmuuid
			extensin_number
			customer_number
			product_code
			//call_type
		群呼拨号
			队列
				新增
				删除
				列表
			坐席状态
				签入
				签出
			群呼任务建立
				号码列表,队列名称
		客服接听
			复用队列
	动态管理用户
		创建用户
		删除用户
		列表展示
	通话记录
		cdr模块存数据库
	事件推送
        使用mq

## 1.安装mariadb
	安装odbc
		sudo apt-get install unixodbc
		安装mysql-connector-odbc.deb
		配置odbcinst.ini

		# Example driver definitions

		# Driver from the postgresql-odbc package

		# Setup from the unixODBC package

		[PostgreSQL]

		Description = ODBC for PostgreSQL

		Driver = /usr/lib/psqlodbc.so

		Setup = /usr/lib/libodbcpsqlS.so

		Driver64 = /usr/lib64/psqlodbc.so

		Setup64 = /usr/lib64/libodbcpsqlS.so

		FileUsage = 1



		# Driver from the mysql-connector-odbc package

		# Setup from the unixODBC package

		[MySQL]

		Description = ODBC for MySQL

		Driver = /usr/lib/libmyodbc5.so

		Setup = /usr/lib/libodbcmyS.so

		Driver64 = /usr/lib64/libmyodbc5.so

		Setup64 = /usr/lib64/libodbcmyS.so


		FileUsage = 1
		
		配置odbc.ini
		[ldap]

		 DSN = ldap 

		 Description = The Database for mysql Driver = MySQL 

		 Database = ldap

		 Server = 10.10.211.6

		 User = ldap

		 Password = ldap123

		 Port = 3306

		 Socket = /var/lib/mysql/mysql.sock 

		 ReadOnly = no 

		 charset = UTF8

## 2.安装pgsql
	apt install postgresql
	设置密码
	切换到postgres执行psql连接数据库
	ALTER USER postgres WITH PASSWORD 'abc123ABC456\!.';
	创建pgsql用户
	create user freeswitch with passwd ‘’；
	创建用户数据库
	create database xxx owen xxxuser；
	赋予所有权限
	grant all on database xxxx to xxxuser;
	\q退出
	
## 3.修改fs核心数据库到pg，switch.xml sofiax.xml
	修改dsn开启自动创建表
	
## 4.动态管理用户
	
## 5.话单
	mod_cdr_csv 转换为逗号分隔的形式
	mod_cdr_pg_csv 直接存入数据库 写入失败会存入文件
	mod_xml(json,format)_cdr 把话单以xml格式发往http服务器，如果服务器不响应就会保持channel不关闭，出现僵尸channel，返回非ok存本地文件
	
## 6.HA
	track_call intelnal