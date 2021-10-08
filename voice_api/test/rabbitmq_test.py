import pika
#用户名密码
credentials = pika.PlainCredentials("sales_sys", "ZAQ!@#edc")
connection = pika.BlockingConnection(pika.ConnectionParameters(host="172.17.0.4", port=5672, virtual_host="voice_event",credentials=credentials))
channel = connection.channel()
# exchange="mm"，exchange(秘书)的名称
# exchange_type="fanout" , 秘书工作方式将消息发送给所有的队列
channel.exchange_declare(exchange="TAP.Events",exchange_type="topic",durable=True)
# 随机生成一个队列，并且在关闭消费者连接后，删除这个队列
#result = channel.queue_declare(exclusive=True)
# queue_name = result.method.queue
# 让exchange和queue进行绑定
channel.queue_bind(exchange="TAP.Events", queue="A_HANGUP_CDR")

def callback(ch, method, properties, body):
    print("消费者接收到了任务：%s" % body.decode("utf8"))

channel.basic_consume(callback, queue="A_HANGUP_CDR", no_ack=True)
channel.start_consuming()