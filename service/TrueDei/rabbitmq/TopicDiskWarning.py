import pika
import sys

#你的RabbitMQ的地址
host = "sdgzs.net"
#RabbitMQ端口号
post = 5672
#创建的账号，当然了也可以使用默认的guest账号，密码也是guest
username = "admin"
#账号的密码
password = "123456"

# 创建一个有凭证的新实例
credentials = pika.PlainCredentials(username, password)
# 使用凭证连接RabbitMQ服务器
connection = pika.BlockingConnection(pika.ConnectionParameters(host,post,credentials=credentials))
#声明一个管道
channel = connection.channel()

#指定使用的交换类型和交换器
channel.exchange_declare(exchange='bin.linux.topic',exchange_type='topic',durable=True)
#如果有输入，就拿到输入的第一个数据为队列，否则默认为：anonymous.info（匿名的，当然了，可以随便修改哦）
# routing_key =  'disk.data'
routing_key =  'disk.warning'
#如果输入的数据，存在第二个，那么就把第二个当作消息，发送出去。否则默认消息就是：Hello World!
# message = '这是采集的扑通的监控disk的数据!'
message = '报警报警!'
#绑定交换的类型，绑定队列，绑定发送的消息
channel.basic_publish(exchange='bin.linux.topic', routing_key=routing_key, body=message)
#提示
print(" [x] Sent %r:%r" % (routing_key, message))
#关闭
connection.close()


# python topic_send.py python.error test    发送了一条python的错误信息，错误内容为test
# python topic_send.py mysql.info hello     发送了一条mysql的信息，信息内容为hello