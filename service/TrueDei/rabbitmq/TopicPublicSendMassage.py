import pika
import sys
from rabbitmq.AllRabbitMQPublicConfig import getRabbitMQPublicConf
from tools.GetConfigFile import readConfigurationFileData

"""
TopicDiskData.py说明：
    这是对Linux服务器的磁盘进行监控
TopicPublicSendMassage.py说明：
    这是一个通用的发送message消息的类
"""
class topicPublicSendMassage():

    def __sendMessages__(self,exchange,routing_key,message):
        #获取通用的RabbitMQ的配置信息，可以减少代码量
        rabbitMQPublicConf = getRabbitMQPublicConf()
        #获取channel
        channel = rabbitMQPublicConf.__getRabbitMQChannel__()
        #指定使用的交换类型和交换器
        channel.exchange_declare(exchange=exchange,exchange_type='topic',durable=True)
        #绑定交换的类型，绑定队列，绑定发送的消息
        channel.basic_publish(exchange=exchange, routing_key=routing_key, body=message)
        #发送完之后自动关闭
        rabbitMQPublicConf.__close__()

    def __sendDiskDataMsg__(self,message):
        rcfd = readConfigurationFileData()
        self.__sendMessages__(rcfd.RabbitMQExchange,rcfd.RabbitMQDiskDataRouting_key,message)

    def __sendDiskWarningMsg__(self,message):
        rcfd = readConfigurationFileData()
        self.__sendMessages__(rcfd.RabbitMQExchange,rcfd.RabbitMQDiskWarningRouting_key,message)

    def __init__(self):
        pass
