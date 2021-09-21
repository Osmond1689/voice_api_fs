# voice_api_fs
just-study<br>
### fs接口规划
	* 呼叫接口
		* 点击拨号
			* crmuuid
			* extensin_number
			* customer_number
			* product_code
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
